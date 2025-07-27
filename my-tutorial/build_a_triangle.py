import time
# Using a for loop to print a star triangle

print("We want to build a triangle...")
time.sleep(2)
print("And we want you to help...")
time.sleep(2)

rows = int(input("How many number of rows should it have? "))

triangle = ''
for i in range(rows):
    triangle += '*'
    print(triangle)

