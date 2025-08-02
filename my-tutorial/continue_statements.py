# Continue statements in Python
# You can use the continue statement if you need to 
# skip the current iteration for a for or a while loop and move on to the next iteration

for letter in "Jessica":
    if letter == 'i':
        continue # Here, we are saying that it the letter is i, skip that iteration and continue with the next iteration(s)
    print(letter)

# The output for the above for loop is "J e s s c a"

# Using a while loop

num  = 0

while num < 100:
    num += 10
    if num == 50:
        continue # Here, 50 will not be printed. It will be skipped and the program will execute the next iteration.
    print("Current tens: ", num)