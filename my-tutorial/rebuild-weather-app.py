import requests

def main():
    user_ask = input("Enter the city: ").strip().title()
    city, country, temp, condition = weather(user_ask)
    print(f"The weather for {city}, {country}: \nTemperature: {temp}°C \nCondition: {condition}")



def weather(location):
    """Build the URL First"""
    API_KEY = ""
    url = f"https://api/weatherapi.com/v1/current.json?key={API_KEY}&q={location}&aqi=no"

    """Make the request"""
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        city = data.get("location", {}).get("name", {})
        country = data.get("location", {}).get("country", {})
        temp = data.get("current", {}).get("temp_c", {})
        condition = data.get("current", {}).get("condition", {}).get("text")
    else:
        print("Enjoy guessing the weather!")
    
    return city, country, temp, condition


main()