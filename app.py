
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("company_financials_clean.csv")

# Dashboard Title
st.title("📊 Havells India Financial Dashboard")

# KPI Section
st.header("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Latest Sales", f"{df['Sales'].iloc[-1]:,.0f}")
col2.metric("Latest Net Profit", f"{df['Net_Profit'].iloc[-1]:,.0f}")
col3.metric("Latest OPM %", f"{df['OPM_Percent'].iloc[-1]}%")

# Sales & Net Profit Chart
st.header("Sales and Net Profit Trend")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Period"], df["Sales"], marker="o", label="Sales")
ax.plot(df["Period"], df["Net_Profit"], marker="o", label="Net Profit")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# OPM Chart
st.header("Operating Profit Margin")

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(df["Period"], df["OPM_Percent"])
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig2)

# Box Plot
st.header("Net Profit Distribution")

fig3, ax3 = plt.subplots(figsize=(6, 5))
df.boxplot(column="Net_Profit", by="Profit_Trend", ax=ax3)
plt.suptitle("")
plt.tight_layout()

st.pyplot(fig3)

# Model Comparison
st.header("Machine Learning Model Comparison")

comparison = pd.DataFrame({
    "Model": ["Logistic Regression", "Decision Tree"],
    "Accuracy": [0.50, 0.75]
})

st.table(comparison)

# Note on small-sample limitation (Required by Project Rubric)
st.caption("⚠️ **Note on Model Performance:** Due to the small sample size (~12-16 quarterly periods), accuracy metrics are subject to high variance and small-sample limitations.")
