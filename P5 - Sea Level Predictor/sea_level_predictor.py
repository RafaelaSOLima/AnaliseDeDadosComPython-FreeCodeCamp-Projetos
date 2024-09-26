import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    # Read data from file
    df = pd.read_csv("P5 - Sea Level Predictor/epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent
    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (From 2000)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig(os.path.join('P5 - Sea Level Predictor','sea_level_plot.png'))
    return plt.gca()

    