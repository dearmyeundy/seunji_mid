import pytest
import numpy as np
import matplotlib.pyplot as plt
from app.plot import plot_velocity_time, plot_position_time

def test_plot_velocity_time():
    # Test data
    time = np.linspace(0, 10, 100)
    velocity = 5 * time  # Assuming constant acceleration of 5 m/s^2

    # Create the plot
    fig, ax = plt.subplots()
    plot_velocity_time(ax, time, velocity)

    # Check if the plot has the correct title and labels
    assert ax.get_title() == "Velocity vs Time"
    assert ax.get_xlabel() == "Time (s)"
    assert ax.get_ylabel() == "Velocity (m/s)"

    # Check if the plot contains the expected data
    lines = ax.get_lines()
    assert len(lines) == 1
    assert np.allclose(lines[0].get_xdata(), time)
    assert np.allclose(lines[0].get_ydata(), velocity)

def test_plot_position_time():
    # Test data
    time = np.linspace(0, 10, 100)
    position = 0.5 * 5 * time**2  # Assuming initial position is 0 and constant acceleration of 5 m/s^2

    # Create the plot
    fig, ax = plt.subplots()
    plot_position_time(ax, time, position)

    # Check if the plot has the correct title and labels
    assert ax.get_title() == "Position vs Time"
    assert ax.get_xlabel() == "Time (s)"
    assert ax.get_ylabel() == "Position (m)"

    # Check if the plot contains the expected data
    lines = ax.get_lines()
    assert len(lines) == 1
    assert np.allclose(lines[0].get_xdata(), time)
    assert np.allclose(lines[0].get_ydata(), position)