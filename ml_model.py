"""
ml_model.py
Module for machine learning model to estimate drift and volatility dynamically.
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

class DriftVolatilityRegressor:
    """
    Regression model to estimate drift and volatility from historical returns.
    """
    def __init__(self, window=30):
        self.window = window
        self.drift_model = LinearRegression()
        self.vol_model = LinearRegression()
        self.scaler = StandardScaler()

    def fit(self, returns):
        """
        Fit regression models to estimate drift and volatility.
        Args:
            returns (np.ndarray): Array of historical returns.
        """
        X = np.arange(len(returns)).reshape(-1, 1)
        y_drift = returns
        y_vol = np.abs(returns - np.mean(returns))
        X_scaled = self.scaler.fit_transform(X)
        self.drift_model.fit(X_scaled, y_drift)
        self.vol_model.fit(X_scaled, y_vol)

    def predict(self, steps):
        """
        Predict drift and volatility for future steps.
        Args:
            steps (int): Number of future steps to predict.
        Returns:
            tuple: (drift, volatility) arrays for each step
        """
        X_future = np.arange(steps).reshape(-1, 1)
        X_scaled = self.scaler.transform(X_future)
        drift = self.drift_model.predict(X_scaled)
        vol = np.abs(self.vol_model.predict(X_scaled))
        return drift, vol
