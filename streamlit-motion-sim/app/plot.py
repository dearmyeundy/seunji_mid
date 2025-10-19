import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_motion_graphs(time, velocity, position):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Velocity-Time graph
    ax1.plot(time, velocity, label='Velocity (m/s)', color='blue')
    ax1.set_title('Velocity-Time Graph')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Velocity (m/s)')
    ax1.grid()
    ax1.legend()

    # Position-Time graph
    ax2.plot(time, position, label='Position (m)', color='orange')
    ax2.set_title('Position-Time Graph')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Position (m)')
    ax2.grid()
    ax2.legend()

    plt.tight_layout()
    return fig

def update_graphs(initial_velocity, acceleration, time_duration, time_step):
    time = np.arange(0, time_duration, time_step)
    velocity = initial_velocity + acceleration * time
    position = initial_velocity * time + 0.5 * acceleration * time**2

    return time, velocity, position

def display_motion_graphs(initial_velocity, acceleration, time_duration, time_step):
    time, velocity, position = update_graphs(initial_velocity, acceleration, time_duration, time_step)
    fig = plot_motion_graphs(time, velocity, position)
    st.pyplot(fig)