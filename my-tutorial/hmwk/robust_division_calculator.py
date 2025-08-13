def safe_divide(numerator, denominator):
    try:

        if denominator == 0:
            return "Error: Cannot divide by zero"
        result = float(numerator) / float(denominator)
        return result
    except ValueError:
        return "Error: Please enter numeric values only."


    
