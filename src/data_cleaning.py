import pandas as pd

def clean_data(df):
    df = df.drop(columns=["Lat", "Long"], errors="ignore")

    df = df.melt(
        id_vars=["Province/State", "Country/Region"],
        var_name="Date",
        value_name="Confirmed"
    )

    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%y")

    df = df.dropna()
    df = df.drop_duplicates()

    return df