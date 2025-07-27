x = int(input("Please enter an integer: "))

if x==0:
    print("You've entered Zero")
elif x < 0:
    x = 0
    print("Negative changed to Zero")
elif x == 1:
    print("You've entered one")
else: 
    print("More")


# Voting system
age = int(input("What's your age? "))

if age >= 18:
    print("You have reached the age of majority")
    isRegistered = input("Have you registered as a voter? (yes/no) ")
    if isRegistered.lower() == "yes":
        print("You are qualified for voting. Here's your voting card")
    elif isRegistered.lower() == 'no':
        print("You have not registred as a voter. You are therefore not eligible to vote!")
    else: 
        print("Enter a valid answer. Either yes or no")

elif age == 0:
    print("Age cannot be Zero")
else:
    print("You have not reached the age of majority! You are not eligible to vote")

