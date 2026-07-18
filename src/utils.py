"""
Utility Functions
Customer Segmentation and CLV Analysis
"""

import pandas as pd


def load_data(file_path):
    """
    Load a CSV file and return a pandas DataFrame.
    """
    return pd.read_csv(file_path)


def save_data(df, file_path):
    """
    Save a DataFrame to a CSV file.
    """
    df.to_csv(file_path, index=False)


def dataset_summary(df):
    """
    Display basic information about the dataset.
    """
    print("=" * 50)
    print("Dataset Shape:", df.shape)
    print("=" * 50)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())