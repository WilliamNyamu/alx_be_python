day = input("Enter a day of the week(Monday - Friday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays ...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost the weekend!")
    case "friday":
        print("It's Friday! Time to relax!")
    case _:
        print("Invalid day entered.")
