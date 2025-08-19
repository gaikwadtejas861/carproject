import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import math

# ---- Professional UI CSS ----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    .stApp {
        background: linear-gradient(135deg, #e0eafc, #cfdef3 85%);
        font-family: 'Poppins', sans-serif;
        color: #222;
        padding-bottom: 40px;
    }
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        color: #243B55;
        margin-bottom: 0.8em;
        letter-spacing: 2px;
        user-select: none;
    }
    .section-card {
        background: #fff;
        border-radius: 20px;
        box-shadow: 0 14px 30px rgba(36,59,85,0.11);
        padding: 22px 28px;
        margin-bottom: 24px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    label, .stNumberInput label, .stMetric label {
        color: #243B55 !important;
        font-weight: 700 !important;
        font-size: 1.12rem !important;
        letter-spacing: 1px;
        user-select: none;
    }
    .stNumberInput input {
        color: #252525 !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        border: 2px solid #243B55 !important;
        background: #eef6fa !important;
        font-size: 1.09rem !important;
    }
    div[data-testid="stMetric"] div {
        font-size: 1.14rem !important;
        font-weight: 800 !important;
        color: #243B55 !important;
        text-shadow: 0 0 8px #cfd8ff1a;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 1.18rem !important;
        font-weight: 700 !important;
        color: #486d9f !important;
    }
    .payment-schedule-title {
        margin-top: 2em;
        text-align: center;
        font-size: 1.27rem;
        font-weight: 700;
        color: #243B55;
    }
    </style>
""", unsafe_allow_html=True)

# ---- App Title ----

st.markdown('<div class="main-title">Mortgage Repayments Calculator</div>', unsafe_allow_html=True)

# ---- Input Section ----
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.write("### Input Data :")
col1, col2 = st.columns(2)
Car_Price = col1.number_input("Car Price", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Calculations ----
loan_amount = Car_Price - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
) if monthly_interest_rate > 0 else loan_amount / number_of_payments

total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

# ---- Repayment Metrics ----
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.write("### Repayments :")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly Repayments", value=f"₹{monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"₹{total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"₹{total_interest:,.0f}")
st.markdown('</div>', unsafe_allow_html=True)

# ---- Payment Schedule ----
schedule = []
remaining_balance = loan_amount

for i in range(1, int(number_of_payments)+1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

st.markdown(f'<div class="payment-schedule-title">Payment Schedule :</div>', unsafe_allow_html=True)
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)

