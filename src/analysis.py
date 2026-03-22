import pandas as pd


def world_daily_trend(df):

    # Group by Date and sum confirmed cases
    world_daily = df.groupby("Date")["Confirmed"].sum().reset_index()

    return world_daily


def country_wise_total(df):

    # Get maximum confirmed cases per country
    country_total = df.groupby("Country/Region")["Confirmed"].max().reset_index()

    # Sort countries in descending order
    country_total = country_total.sort_values(by="Confirmed", ascending=False)

    return country_total


def growth_rate(df):

    # Calculate global daily confirmed cases
    world_daily = df.groupby("Date")["Confirmed"].sum().reset_index()

    # Calculate percentage growth rate
    world_daily["Growth_Rate"] = world_daily["Confirmed"].pct_change() * 100

    return world_daily


def top_affected_country(country_total):

    # Return the country with highest confirmed cases
    return country_total.iloc[0]


def peak_day(world_daily):

    # Return the day with highest confirmed cases
    return world_daily.sort_values(by="Confirmed", ascending=False).iloc[0]