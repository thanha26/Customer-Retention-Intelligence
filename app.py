import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("customer_churn_model.pkl")
scaler = joblib.load("churn_scaler.pkl")
columns = joblib.load("churn_columns.pkl")

st.set_page_config(
    page_title="Customer Retention Intelligence",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
/* Make dropdown selected values visible */
div[data-baseweb="select"] span {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Make dropdown input text visible */
div[data-baseweb="select"] div {
    color: #111827 !important;
}

/* Number input text */
div[data-baseweb="input"] input {
    color: #ffffff !important;
    background: #2b2d38 !important;
    font-weight: 600 !important;
}

/* Number input placeholder */
div[data-baseweb="input"] input::placeholder {
    color: #cbd5e1 !important;
}

/* Make placeholders visible */
input::placeholder {
    color: #6b7280 !important;
}

/* Make warning / validation message readable */
div[data-testid="stAlert"] {
    background-color: #fff7ed !important;
    color: #7c2d12 !important;
    border: 1px solid #fed7aa !important;
    border-radius: 12px !important;
}

div[data-testid="stAlert"] p {
    color: #7c2d12 !important;
    font-weight: 600 !important;
}

/* General markdown text */
.stMarkdown, .stMarkdown p, p {
    color: #111827 !important;
}
.stApp {
    background: #f7f9fc;
    color: #1f2937;
}

.main-header {
    background: white;
    padding: 45px;
    border-radius: 22px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    margin-bottom: 35px;
    border: 1px solid #e5e7eb;
    position: relative;
    overflow: hidden;
}

.main-header:before {
    content: "";
    position: absolute;
    top: -70px;
    right: -70px;
    width: 260px;
    height: 260px;
    background: radial-gradient(circle, rgba(59,130,246,0.18), transparent 70%);
}

.main-header h1 {
    color: #111827;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.main-header p {
    color: #4b5563;
    font-size: 17px;
}

.section-card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 8px 28px rgba(0,0,0,0.06);
    border: 1px solid #e5e7eb;
    margin-bottom: 25px;
}

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 20px;
}

label, .stSelectbox label, .stNumberInput label {
    color: #111827 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

/* Dropdowns */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border-radius: 12px !important;
}

/* Number input container */
div[data-baseweb="input"] {
    background: #2b2d38 !important;
    border-radius: 12px !important;
}

.stButton > button {
    background: linear-gradient(135deg, #111827 0%, #1d4ed8 45%, #38bdf8 100%);
    color: #ffffff !important;
    border-radius: 18px;
    padding: 16px 28px;
    font-size: 19px;
    font-weight: 800;
    border: 1px solid rgba(255,255,255,0.35);
    width: 100%;
    box-shadow: 0 14px 30px rgba(37,99,235,0.32);
    transition: all 0.25s ease-in-out;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 18px 38px rgba(37,99,235,0.45);
    background: linear-gradient(135deg, #38bdf8 0%, #2563eb 45%, #111827 100%);
    color: #ffffff !important;
}

.stButton > button:active {
    transform: scale(0.98);
}
.result-card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-left: 8px solid;
    margin-top: 25px;
}

.result-card h2 {
    margin-bottom: 8px;
    color: #111827;
}

.result-card h1 {
    font-size: 44px;
    font-weight: 800;
}

.recommend-card {
    background: #ffffff;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 28px rgba(0,0,0,0.06);
    margin-top: 18px;
    color: #374151;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>Customer Retention Intelligence System</h1>
    <p>Predict customer churn risk and generate data-driven retention recommendations.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Customer Information</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Select", "Female", "Male"])
    senior_citizen_input = st.selectbox("Senior Citizen", ["Select", "No", "Yes"])
    partner = st.selectbox("Partner", ["Select", "Yes", "No"])
    dependents = st.selectbox("Dependents", ["Select", "Yes", "No"])
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=None, placeholder="Enter tenure")

with col2:
    phone_service = st.selectbox("Phone Service", ["Select", "Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Select", "No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["Select", "DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Select", "Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Select", "Yes", "No", "No internet service"])

with col3:
    contract = st.selectbox("Contract", ["Select", "Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Select", "Yes", "No"])
    payment_method = st.selectbox(
        "Payment Method",
        ["Select", "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=150.0, value=None, placeholder="Enter amount")
    total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=None, placeholder="Enter total")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Service Details</div>', unsafe_allow_html=True)

col4, col5, col6, col7 = st.columns(4)

with col4:
    device_protection = st.selectbox("Device Protection", ["Select", "Yes", "No", "No internet service"])

with col5:
    tech_support = st.selectbox("Tech Support", ["Select", "Yes", "No", "No internet service"])

with col6:
    streaming_tv = st.selectbox("Streaming TV", ["Select", "Yes", "No", "No internet service"])

with col7:
    streaming_movies = st.selectbox("Streaming Movies", ["Select", "Yes", "No", "No internet service"])

st.markdown('</div>', unsafe_allow_html=True)

if st.button("Predict Churn Risk"):

    selected_values = [
        gender, senior_citizen_input, partner, dependents,
        phone_service, multiple_lines, internet_service,
        online_security, online_backup, contract,
        paperless_billing, payment_method, device_protection,
        tech_support, streaming_tv, streaming_movies
    ]

    if "Select" in selected_values or tenure is None or monthly_charges is None or total_charges is None:
        st.warning("Please fill all fields before prediction.")

    else:
        senior_citizen = 1 if senior_citizen_input == "Yes" else 0

        user_data = {
            "gender": gender,
            "SeniorCitizen": senior_citizen,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone_service,
            "MultipleLines": multiple_lines,
            "InternetService": internet_service,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "StreamingTV": streaming_tv,
            "StreamingMovies": streaming_movies,
            "Contract": contract,
            "PaperlessBilling": paperless_billing,
            "PaymentMethod": payment_method,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges
        }

        input_df = pd.DataFrame([user_data])

        binary_mapping = {
            "Female": 0,
            "Male": 1,
            "No": 0,
            "Yes": 1
        }

        binary_cols = ["gender", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]

        for col in binary_cols:
            input_df[col] = input_df[col].map(binary_mapping)

        if "TotalCharges" in input_df.columns and "TotalCharges" not in columns:
            input_df = input_df.drop(columns=["TotalCharges"])

        input_df = pd.get_dummies(input_df, drop_first=True)
        input_df = input_df.reindex(columns=columns, fill_value=0)

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)[0]
        churn_probability = model.predict_proba(input_scaled)[0][1] * 100



        if prediction == 1:
            color = "#ef4444"
            risk = "High Churn Risk"
            recommendations = """
            - Offer a personalized discount or loyalty benefit.
            - Provide quick issue resolution and priority support.
            - Encourage the customer to move to a longer-term contract.
            - Review pricing, service quality, and payment method concerns.
            """
        else:
            color = "#22c55e"
            risk = "Low Churn Risk"
            recommendations = """
            - Continue providing consistent service quality.
            - Maintain regular engagement with the customer.
            - Offer loyalty rewards to improve long-term retention.
            - Monitor customer satisfaction periodically.
            """

        st.markdown(f"""
        <div class="result-card" style="border-left-color:{color};">
            <h2>Prediction Result</h2>
            <h1 style="color:{color};">{risk}: {churn_probability:.1f}%</h1>
            <p>Model used: Logistic Regression</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(float(churn_probability / 100))

        st.markdown("""
        <div class="recommend-card">
            <h3>Retention Recommendations</h3>
        """, unsafe_allow_html=True)

        st.write(recommendations)

        st.markdown("</div>", unsafe_allow_html=True)