import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. SETUP & DATA GENERATION
print("Generating Synthetic UK Clinical Trial Data...")
np.random.seed(42)

# Real London Boroughs and their approximate Deprivation profiles (1=High Deprivation, 10=Low)
borough_profiles = {
    'Tower Hamlets': 2, 'Hackney': 2, 'Newham': 3, 'Barking & Dagenham': 2,
    'Westminster': 6, 'Camden': 5, 'Islington': 4, 'Kensington & Chelsea': 8,
    'Richmond upon Thames': 9, 'Bromley': 7, 'Croydon': 5, 'Lewisham': 4,
    'Ealing': 5, 'Hillingdon': 6, 'Haringey': 3, 'Southwark': 3
}

boroughs = list(borough_profiles.keys())
n_records = 1000
data_list = []

for i in range(n_records):
    b = np.random.choice(boroughs)
    imd_base = borough_profiles[b]
    
    # Features
    age = np.random.randint(18, 85)
    imd_score = max(1, min(10, imd_base + np.random.randint(-1, 2)))
    # Distance: Central boroughs are closer to our "Trial Hub"
    distance = np.random.uniform(2, 8) if b in ['Camden', 'Westminster', 'Islington'] else np.random.uniform(10, 25)
    comorbidities = np.random.poisson(1.2)
    
    # Logic for Dropout (Higher distance + Lower IMD = Higher probability)
    dropout_prob = (distance * 0.04) + ((11 - imd_score) * 0.06) + (comorbidities * 0.05)
    is_dropout = 1 if dropout_prob > 0.7 else 0
    
    data_list.append([i, b, age, imd_score, round(distance, 2), comorbidities, is_dropout])

# Create DataFrame
columns = ['Patient_ID', 'Borough', 'Age', 'IMD_Decile', 'Distance_Miles', 'Comorbidities', 'Dropped_Out']
df = pd.DataFrame(data_list, columns=columns)

# 2. PATIENT STRATIFICATION (K-MEANS CLUSTERING)
print("Clustering patients into 'Personas'...")
scaler = StandardScaler()
features_for_clustering = ['Age', 'IMD_Decile', 'Distance_Miles', 'Comorbidities']
X_scaled = scaler.fit_transform(df[features_for_clustering])

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Patient_Persona_ID'] = kmeans.fit_predict(X_scaled)

# 3. PREDICTIVE MODELING (DROPOUT PROBABILITY)
print("Calculating Risk Scores...")
X_train = df[['Age', 'IMD_Decile', 'Distance_Miles', 'Comorbidities']]
y_train = df['Dropped_Out']

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Add the 'Risk Probability' to the CSV so Tableau can show % Risk
df['Attrition_Risk_Percentage'] = rf.predict_proba(X_train)[:, 1] * 100

# 4. EXPORT TO CSV
df.to_csv('UK_Clinical_Trial_Final.csv', index=False)
print("SUCCESS! File saved as 'UK_Clinical_Trial_Final.csv'")
print(df.head())
