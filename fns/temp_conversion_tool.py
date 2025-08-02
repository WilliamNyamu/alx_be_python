FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    convert = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{convert}°C"

def convert_to_fahrenheit(celcius):
    convert = CELSIUS_TO_FAHRENHEIT_FACTOR * celcius + 32
    return f"{convert}°F"

def main():
    user_prompt = float(input("Enter a temperature to convert: "))
    user_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().capitalize()
    if user_unit == "F":
        conversion = convert_to_celcius(user_prompt)
        print(f"{user_prompt}°{user_unit} is {conversion}")
    elif user_unit == "C":
        conversion = convert_to_fahrenheit(user_prompt)
        print(f"{user_prompt}°{user_unit} is {conversion}")
    else:
        print("Invalid Temperature. Please enter a numeric value.")
    
main()

