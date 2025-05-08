import os
import glob
import pandas as pd


def season_from_month(month):
    if month in (12, 1, 2):
        return 'Summer'
    elif month in (3, 4, 5):
        return 'Autumn'
    elif month in (6, 7, 8):
        return 'Winter'
    elif month in (9, 10, 11):
        return 'Spring'
    else:
        return None


def main():
    
    data_folder = 'temperatures'
    pattern = os.path.join(data_folder, '*.csv')
    files = glob.glob(pattern)
    if not files:
        print(f"No CSV files found in {data_folder}")
        return

    frames = []
    for filepath in files:
        df = pd.read_csv(filepath)
        
        for col in ('STATION_NAME', 'Temperature'):
            '''if col not in df.columns:
                raise KeyError(f"Required column '{col}' not found in file {filepath}")'''
        
        df['Date'] = pd.to_datetime(df['Date'])
        df['Season'] = df['Date'].dt.month.map(season_from_month)
        frames.append(df[['STATION_NAME', 'Season', 'Temperature']])

   
    data = pd.concat(frames, ignore_index=True)

    
    season_order = ['Summer', 'Autumn', 'Winter', 'Spring']
    season_avg = data.groupby('Season')['Temperature'].mean().reindex(season_order)
    with open('average_temp.txt', 'w') as f:
        f.write("Average Temperature by Season (°C)\n")
        for season, avg in season_avg.items():
            f.write(f"{season}: {avg:.2f}\n")

   
    station_range = data.groupby('Station')['Temperature'].agg(lambda x: x.max() - x.min())
    max_range = station_range.max()
    stations_max_range = station_range[station_range == max_range].index.tolist()
    with open('largest_temp_range_station.txt', 'w') as f:
        f.write(f"Largest Temperature Range: {max_range:.2f}°C\n")
        f.write("Station(s) with largest range:\n")
        for st in stations_max_range:
            f.write(f"- {st}\n")

    
    station_avg = data.groupby('Station')['Temperature'].mean()
    highest_avg = station_avg.max()
    lowest_avg = station_avg.min()
    warmest = station_avg[station_avg == highest_avg].index.tolist()
    coolest = station_avg[station_avg == lowest_avg].index.tolist()
    with open('warmest_and_coolest_station.txt', 'w') as f:
        f.write("Warmest Station(s) by Mean Temperature:\n")
        for st in warmest:
            f.write(f"- {st}: {highest_avg:.2f}°C\n")
        f.write("\nCoolest Station(s) by Mean Temperature:\n")
        for st in coolest:
            f.write(f"- {st}: {lowest_avg:.2f}°C\n")

if __name__ == '__main__':
    main()
