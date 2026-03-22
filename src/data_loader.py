import pandas as pd

def load_data():
    file_path = "data/Covid-19_Dataset.csv"
    
    df = pd.read_csv(file_path)
    
    print("Dataset loaded successfully ")
    print("\nFirst 5 rows:\n")
    print(df.head())
    
    return df