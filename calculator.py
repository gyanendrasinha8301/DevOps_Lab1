def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def divide(a, b):
    """Returns a divided by b. Raises a ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b