import pandas as pd
import numpy as np


data = pd.read_csv('CSV_FILES/temperature_data.csv')

mean_temperatures = data.groupby('city')['temperature'].mean()

std_deviation_temperatures = data.groupby('city')['temperature'].std()

temperature_ranges = data.groupby(
    'city')['temperature'].apply(lambda x: max(x) - min(x))
city_with_highest_range = temperature_ranges.idxmax()

city_with_lowest_std_deviation = std_deviation_temperatures.idxmin()

print("Mean Temperatures:")
print(mean_temperatures)

print("\nStandard Deviations of Temperatures:")
print(std_deviation_temperatures)

print(f"\nCity with the Highest Temperature Range: {city_with_highest_range}")
print(
    f"City with the Most Consistent Temperature: {city_with_lowest_std_deviation}")
