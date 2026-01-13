import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Supply Chain Risk Tower")

# --- SIDEBAR SIMULATION ---
st.sidebar.header("⚠️ Scenario Simulation")
st.sidebar.info("Adjust factors to simulate a global crisis.")

fuel_multiplier = st.sidebar.slider("Fuel Price Surge (%)", 0, 100, 0) / 100
congestion_boost = st.sidebar.slider("Port Congestion Increase (%)", 0, 100, 0) / 100

# --- DATA PROCESSING ---
df_original = pd.read_csv('data/processed/route_risk_scores.csv')
df = df_original.copy()

# Apply "What-If" Logic
# If fuel goes up, fragility increases. If congestion goes up, delay volatility increases.
df['fragility_index'] = df['fragility_index'] * (1 + (fuel_multiplier * 0.5) + (congestion_boost * 0.5))
df['delay_volatility'] = df['delay_volatility'] * (1 + congestion_boost)

# Re-calculate Risk Level based on new scores
df['risk_level'] = pd.cut(df['fragility_index'], bins=[0, 30, 60, 1000], labels=['Stable', 'Volatile', 'Critical'])

# --- DASHBOARD UI ---
st.title("🚢 Supply Chain Control Tower: Crisis Simulator")

m1, m2, m3 = st.columns(3)
m1.metric("Current Fragility Avg", f"{df['fragility_index'].mean():.1f}", 
          delta=f"{df['fragility_index'].mean() - df_original['fragility_index'].mean():.1f}")
m2.metric("Critical Routes", len(df[df['risk_level'] == 'Critical']), 
          delta=len(df[df['risk_level'] == 'Critical']) - len(df_original[df_original['risk_level'] == 'Critical']))
m3.metric("System Stress Level", "HIGH" if fuel_multiplier > 0.5 else "NORMAL")

# Visuals
c1, c2 = st.columns(2)
with c1:
    st.subheader("Simulated Risk Matrix")
    fig = px.scatter(df, x="avg_delay", y="delay_volatility", size="fragility_index", color="risk_level",
                     color_discrete_map={'Stable': 'green', 'Volatile': 'orange', 'Critical': 'red'})
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Route Fragility Ranking")
    st.dataframe(df[['origin', 'destination', 'fragility_index', 'risk_level']].sort_values('fragility_index', ascending=False))