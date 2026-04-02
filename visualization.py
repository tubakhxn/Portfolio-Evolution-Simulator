def plot_3d_animated_scatter(num_points=200, num_frames=100):
    """
    Animated 3D scatter plot with colorful moving points inside a cube.
    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import animation
    import numpy as np

    # Generate initial random positions and colors
    np.random.seed(0)
    pos = np.random.rand(num_points, 3) * 10
    colors = plt.cm.rainbow(np.linspace(0, 1, num_points))

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    ax.set_title(' Portfolio Evolution Simulator ', color='#39ff14', fontsize=16)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')

    scat = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors, s=40, alpha=0.8)

    def update(frame):
        # Move points in a random walk
        step = np.random.randn(num_points, 3) * 0.2
        new_pos = pos + frame * step / num_frames
        scat._offsets3d = (new_pos[:, 0], new_pos[:, 1], new_pos[:, 2])
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)
    plt.show()
"""
visualization.py
Module for all visualizations: 3D animated plot, histogram, average line, rolling volatility.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Dark theme and neon style
plt.style.use('dark_background')

# Neon color palette
def neon_color(profit):
    return '#39ff14' if profit else '#ff073a'

def plot_3d_animated(paths=None, interval=40, dummy_mode=False):
    # If paths is None or dummy_mode is True, generate dummy data
    if paths is None or dummy_mode:
        num_paths, num_steps = 5, 100
        np.random.seed(0)
        # Create dummy data: 5 paths, each with 100 steps
        paths = np.cumprod(1 + 0.001 + 0.01 * np.random.randn(num_paths, num_steps), axis=1) * 1000
    else:
        num_paths, num_steps = paths.shape

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Time')
    ax.set_ylabel('Simulation')
    ax.set_zlabel('Portfolio Value')
    ax.set_title('3D Animated Portfolio Evolution', color='#39ff14', fontsize=16)

    # Animate one line per path
    lines = []
    for i in range(num_paths):
        color = neon_color(paths[i, -1] > paths[i, 0])
        l, = ax.plot([], [], [], color=color, alpha=0.8, linewidth=2)
        lines.append(l)

    def init():
        for l in lines:
            l.set_data([], [])
            l.set_3d_properties([])
        return lines

    def animate(frame):
        for i, l in enumerate(lines):
            l.set_data(np.arange(frame), np.full(frame, i))
            l.set_3d_properties(paths[i, :frame])
        return lines

    ani = animation.FuncAnimation(fig, animate, frames=num_steps, init_func=init,
                                  interval=interval, blit=True, repeat=False)

    # --- Always show a static plot of the data for debugging ---
    for i in range(num_paths):
        color = neon_color(paths[i, -1] > paths[i, 0])
        ax.plot(np.arange(num_steps), np.full(num_steps, i), paths[i],
                color=color, alpha=0.8, linewidth=2)

    plt.show()

def plot_histogram(paths):
    final_returns = (paths[:, -1] - paths[:, 0]) / paths[:, 0]
    plt.figure(figsize=(10, 5))
    plt.hist(final_returns, bins=30, color='#39ff14', alpha=0.8, edgecolor='#ff073a')
    plt.title('Histogram of Final Portfolio Returns', color='#39ff14')
    plt.xlabel('Return')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.show()

def plot_average_line(paths):
    avg = np.mean(paths, axis=0)
    plt.figure(figsize=(10, 5))
    for glow in range(6, 0, -1):
        plt.plot(avg, color='#39ff14', alpha=0.08 + 0.12 * (glow == 1), linewidth=2 + glow*2)
    plt.title('Average Portfolio Value Over Time', color='#39ff14')
    plt.xlabel('Time')
    plt.ylabel('Average Value')
    plt.grid(False)
    plt.show()

def plot_rolling_volatility(paths, window=20):
    returns = (paths[:, 1:] - paths[:, :-1]) / paths[:, :-1]
    rolling_vol = np.std(returns, axis=0)
    rolling_vol = np.convolve(rolling_vol, np.ones(window)/window, mode='valid')
    plt.figure(figsize=(10, 5))
    for glow in range(6, 0, -1):
        plt.plot(rolling_vol, color='#ff073a', alpha=0.08 + 0.12 * (glow == 1), linewidth=2 + glow*2)
    plt.title('Rolling Volatility (Neon Red)', color='#ff073a')
    plt.xlabel('Time')
    plt.ylabel('Volatility')
    plt.grid(False)
    plt.show()
