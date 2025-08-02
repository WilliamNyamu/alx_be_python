from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d || %H:%M:%S")
    return current_date, formatted

now, formatted_now = display_current_datetime()
print(f"Current date and time: {formatted_now}")

def calculate_future_date():
    user_days = float(input("Enter number of days: "))
    future_date = now + timedelta(days=user_days)
    formatted = future_date.strftime("%Y-%m-%d")
    return formatted

future_date = calculate_future_date()
print(f"Future date: {future_date}")

def calculate_remaining_days():
    orientation_day = "18 August 2025"
    formatted_date = datetime.strptime(orientation_day, "%d %B %Y")
    number_of_days = formatted_date - now
    return number_of_days

remaining_days = calculate_remaining_days()
print(f"Remaining Days: {remaining_days}")


