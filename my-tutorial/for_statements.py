# Iterates over items of any sequence (a list or a string), in the order that they appear in the sequence

# Measure some strings
words = ['Samson','William', 'Emmanuel', 'Isaac']

for w in words:
    print(w, len(w))

# If you need to iterate over a sequence of numbers, the built-in functino range() comes in handy
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

#It is possible to let the range start at another number.
# Or to specify a different increment ( even negative; sometimes this is called the 'step')
print(list(range(5, 10))) # Shows the where to start and stop
print(list(range(0, 10, 3))) # Shows the start, stop, and step

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'the', 'Lamb', 'of', 'God']
for i in range(len(a)):
    print(i, a[i])

