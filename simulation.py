"""
simulation.py
Module for running Monte Carlo portfolio simulations using ML-estimated drift and volatility.
"""
import numpy as np
from ml_model import DriftVolatilityRegressor

class PortfolioSimulator:
    def __init__(self, initial_value=1000, num_paths=200, num_steps=252, seed=42):
        self.initial_value = initial_value
        self.num_paths = num_paths
        self.num_steps = num_steps
        self.seed = seed
        self.simulated_paths = None

    def simulate(self, historical_returns):
        """
        Simulate portfolio paths using ML-estimated drift and volatility.
        Args:
            historical_returns (np.ndarray): Array of historical returns.
        Returns:
            np.ndarray: Simulated portfolio paths (num_paths x num_steps)
        """
        np.random.seed(self.seed)
        ml_model = DriftVolatilityRegressor()
        ml_model.fit(historical_returns)
        drift, vol = ml_model.predict(self.num_steps)
        paths = np.zeros((self.num_paths, self.num_steps))
        paths[:, 0] = self.initial_value
        for t in range(1, self.num_steps):
            random_shock = np.random.normal(0, 1, self.num_paths)
            returns = drift[t] + vol[t] * random_shock
            paths[:, t] = paths[:, t-1] * (1 + returns)
        self.simulated_paths = paths
        return paths
