# Define the height of the pyramid
rows = 5

# Initialize the row counter
i = 1

# Outer loop to handle number of rows
while i <= rows:
    # Print leading spaces
    space = 1
    while space <= (rows - i):
        print(" ", end="")  # Print space without new line
        space += 1

    # Print asterisks
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")  # Print star without new line
        star += 1

    # Move to the next line after printing each row
    print()

    # Increment the row counter
    i += 1
