# Generate a list of 10 random integers (0–20)
# Use a for loop to print whether each number is even or odd

import random

numbers = [random.randint(0, 20) for _ in range(10)]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

