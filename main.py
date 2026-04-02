"""
main.py
Entry point for the Portfolio Evolution Simulator.
"""
from data_loader import generate_sample_data
from simulation import PortfolioSimulator
from visualization import (
    plot_3d_animated, plot_histogram, plot_average_line, plot_rolling_volatility
)
import numpy as np

if __name__ == "__main__":
    # Show a cool animated 3D scatter plot like your reference!
    from visualization import plot_3d_animated_scatter
    plot_3d_animated_scatter(num_points=300, num_frames=120)
