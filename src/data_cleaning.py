import pandas as pd


def clean_data(df):
    """
    Clean and transform the dataset.

    Steps:
    - Remove unnecessary columns
    - Convert wide format to long format
    - Convert Date column to datetime
    - Remove missing values and duplicates

    Args:
        df (DataFrame): Raw dataset

    Returns:
        df (DataFrame): Cleaned dataset
    """

    # Drop unnecessary columns (if present)
    df = df.drop(columns=["Lat", "Long"], errors="ignore")

    # Convert wide format (multiple date columns) to long format
    df = df.melt(
        id_vars=["Province/State", "Country/Region"],
        var_name="Date",
        value_name="Confirmed"
    )

    # Convert Date column to datetime format
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%y")

    # Remove missing values
    df = df.dropna()

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df