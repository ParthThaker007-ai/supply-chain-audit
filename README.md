# 🚢 Global Supply Chain Fragility Audit & Crisis Simulator

**An Enterprise-Grade Decision Support System (DSS) for identifying and stress-testing global trade route vulnerabilities.**

![Dashboard Preview](map_preview.png) *(Note: Replace this with a screenshot of your Streamlit app)*

## 🎯 Business Case
Global supply chains are increasingly volatile. This project provides a "Control Tower" view of shipping data, allowing logistics managers to:
1. **Identify "Fragile" Routes:** Using a custom-weighted index of latency and volatility.
2. **Stress-Test Scenarios:** Simulate how a 50% fuel spike or port strikes impact global delivery stability.
3. **Data-Driven Mitigation:** Pivot from reactive to proactive risk management.

## 🛠️ Tech Stack
- **Engine:** Python 3.10 (Pandas, NumPy, Scikit-Learn)
- **Simulation:** Synthetic Data Engine (100,000+ records)
- **UI/UX:** Streamlit & Plotly (Interactive Web Dashboard)
- **Version Control:** Git/GitHub (Professional Pipeline)

## 🧠 The Fragility Index Logic
Unlike standard delay tracking, this project uses a **Composite Risk Score**:
- **Volatility (40%):** Standard deviation of delays (Unpredictability is higher risk than constant delays).
- **Latency (30%):** Average days beyond the planned schedule.
- **Fuel Sensitivity (30%):** Impact of price fluctuations on specific long-haul routes.

## 🚀 Installation & Usage
1. **Clone & Setup:**
   ```bash
   git clone [https://github.com/ParthThaker007-ai/supply-chain-audit.git](https://github.com/ParthThaker007-ai/supply-chain-audit.git)
   cd supply-chain-audit
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   pip install -r requirements.txt