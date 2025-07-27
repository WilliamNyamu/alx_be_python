#  Ordered, immutable collections of items similar to lists 
# but enclosed in parentheses (). Once created, their elements 
# cannot be changed

my_tuple = (1, 2, 3, 4, 5)
# Tuple Indexing
print(my_tuple[0])
print(my_tuple[3])
print(my_tuple[-1])
# Tuple length. Use len()
length = len(my_tuple)
print(length)

## Nested Tuples
# Tuples can contain values of any data type, 
# even lists and other tuples. These inner tuples are 
# called nested tuples

a_tuple = ([1, 2, 3], (4, 5, 6))
print(a_tuple[0])
print(a_tuple[1][2])

# Tuples can be sliced as lists

## Tuple Methods
b_tuple = (4, 4, 5, 6, 6, 7, 8, 9, 10)
print(b_tuple.count(10))
print(b_tuple.index(7))

# 💡 Tip: tuples are immutable. 
# They cannot be modified, so we can't add, update, or 
# remove elements from the tuple.

# 🧠 tuple assignment
# Tuple assignment is assigning values to multiple variables on the same line.
# a, b = 1, 2
# They're commonly used in swapping values
# a,b = b, a
