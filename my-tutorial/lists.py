# Comma-separated values between square brackets. 
# They may contain items of different types, but usually of the same type

squares = [1, 4, 9, 16, 25]
print(squares)
squares.append(6**2)
print(squares)

#Indexing lists
print(squares[0])
print(squares[-1])
print(squares[-3:]) # Slicing returns a new list
#Slicing
print(squares[:]) #Returns a copy of the list
# List concatenation
print(squares + [36, 49, 64, 81, 100])

# Lists are mutable, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125] # something's wrong here
cubes[3] = 4**3 # Replacing 65 with 64
print(cubes)

# Add new items at the end of the list using the .append() method
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print(cubes)

# Slicing lists is also possible
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters)
print(len(letters)) # len() is a built-in function that shows the count of the number of elements in the list.
letters [2:5] = ['C', 'D', 'E'] # replace some values
print(letters)
letters [2:5] = [] # remove some values
print(letters)
letters [:] = [] # Clear the list by replacing all the elements with an empty list
 
# It is possible to nest lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
