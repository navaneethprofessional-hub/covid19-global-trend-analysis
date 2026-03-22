import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

from data_loader import load_data
from data_cleaning import clean_data
from analysis import (
    world_daily_trend,
    country_wise_total,
    growth_rate,
    top_affected_country,
    peak_day
)
from visualization import (
    plot_world_trend,
    plot_top_countries,
    plot_growth_rate,
    plot_distribution,
    plot_scatter
)

# Load and clean data
df = load_data()
df = clean_data(df)

# Perform analysis
world_daily = world_daily_trend(df)
country_total = country_wise_total(df)
growth_df = growth_rate(df)

top_country = top_affected_country(country_total)
peak = peak_day(world_daily)

# Generate visualizations
plot_world_trend(world_daily)
plot_top_countries(country_total)
plot_growth_rate(growth_df)
plot_distribution(country_total)
plot_scatter(country_total)

# Print key insights
print("\nTop Affected Country:")
print(top_country["Country/Region"], "-", top_country["Confirmed"])

print("\nPeak Day:")
print(peak["Date"], "-", peak["Confirmed"])

print("\nRecent Growth Rate:")
print(growth_df.tail())