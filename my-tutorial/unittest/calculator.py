def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return round(x * y, 2)

def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return x / y

