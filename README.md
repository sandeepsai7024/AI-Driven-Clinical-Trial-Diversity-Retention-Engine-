# AI-Driven-Clinical-Trial-Diversity-Retention-Engine-🏥💻

 🏆 Project Overview
 
In the UK, the **MHRA** is increasingly mandating that clinical trials reflect the diversity of the population. Currently, **30% of patients drop out** of Phase III trials, with an average replacement cost of **£30,000 per patient**.

This project uses **Synthetic Health Data** and **Machine Learning** to predict patient attrition before it happens, allowing trial managers to re-allocate budgets to under-represented and high-risk UK boroughs.

---

🛠️ The Tech Stack
* **Python (Scikit-Learn):** K-Means Clustering for patient personas & Random Forest for attrition prediction.
* **Data:** Synthetic UK patient records including IMD (Index of Multiple Deprivation) and geospatial logistics.
* **Power BI:** A strategic dashboard for clinical trial ROI and site selection.

---

 📊 Key Insights & Logic

 1. Patient Stratification (K-Means)
We identified 4 distinct "Patient Personas." The highest-risk group, **"The Logistically Excluded,"** consists of patients in high-deprivation boroughs with travel distances >12 miles. 

 2. The "Smoking Gun" (Attrition Drivers)
As visualized in the **Risk vs. Distance Scatter Plot**, every 5 miles of additional travel increases predicted dropout risk by ~15%.



#### 3. Financial Impact
* **Total Cost at Risk:** £1.8M (based on 30% historical attrition).
* **Potential Savings:** **£480,000** by implementing targeted interventions (e.g., travel vouchers or home nursing) for the top 20% high-risk patients identified by the model.

---

🚀 How to Use This Project
1. "Run the Model: Execute `attrition_engine.py` to generate the risk-scored CSV.
2. **View the Dashboard:** Open the Power BI file to see the London Borough Heatmap.
3. **Strategy:** Use the "Borough Slicer" to identify where to deploy mobile clinic units.

---

### 📜 Compliance Note
This model directly supports the **Health Research Authority (HRA)** and **MHRA** diversity requirements by identifying participation barriers in underserved communities (IMD Deciles 1-3).
