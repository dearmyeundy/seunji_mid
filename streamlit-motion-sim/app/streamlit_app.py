import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from simulations import calculate_uniform_motion, calculate_free_fall
from controls import create_controls

st.set_page_config(layout="wide")
st.title("🚀 Motion Simulation: Uniform Motion & Free Fall 🌌")
st.markdown("---")

# Create input controls for simulation parameters
initial_velocity, acceleration, time_interval = create_controls()

# Time array for simulation
time = np.arange(0, time_interval, 0.1)

# Calculate motion for uniform motion and free fall
uniform_position, uniform_velocity = calculate_uniform_motion(initial_velocity, acceleration, time)
free_fall_position, free_fall_velocity = calculate_free_fall(initial_velocity, time)

# Plotting the results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Velocity-Time Graph
ax1.plot(time, uniform_velocity, label='Uniform Motion Velocity', color='blue')
ax1.plot(time, free_fall_velocity, label='Free Fall Velocity', color='orange')
ax1.set_title('Velocity-Time Graph')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Velocity (m/s)')
ax1.legend()
ax1.grid()

# Position-Time Graph
ax2.plot(time, uniform_position, label='Uniform Motion Position', color='blue')
ax2.plot(time, free_fall_position, label='Free Fall Position', color='orange')
ax2.set_title('Position-Time Graph')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Position (m)')
ax2.legend()
ax2.grid()

# Display the plots in Streamlit
st.pyplot(fig)

st.markdown("---")
st.info("Adjust the parameters above to see how they affect the motion and the graphs!")