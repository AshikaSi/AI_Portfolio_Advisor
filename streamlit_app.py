import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pipeline.run_advisor import run_advisor


st.set_page_config(
    page_title="Future Portfolio Advisor",
    layout="centered"
)

st.title("📊 Future Portfolio Advisor")

# ----------------------------
# User Inputs
capital = st.number_input(
    "Initial Investment",
    min_value=1000,
    step=1000,
    value=10000
)

years = st.slider(
    "Investment Horizon (Years)",
    min_value=1,
    max_value=30,
    value=5
)

risk_profile = st.selectbox(
    "Risk Profile",
    ["conservative", "moderate", "aggressive"]
)

# ----------------------------
# Run Advisor
if st.button("Optimize Portfolio"):
    with st.spinner("Optimizing portfolio..."):
        result = run_advisor(
            capital=capital,
            years=years,
            risk_profile=risk_profile
        )

    st.success("Optimization Complete")

    # ----------------------------
    # Portfolio Weights
    st.subheader("📌 Portfolio Allocation")

    weights_df = pd.DataFrame.from_dict(
        result["portfolio"]["weights"],
        orient="index",
        columns=["Weight"]
    )

    st.bar_chart(weights_df)

    # ----------------------------
    # Metrics
    st.subheader("📈 Portfolio Metrics")

    col1, col2, col3 = st.columns(3)
    col1.metric("Expected Return", f"{result['portfolio']['expected_return']:.2%}")
    col2.metric("Volatility", f"{result['portfolio']['volatility']:.2%}")
    col3.metric("Sharpe Ratio", f"{result['portfolio']['sharpe']:.2f}")

    # ----------------------------
    # Projection Summary
    st.subheader("🔮 Investment Projection")

    proj = result["projection"]

    st.write(f"**Median Value:** ₹{proj['median']:.2f}")
    st.write(f"**Worst 10% Case:** ₹{proj['worst_10']:.2f}")
    st.write(f"**Best 90% Case:** ₹{proj['best_90']:.2f}")
