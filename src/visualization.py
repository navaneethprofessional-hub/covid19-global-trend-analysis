import matplotlib.pyplot as plt

def plot_world_trend(world_daily):
    plt.figure(figsize=(10, 5))
    plt.plot(world_daily["Date"], world_daily["Confirmed"])
    plt.title("Global COVID-19 Trend")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_top_countries(country_total):
    top10 = country_total.head(10)

    plt.figure(figsize=(10, 5))
    plt.bar(top10["Country/Region"], top10["Confirmed"])
    plt.title("Top 10 Countries by Confirmed Cases")
    plt.xlabel("Country")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()