# A python script for determining the prime numbers
# Illustrates the break and continue statements

# Use the break statement when you want to exit a loop when a certain condition is met.

for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            print (f" {n} equals {i} * {n / i}")
            break # The BREAK statement breaks out of the innermost loop.
    else:
        # loop fell through without finding a factor
        print(f"{n} is a prime number")

# In a for loop, the break statement is executed once the final iteration in the loop has been reached.
# The else statement is run when the break statement is not executed.

for letter in 'Python':
    if letter == 'h':
        break  # Breaks out of the loop when 'h' is encountered
    print("Letter: ", letter)


# Using a while loop, let's demonstrate the break statement.
num = 0
while num < 20:
    num+=1
    print("Current number: ", num)
    if num == 9:
        break