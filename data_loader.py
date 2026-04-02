"""
data_loader.py
Module for loading or generating sample portfolio data.
"""
import numpy as np
import pandas as pd

def generate_sample_data(num_points=252, seed=42):
    """
    Generate synthetic historical returns for a portfolio.
    Args:
        num_points (int): Number of time points (e.g., trading days).
        seed (int): Random seed for reproducibility.
    Returns:
        pd.DataFrame: DataFrame with columns ['date', 'return']
    """
    np.random.seed(seed)
    # Simulate daily returns with some drift and volatility
    drift = 0.0005
    volatility = 0.01
    returns = np.random.normal(drift, volatility, num_points)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=num_points)
    return pd.DataFrame({'date': dates, 'return': returns})
