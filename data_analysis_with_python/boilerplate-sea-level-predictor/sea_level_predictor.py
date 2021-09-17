import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    year_arr = pd.Series(range(1880, 2051))
    plt.plot(year_arr, res.intercept + res.slope * year_arr, "r")

    # Create second line of best fit
    res = linregress(
        df[(df["Year"] >= 2000)]["Year"],
        df[(df["Year"] >= 2000)]["CSIRO Adjusted Sea Level"],
    )
    year_arr = pd.Series(range(2000, 2051))
    plt.plot(year_arr, res.intercept + res.slope * year_arr, "g")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.xticks(
        ticks=[
            1850.0,
            1875.0,
            1900.0,
            1925.0,
            1950.0,
            1975.0,
            2000.0,
            2025.0,
            2050.0,
            2075.0,
        ]
    )

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()

