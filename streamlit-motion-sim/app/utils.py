def validate_positive(value):
    if value < 0:
        raise ValueError("Value must be positive.")
    return value

def format_time(seconds):
    return f"{seconds:.2f} seconds"

def format_velocity(velocity):
    return f"{velocity:.2f} m/s"

def format_position(position):
    return f"{position:.2f} meters"