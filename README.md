# 📊 Future Portfolio Advisor

Future Portfolio Advisor is an educational web application that demonstrates
portfolio optimization and investment outcome simulation using quantitative finance methods.

This project was built as a learning exercise to understand:
- Risk–return trade-offs
- Portfolio optimization constraints
- Monte Carlo simulation for long-term projections
- End-to-end deployment of a data-driven application

⚠️ **This is a student-built educational project and not financial advice.**

---

## 🚀 Live Demo

🔗 **Streamlit App:**  
https://aiportfolioadvisorgit-4te2j7kzzadmoef3rgknww.streamlit.app/

---

## 🧠 What This App Does

Users can:
- Enter an initial investment amount
- Select an investment horizon (years)
- Choose a risk profile (conservative / moderate / aggressive)
- View:
  - Optimized portfolio allocation
  - Expected return, volatility, and Sharpe ratio
  - Monte Carlo-based future value projections

---

## ⚙️ Methodology

### 📌 Portfolio Optimization
- Uses **Modern Portfolio Theory**
- Optimizes for **maximum Sharpe ratio**
- Enforces realistic weight constraints per asset
- Covariance estimation via historical price data

### 📌 Risk Profiles
Each risk profile defines:
- Minimum and maximum asset weights
- Different risk exposure levels

### 📌 Monte Carlo Simulation
- Simulates thousands of possible future price paths
- Models uncertainty in returns and volatility
- Provides percentile-based outcomes:
  - Median case
  - Worst 10% case
  - Best 90% case

---

## 🧩 Tech Stack

**Backend / Core Logic**
- Python
- NumPy
- Pandas
- PyPortfolioOpt
- Statsmodels (SARIMAX)

**Visualization & UI**
- Streamlit
- Matplotlib

**Deployment**
- GitHub
- Streamlit Cloud

---


---

## 🧪 Disclaimer

This application:
- Is built for educational and academic purposes only
- Does NOT provide investment or financial advice
- Should NOT be used for real-money investment decisions

All outputs are simulations based on historical data and assumptions.

---

## 👩‍💻 Author

**Ashika Singh**  
B.Tech (Electrical Engineering)  
IIT ISM Dhanbad  

Interests:
- Machine Learning
- Quantitative Finance
- Time Series Analysis
- AI-driven Decision Systems

---

⭐ If you find this project interesting, feel free to explore, fork, or build upon it.
