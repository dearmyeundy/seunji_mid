import numpy as np

def uniform_motion(initial_velocity, acceleration, time):
    """
    Calculate position and velocity for uniform motion.
    
    Parameters:
    - initial_velocity: Initial velocity (m/s)
    - acceleration: Acceleration (m/s^2)
    - time: Time (s)
    
    Returns:
    - position: Position at time t (m)
    - velocity: Velocity at time t (m/s)
    """
    position = initial_velocity * time + 0.5 * acceleration * time**2
    velocity = initial_velocity + acceleration * time
    return position, velocity

def free_fall(initial_velocity, time, g=9.81):
    """
    Calculate position and velocity for free fall motion.
    
    Parameters:
    - initial_velocity: Initial velocity (m/s)
    - time: Time (s)
    - g: Acceleration due to gravity (m/s^2), default is 9.81 m/s^2
    
    Returns:
    - position: Position at time t (m)
    - velocity: Velocity at time t (m/s)
    """
    position = initial_velocity * time - 0.5 * g * time**2
    velocity = initial_velocity - g * time
    return position, velocity

def simulate_motion(initial_velocity, acceleration, time_intervals):
    """
    Simulate motion for both uniform motion and free fall.
    
    Parameters:
    - initial_velocity: Initial velocity (m/s)
    - acceleration: Acceleration (m/s^2)
    - time_intervals: List of time intervals (s)
    
    Returns:
    - uniform_positions: Positions for uniform motion at each time interval
    - uniform_velocities: Velocities for uniform motion at each time interval
    - free_fall_positions: Positions for free fall at each time interval
    - free_fall_velocities: Velocities for free fall at each time interval
    """
    uniform_positions = []
    uniform_velocities = []
    free_fall_positions = []
    free_fall_velocities = []

    for t in time_intervals:
        pos_uniform, vel_uniform = uniform_motion(initial_velocity, acceleration, t)
        pos_free_fall, vel_free_fall = free_fall(initial_velocity, t)

        uniform_positions.append(pos_uniform)
        uniform_velocities.append(vel_uniform)
        free_fall_positions.append(pos_free_fall)
        free_fall_velocities.append(vel_free_fall)

    return uniform_positions, uniform_velocities, free_fall_positions, free_fall_velocities