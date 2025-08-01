# 

# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # returning it for use in future calculation

def calculate_future_date(current_date):
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for days.")

def main():
    current = display_current_datetime()
    calculate_future_date(current)

if __name__ == "__main__":
    main()
