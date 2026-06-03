# Customer Churn Prediction — Telecom Industry

## Business Problem
A telecom company is losing customers every month. Acquiring a new customer costs 5x more than retaining an existing one. This project predicts which customers are likely to churn so the retention team can act proactively before losing them.

## Dataset
- Source: IBM Telco Customer Churn (Kaggle)
- Records: 7,044 customers after cleaning
- Features: 21 columns including demographics, services, and billing info
- Target: Churn (Yes/No)
- Note: Real-world data quality issues were intentionally injected for realistic preprocessing practice including nulls, duplicates, inconsistent categories, outliers, wrong datatypes, and noise columns

## Tech Stack
- Python: Pandas, NumPy, Scikit-learn, XGBoost, SHAP, Imbalanced-learn
- Visualization: Matplotlib, Seaborn
- Dashboard: Power BI
- Environment: Google Colab
- Version Control: GitHub

## Project Workflow
1. Problem Understanding and Business Context
2. Data Injection — 6 real-world quality issues simulated
3. Data Cleaning and Preprocessing
4. Exploratory Data Analysis
5. Feature Engineering and Encoding
6. Class Balancing with SMOTE
7. Model Building and Evaluation
8. SHAP Explainability
9. Power BI Business Dashboard

## Key Business Insights
- Month-to-month contract customers churn significantly more than long-term contract customers
- Customers in their first 12 months are at highest churn risk
- Fiber optic internet users show higher churn — likely due to high pricing vs expectations
- Higher monthly charges correlate strongly with churn probability

## Model Performance

| Model               | Accuracy | Recall | F1    | AUC   |
|---------------------|----------|--------|-------|-------|
| Logistic Regression | 74.6%    | 77.5%  | 61.8% | 84.0% |
| Random Forest       | 77.7%    | 58.6%  | 58.2% | 81.8% |
| XGBoost             | 77.3%    | 58.3%  | 57.7% | 81.6% |

Selected Model: Logistic Regression
Reason: Highest Recall and AUC — in churn prediction, missing an actual churner (false negative) is more costly than a false alarm. Recall directly minimizes this risk.

## SHAP Feature Importance — Top 5 Drivers of Churn
1. InternetService — Fiber optic (0.73)
2. Tenure (0.69)
3. Monthly Charges (0.50)
4. Contract — Two year (0.48)
5. Streaming Services (0.27)

## Power BI Dashboard
Three page interactive dashboard:
- Page 1: KPI Overview — Total Customers, Churn Rate, Predicted Churners, Average Churn Probability
- Page 2: Churn Analysis — by Contract Type, Internet Service, Tenure Group
- Page 3: ML Insights — SHAP Feature Importance

## Project Structure
customer-churn-prediction/
    churn_prediction.ipynb
    churn_dashboard.csv
    shap_importance.csv
    README.md

## Author
Thanha Shajahan
Data Science and AI — Luminar Technolab
