from datetime import datetime, date, timedelta, timezone
# Converting to other timezones

now = datetime.now() # Current local datetime (date & time)
print(now)
today = date.today() # Shows today's date (date only)
print(today)
print(datetime.now().date())
current_time = datetime.now().time() # Shows the current time(time only)
print(current_time)

# Create Specific Dates/Times
custom_date = datetime(2025, 12, 25, 15, 30) # Dec 25, 2025 @ 3:30 PM
print(custom_date)

#Formatting and Parsing 
# Convert to String (strftime) => String format time
formatted = now.strftime("%Y.%m.%d %H:%M:%S")
print(formatted)

# Common format codes:
# %Y: 4-digit year | %m: Month (01-12) | %d: Day (01-31)
# %H: Hour (00-23) | %M: Minute | %S: Second

# Parse String to Datetime(strptime) => String Parse Time
date_str = "25 December 2025 3:30 PM"
parsed = datetime.strptime(date_str, "%d %B %Y %I:%M %p")
print(parsed)

# Date Arithmetic
future = now + timedelta(days=7, hours=3)
past = now - timedelta(weeks=2)
years = now - timedelta(days=365)

print(future)
print(past)
print(f"Years: {years}")

# Calculate Differences
new_year = datetime(2026, 1, 1)
time_left = new_year - now
print(time_left.days) # Days remaining until 2026

# Time Zones
utc_now = datetime.now(timezone.utc)
print(utc_now)

test_string = "9 F"
print(test_string.split(sep=' '))