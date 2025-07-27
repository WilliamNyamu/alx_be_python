# Even or Odd twist. Finding if a number is even or odd

number = int(input("Please enter a number: "))
if number%2 == 0 & number != 0: 
    print(f"{number} is Even!")
elif number == 0:
    print(f"{number} is Zero")
else:
    print(f"{number} is Odd!")