import pandas as pd

def world_daily_trend(df):
    world_daily = df.groupby("Date")["Confirmed"].sum().reset_index()
    return world_daily

def country_wise_total(df):
    country_total = df.groupby("Country/Region")["Confirmed"].max().reset_index()
    country_total = country_total.sort_values(by="Confirmed", ascending=False)
    return country_total