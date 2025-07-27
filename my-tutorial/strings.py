# To quote a quote, we need to "escape" it, by preceding it with \
print('doesn\'t')  # use \' to escape the single quote

# \n means a new line
# Without print() special characters are included in the string. With print() they are interpreted
print("First Line.\nSecond Line")

# If you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an "r" before the first quote:
print(r"C:\some\name")

# strings can be concateneted with the + operator and repeated by the * operator:
print(3 * 'un' + 'ium')
print('Wi' + 2 * 'l' + 'iam')
print('E' + 2 * 'm' + 'anuel')
print('Is' + 2 *'a' + 'c')

# Putting several strings together within parenthesis
text = ('Put several strings together within parentheses '
        'to have them joined together.')
print(text)
