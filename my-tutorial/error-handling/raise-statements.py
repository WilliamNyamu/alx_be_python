# We can use the raise statement to explicitly 
# raise an exception when encountering an error 
# condition within your code

def divide(x, y):
    try:
        return x /y
    except ZeroDivisionError:
        return "Division by zero nimekataa"
print(divide(5, 0))

# This can also be written as:
def divide2(x, y):
    if y==0:
        return "Division by zero haiwezi"
    else:
        return x / y
print(divide2(5,0))

# or

def divide3(x, y):
    if y == 0:
        raise ValueError("Division by zero haiwezi")
    return x / y
print(divide3(5, 0))  # This will raise an exception