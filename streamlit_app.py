
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

from pipeline.run_advisor import run_advisor

# --------------------------------------------------
# Page Config (ONLY ONCE, TOP OF FILE)
st.set_page_config(
    page_title="Future Portfolio Advisor",
    page_icon="📈",
    layout="centered"
)

# --------------------------------------------------
# Header
st.title("📊 Future Portfolio Advisor")

st.markdown(
    """
    **Developed by:** Ashika Singh  
    _B.Tech (Electrical Engineering), IIT ISM Dhanbad_
    """
)

st.info(
    """
    📌 **Educational Disclaimer**

    This application is a **student-built educational project** designed to demonstrate
    portfolio optimization and investment simulation concepts.

    - Not financial advice  
    - Not intended for real-money investment decisions  
    - Built for learning, experimentation, and academic demonstration
    """
)

st.markdown("---")

# --------------------------------------------------
# User Inputs
capital = st.number_input(
    "Initial Investment (₹)",
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

# --------------------------------------------------
# Run Advisor
if st.button("Optimize Portfolio"):
    with st.spinner("Optimizing portfolio..."):
        result = run_advisor(
            capital=capital,
            years=years,
            risk_profile=risk_profile
        )

    st.success("Optimization Complete")

    # --------------------------------------------------
    # Portfolio Weights
    st.subheader("📌 Portfolio Allocation")

    weights_df = pd.DataFrame.from_dict(
        result["portfolio"]["weights"],
        orient="index",
        columns=["Weight"]
    )

    st.bar_chart(weights_df)

    # --------------------------------------------------
    # Metrics
    st.subheader("📈 Portfolio Metrics")

    col1, col2, col3 = st.columns(3)
    col1.metric("Expected Return", f"{result['portfolio']['expected_return']:.2%}")
    col2.metric("Volatility", f"{result['portfolio']['volatility']:.2%}")
    col3.metric("Sharpe Ratio", f"{result['portfolio']['sharpe']:.2f}")

    # --------------------------------------------------
    # Projection Summary
    st.subheader("🔮 Investment Projection")

    proj = result["projection"]

    st.write(f"**Median Value:** ₹{proj['median']:.2f}")
    st.write(f"**Worst 10% Case:** ₹{proj['worst_10']:.2f}")
    st.write(f"**Best 90% Case:** ₹{proj['best_90']:.2f}")

# --------------------------------------------------
# Footer
st.markdown("---")

st.markdown(
    """
    👩‍💻 **About the Project**

    This tool applies portfolio optimization techniques and Monte Carlo simulation
    to visualize long-term investment outcomes under different risk profiles.

    Built as part of a learning project in quantitative finance and machine learning.
    """
)
