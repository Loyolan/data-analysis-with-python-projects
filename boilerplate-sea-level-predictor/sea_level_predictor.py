import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_levels_predicted = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_predicted, 'r', label="Best fit over")

    # Create second line of best fit
    df_2000_onwards = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000_onwards['Year'], df_2000_onwards['CSIRO Adjusted Sea Level'])
    years_2000_to_2050 = np.arange(2000, 2051)
    sea_levels_predicted_2000 = intercept_2000 + slope_2000 * years_2000_to_2050
    plt.plot(years_2000_to_2050, sea_levels_predicted_2000, 'g', label='Best fit 2000 onwards')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
