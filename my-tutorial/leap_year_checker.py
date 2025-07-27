# Checks if a given year is a leap year. 
# The user enters a certain year and the programs returns whether the year is leap or not.
# A leap year is divisible by 4 and not divisible by 100

year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year%400 == 0:
        print(f"{year} is a leap year")
    elif year%100 != 0:
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")
else:
    print(f"{year} is not a leap year")