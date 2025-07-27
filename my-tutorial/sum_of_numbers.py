import time

# Calculating the sum of numbers from 1 to 100 and printing the last result only

# Initialiaze a variable
print("Calculating the sum of numbers from 1-100...")
time.sleep(3)
total = 0
for i in range(1,101):
    total += i
print(total)