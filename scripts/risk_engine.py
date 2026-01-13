import pandas as pd
import numpy as np
import os

def calculate_fragility_metrics():
    # 1. Load Data
    df = pd.read_csv('data/raw/shipping_data.csv')

    # 2. Calculate KPIs
    # Delay: Actual vs Planned
    df['delay_days'] = df['actual_duration'] - df['planned_duration']
    
    # 3. Aggregate by Route (The "Fragility" Logic)
    route_stats = df.groupby(['origin', 'destination']).agg({
        'delay_days': ['mean', 'std', 'max'], # std = Volatility
        'vessel_load_factor': 'mean',
        'fuel_cost_index': 'mean'
    }).reset_index()

    # Flatten the multi-index columns
    route_stats.columns = ['origin', 'destination', 'avg_delay', 'delay_volatility', 'max_delay', 'avg_load', 'avg_fuel_price']

    # 4. THE FRAGILITY SCORE FORMULA
    # We weight Volatility (40%), Avg Delay (30%), and Fuel Sensitivity (30%)
    # Normalize values between 0 and 1 first
    def normalize(col):
        return (col - col.min()) / (col.max() - col.min())

    score = (
        normalize(route_stats['delay_volatility']) * 0.4 +
        normalize(route_stats['avg_delay']) * 0.3 +
        normalize(route_stats['avg_fuel_price']) * 0.3
    )
    
    route_stats['fragility_index'] = score * 100 # Scale to 0-100
    
    # 5. Categorize Risk
    route_stats['risk_level'] = pd.cut(route_stats['fragility_index'], 
                                       bins=[0, 30, 60, 100], 
                                       labels=['Stable', 'Volatile', 'Critical'])

    os.makedirs('data/processed', exist_ok=True)
    route_stats.to_csv('data/processed/route_risk_scores.csv', index=False)
    print("Fragility Index Calculation Complete.")

if __name__ == "__main__":
    calculate_fragility_metrics()