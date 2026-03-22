import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns in output
pd.set_option('display.max_columns', None)

# Import custom modules
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

# Step 1: Load dataset
df = load_data()

# Step 2: Clean and transform data (wide → long format)
df = clean_data(df)

# Step 3: Perform analysis
world_daily = world_daily_trend(df)
country_total = country_wise_total(df)

# Step 4: Calculate growth rate
world_daily = growth_rate(world_daily)

# Step 5: Extract key insights
top_country = top_affected_country(country_total)
peak = peak_day(world_daily)

# Step 6: Display results in readable format
print("\nTop Affected Country:")
print("---------------------------------")
print(f"Country : {top_country['Country/Region']}")
print(f"Cases   : {int(top_country['Confirmed'])}")

print("\nPeak Day (Highest Global Cases):")
print("---------------------------------")
print(f"Date  : {peak['Date'].date()}")
print(f"Cases : {int(peak['Confirmed'])}")

print("\nRecent Growth Rate (Last 5 Days):")
print("---------------------------------")
print(world_daily.tail(5).to_string(index=False))

# Step 7: Generate and save visualizations
plot_world_trend(world_daily)
plot_top_countries(country_total)
plot_growth_rate(world_daily)
plot_distribution(country_total)
plot_scatter(country_total)