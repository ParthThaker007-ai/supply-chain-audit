import pandas as pd
import numpy as np
import os

def generate_supply_chain_data(records=100000):
    np.random.seed(42)
    
    # Major Global Ports
    ports = ['Shanghai', 'Singapore', 'Rotterdam', 'Los Angeles', 'Hamburg', 'Dubai', 'Mumbai', 'Savannah']
    vessel_types = ['Container', 'Bulk Carrier', 'Oil Tanker']
    
    routes = []
    
    print(f"Generating {records} simulated shipping records...")
    
    for _ in range(records):
        origin = np.random.choice(ports)
        destination = np.random.choice([p for p in ports if p != origin])
        
        # Logic: Long distance routes have higher base travel times
        base_travel_time = np.random.randint(15, 45) 
        
        # Logic: Congestion follows an Exponential distribution (most are 0-2 days, some are 10+)
        port_congestion_delay = np.random.exponential(scale=1.5) 
        
        # Logic: Weather impact occurs in 15% of journeys
        weather_impact = np.random.choice([0, 3, 7, 12], p=[0.85, 0.10, 0.04, 0.01])
        
        total_time = base_travel_time + port_congestion_delay + weather_impact
        
        routes.append({
            'origin': origin,
            'destination': destination,
            'vessel_type': np.random.choice(vessel_types),
            'planned_duration': base_travel_time,
            'actual_duration': round(total_time, 2),
            'fuel_cost_index': round(np.random.uniform(1.2, 2.8), 2),
            'vessel_load_factor': round(np.random.uniform(0.5, 1.0), 2)
        })
    
    df = pd.DataFrame(routes)
    
    # Ensure the directory exists
    os.makedirs('data/raw', exist_ok=True)
    
    # Save the file
    output_path = 'data/raw/shipping_data.csv'
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Data saved to {output_path}")

if __name__ == "__main__":
    generate_supply_chain_data()