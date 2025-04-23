import os
import pandas as pd
from datetime import datetime

def get_season(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    month = date.month
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"

def analyze_temperatures(folder_path):
    all_data = []

    # Read all CSV files
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder_path, file))
            if not {'station_id', 'date', 'temperature'}.issubset(df.columns):
                continue
            df['season'] = df['date'].apply(get_season)
            all_data.append(df)

    if not all_data:
        print("No valid temperature data found.")
        return

    full_df = pd.concat(all_data)

    # Average temperature per season
    season_avg = full_df.groupby('season')['temperature'].mean()
    with open("average_temp.txt", "w") as f:
        f.write("Average Temperature by Season (°C):\n")
        for season, avg in season_avg.items():
            f.write(f"{season}: {avg:.2f}\n")

    # Temperature range per station
    station_range = full_df.groupby('station_id')['temperature'].agg(['min', 'max'])
    station_range['range'] = station_range['max'] - station_range['min']
    max_range = station_range['range'].max()
    largest_range_stations = station_range[station_range['range'] == max_range]

    with open("largest_temp_range_station.txt", "w") as f:
        f.write("Stations with the Largest Temperature Range:\n")
        f.write(largest_range_stations.to_string())

    # Warmest and coolest stations (by average temp)
    station_avg = full_df.groupby('station_id')['temperature'].mean()
    max_avg = station_avg.max()
    min_avg = station_avg.min()
    warmest = station_avg[station_avg == max_avg]
    coolest = station_avg[station_avg == min_avg]

    with open("warmest_and_coolest_station.txt", "w") as f:
        f.write("Warmest Station(s):\n")
        f.write(warmest.to_string())
        f.write("\n\nCoolest Station(s):\n")
        f.write(coolest.to_string())

# Replace with your actual folder path
analyze_temperatures(r'C:\Users\Lenovo\Desktop\HIT137 Assignment 2 S1 2025\temperatures')