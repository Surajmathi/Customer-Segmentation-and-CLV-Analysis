"""
Data Preprocessing Module
Customer Segmentation and CLV Analysis

This module contains reusable functions for cleaning and preparing
the Global Superstore dataset before analysis.
"""

import pandas as pd


def load_dataset(file_path):
    """
    Load the Global Superstore dataset.
    """
    df = pd.read_csv(file_path)
    return df


def standardize_column_names(df):
    """
    Convert column names to lowercase and replace spaces with underscores.
    Example:
    'Order Date' -> 'order_date'
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Removed {before - after} duplicate rows.")
    return df


def handle_missing_values(df):
    """
    Display missing values in each column.
    (No values are dropped or filled automatically.)
    """
    print("\nMissing Values:")
    print(df.isnull().sum())

    return df

def convert_date_columns(df):
    """
    Convert Order Date and Ship Date columns to datetime format.
    """
    date_columns = ["order_date", "ship_date"]

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df