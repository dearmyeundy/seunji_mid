import pytest
from app.simulations import calculate_uniform_motion, calculate_free_fall

def test_calculate_uniform_motion():
    # Test for uniform motion with constant velocity
    initial_velocity = 10  # m/s
    acceleration = 0       # m/s^2
    time = 5               # seconds
    expected_position = initial_velocity * time
    expected_velocity = initial_velocity

    position, velocity = calculate_uniform_motion(initial_velocity, acceleration, time)

    assert position == expected_position, f"Expected position: {expected_position}, but got: {position}"
    assert velocity == expected_velocity, f"Expected velocity: {expected_velocity}, but got: {velocity}"

def test_calculate_free_fall():
    # Test for free fall motion under gravity
    initial_velocity = 0   # m/s
    acceleration = 9.81    # m/s^2 (gravity)
    time = 3               # seconds
    expected_position = (initial_velocity * time) + (0.5 * acceleration * time**2)
    expected_velocity = initial_velocity + (acceleration * time)

    position, velocity = calculate_free_fall(initial_velocity, acceleration, time)

    assert position == expected_position, f"Expected position: {expected_position}, but got: {position}"
    assert velocity == expected_velocity, f"Expected velocity: {expected_velocity}, but got: {velocity}"