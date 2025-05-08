import os
import pandas as pd

#all csv files need to be saves in a folder named temperatures. 
TEMPERATURE_FOLDER = 'temperatures'

#Grouping months based on seasons
SEASON_MAP = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

def load_all_temperature_data(folder):
    data_frames = []
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder, filename))
            df['Year'] = filename[-8:-4]  # Extracting year from filename
            data_frames.append(df)
    return pd.concat(data_frames, ignore_index=True)

#task1-Calculation average temperature and saving it in average_temp.txt
def calculate_seasonal_averages(df):
    seasonal_avgs = []
    for season, months in SEASON_MAP.items():
        df[season] = df[months].mean(axis=1)
    season_means = df.groupby('Year')[[*SEASON_MAP]].mean().mean()
    season_means.round(2).to_csv('average_temp.txt', header=True)
#task 2-  Finding the station/stations have the largest temperature range and saving it in largest_temp_range_station.txt. 
def find_largest_temperature_range(df):
    df['MaxTemp'] = df[[*SEASON_MAP['Summer'], *SEASON_MAP['Autumn'], 
                        *SEASON_MAP['Winter'], *SEASON_MAP['Spring']]].max(axis=1)
    df['MinTemp'] = df[[*SEASON_MAP['Summer'], *SEASON_MAP['Autumn'], 
                        *SEASON_MAP['Winter'], *SEASON_MAP['Spring']]].min(axis=1)
    df['TempRange'] = df['MaxTemp'] - df['MinTemp']
    max_range = df['TempRange'].max()
    result = df[df['TempRange'] == max_range][['STATION_NAME', 'TempRange']]
    result.to_csv('largest_temp_range_station.txt', index=False)

#Task 3- Finding the warmest and coolest station/stations and saving the result in warmest_and_coolest_station.txt.
def find_warmest_and_coolest_stations(df):
    month_cols = list(SEASON_MAP['Summer'] + SEASON_MAP['Autumn'] +
                      SEASON_MAP['Winter'] + SEASON_MAP['Spring'])
    df['AvgAnnualTemp'] = df[month_cols].mean(axis=1)
    max_temp = df['AvgAnnualTemp'].max()
    min_temp = df['AvgAnnualTemp'].min()
    warmest = df[df['AvgAnnualTemp'] == max_temp][['STATION_NAME', 'AvgAnnualTemp']]
    coolest = df[df['AvgAnnualTemp'] == min_temp][['STATION_NAME', 'AvgAnnualTemp']]
    with open('warmest_and_coolest_station.txt', 'w') as f:
        f.write("Warmest Station(s):\n")
        f.write(warmest.to_string(index=False))
        f.write("\n\nCoolest Station(s):\n")
        f.write(coolest.to_string(index=False))

def main():
    df = load_all_temperature_data(TEMPERATURE_FOLDER)
    calculate_seasonal_averages(df.copy())
    find_largest_temperature_range(df.copy())
    find_warmest_and_coolest_stations(df.copy())

#This file needs to saved on the same folder where folder named 'temperatures' is kept
if __name__ == '__main__':
    main()