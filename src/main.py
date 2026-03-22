import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

from data_loader import load_data
from data_cleaning import clean_data
from analysis import world_daily_trend, country_wise_total
from visualization import plot_world_trend, plot_top_countries

df = load_data()
df = clean_data(df)

world_daily = world_daily_trend(df)
country_total = country_wise_total(df)

plot_world_trend(world_daily)
plot_top_countries(country_total)