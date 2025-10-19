import streamlit as st

def motion_controls():
    st.sidebar.header("Motion Parameters")

    initial_velocity = st.sidebar.number_input("Initial Velocity (m/s)", value=0.0, step=0.1)
    acceleration = st.sidebar.number_input("Acceleration (m/s²)", value=0.0, step=0.1)
    time_interval = st.sidebar.number_input("Time Interval (s)", value=1.0, step=0.1)

    return initial_velocity, acceleration, time_interval

def free_fall_controls():
    st.sidebar.header("Free Fall Parameters")

    initial_height = st.sidebar.number_input("Initial Height (m)", value=0.0, step=0.1)
    time_interval = st.sidebar.number_input("Time Interval (s)", value=1.0, step=0.1)

    return initial_height, time_interval

def display_controls():
    motion_type = st.sidebar.selectbox("Select Motion Type", ["Uniform Motion", "Free Fall"])

    if motion_type == "Uniform Motion":
        return motion_controls()
    else:
        return free_fall_controls()