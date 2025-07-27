# This is a classic interview question
# Task:
# For numbers from 1 to 100:
# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
# Otherwise, print the number

for i in range(1, 101):
    if i%3 == 0:
        if i%5 == 0:
            print(f"{i} => FizzBuzz")
        else:
            print(f"{i} => Fizz")
    elif i%5 == 0:
        print(f"{i} => Buzz")
    else:
        print(f"{i}")