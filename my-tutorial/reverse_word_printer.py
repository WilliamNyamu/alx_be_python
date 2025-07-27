# Printing each letter in reverse order


# The user enters a word and each letter gets printed in reverse order
word = input("Enter a word: ")
for letter in word[::-1]: # slicing the string to reverse it.
    print(letter)

