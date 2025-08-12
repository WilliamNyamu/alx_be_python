# Get the file handler
fhand = open('daffodils.txt')
print(fhand)

# Loop through each line via file handler
# for line in fhand:
#     print(line)

# There's a new line character at the end of each line which prints
# output to the next line. We can visualize it using the repr method.
# for line in fhand:
#     print(repr(line))

# Use this instead
for line in fhand:
    print(line, end='')

# Letting the user choose a file
fname = input('Enter the file name: ')
ghand = open(fname)
count = 0
for line in ghand:
    count = count + 1
print(f"There are {count} lines in {fname}")


# Writing into a file
fout = open('flower.txt', 'w')
fout.write("This content would be added and existing would be discarded")
fout.close()

my_lst = ["William"]
another_name = input("Enter another name: ").strip()
my_lst.append(another_name)
test_string = ' '.join(my_lst)
print(test_string)
