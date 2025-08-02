def add(*args):
    """Returns the sum of x and y."""
    sum = 0
    for arg in args:
        sum += arg
    return sum


def subtract(*args):
    """Returns the difference of the given numbers"""
    subtract = None
    for arg in args:
        if subtract == None:
            subtract = arg
        else:
            subtract -=arg
    return subtract


def multiply(*args):
    multiply = 1
    for arg in args:
        multiply *= arg
    return multiply

def divide(*args):
    """Return the division of given numbers"""
    divide = None
    for arg in args:
        if divide == None:
            divide = arg
        else:
            divide /= arg
    return divide


