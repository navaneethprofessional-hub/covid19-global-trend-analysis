import pandas as pd


def load_data():
    """
    Load the COVID-19 dataset from the data folder.

    Returns:
        df (DataFrame): Raw dataset
    """
    
    # File path (relative path for portability)
    file_path = "data/Covid-19_Dataset.csv"
    
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path)
    
    # Display basic confirmation
    print("Dataset loaded successfully")
    print("\nFirst 5 rows:\n")
    print(df.head())
    
    return df