import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw data.
    """
    df = df.copy()

    df.drop(columns=["Id"], inplace=True)
    
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    df[categorical_cols] = df[categorical_cols].fillna("Unknown")

    return df
