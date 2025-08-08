#  A script to count the letters in a string
sum = 0
user_input = input("Enter the word/phrase for count: ").lower()

for i in user_input:
    sum += 1
print(sum)

print(len(user_input))