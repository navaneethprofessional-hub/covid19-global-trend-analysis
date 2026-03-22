import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)


def plot_world_trend(world_daily):

    # Line chart for global trend
    plt.figure(figsize=(10, 5))
    plt.plot(world_daily["Date"], world_daily["Confirmed"])

    plt.title("Global COVID-19 Trend")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("outputs/world_trend.png")
    plt.show()


def plot_top_countries(country_total):

    # Bar chart for top 10 countries
    top10 = country_total.head(10)

    plt.figure(figsize=(10, 5))
    plt.bar(top10["Country/Region"], top10["Confirmed"])

    plt.title("Top 10 Countries by Confirmed Cases")
    plt.xlabel("Country")
    plt.ylabel("Confirmed Cases")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("outputs/top_countries.png")
    plt.show()


def plot_growth_rate(growth_df):

    # Line chart for growth rate
    plt.figure(figsize=(10, 5))
    plt.plot(growth_df["Date"], growth_df["Growth_Rate"])

    plt.title("COVID-19 Growth Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Growth Rate (%)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("outputs/growth_rate.png")
    plt.show()


def plot_distribution(country_total):

    # Histogram for distribution of cases
    plt.figure(figsize=(10, 5))
    plt.hist(country_total["Confirmed"], bins=30)

    plt.title("Distribution of Confirmed Cases Across Countries")
    plt.xlabel("Confirmed Cases")
    plt.ylabel("Number of Countries")

    plt.tight_layout()

    plt.savefig("outputs/distribution.png")
    plt.show()


def plot_scatter(country_total):

    # Scatter plot for top 10 countries
    top10 = country_total.head(10)

    plt.figure(figsize=(8, 5))
    plt.scatter(top10["Country/Region"], top10["Confirmed"])

    plt.title("Top 10 Countries - Scatter Plot")
    plt.xlabel("Country")
    plt.ylabel("Confirmed Cases")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("outputs/scatter.png")
    plt.show()