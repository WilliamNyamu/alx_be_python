# Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

# Instructions:

# Prompt for User Input:

# Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
# Make sure you use num1 and num2 for first and second numbers
# Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.
# Perform the Calculation Using Match Case:

# Implement a Match Case statement that executes the chosen operation based on the user’s input.
# For addition (+), subtract (-), multiply (*), and divide (/).
# Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.
# Output the Result:

# Display the result of the operation in a user-friendly message, e.g., The result is [result].
# Example Interaction:

# Enter the first number: 10
# Enter the second number: 5
# Choose the operation (+, -, *, /): *
# The result is 50.
# Or, for a division by zero scenario:

# Enter the first number: 10
# Enter the second number: 0
# Choose the operation (+, -, *, /): /
# Cannot divide by zero.

# match_case_calculator.py

# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the operation using match-case
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        # Handle division by zero
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        # Handle invalid operation input
        print("Invalid operation selected.")
