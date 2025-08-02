import requests # Importing the requests module for getting the weather data

# Build the URL
# | Part                        | Meaning                                                                                                 |
# | --------------------------- | ------------------------------------------------------------------------------------------------------- |
# | `http://api.weatherapi.com` | The **base domain** of the API                                                                          |
# | `/v1/current.json`          | The **endpoint** — tells the API you want current weather data in JSON format                           |
# | `?key=YOUR_API_KEY`         | A **query parameter** — you must send your personal API key so the server can authenticate your request |
# | `&q={CITY}`                | Another query parameter — `q` is the **query for location**, here it's Nairobi                          |
# | `&aqi=no`                   | Optional parameter — means **"Air Quality Index = no"** (you don’t want AQI data)                       |

API_KEY = "d766b13d9d8744809e4102426250208"
City = input("Enter the city: ").title()

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={City}&aqi=no"

# Make the request to the server
response = requests.get(url)

#The status_code tells us how did it go with the request we made.
print(response.status_code) # Find more status codes and their meaning at the bottom

if response.status_code == 200:
    # Convert the data into a python dictionary
    data = response.json()

    # Extract the relevant weather data
    location = data.get('location', {}).get('name')
    country = data.get('location', {}).get('country', {})
    temperature = data.get('current', {}).get('temp_c')
    condition = data.get('current', {}).get('condition', {}).get('text')

    # Print the weather info
    print(f"\nWeather in {location}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
else:
    print("Error fetching weather data. The status code returned is ", {response.status_code})

# | Status Code | Meaning               | Explanation                                                            |
# | ----------- | --------------------- | ---------------------------------------------------------------------- |
# | **200**     | OK                    | ✅ The request was successful, and you can safely use `response.json()` |
# | 400         | Bad Request           | ❌ You probably sent something wrong (e.g., invalid city)               |
# | 401         | Unauthorized          | ❌ Your API key is missing or incorrect                                 |
# | 403         | Forbidden             | ❌ You don't have permission to access this resource                    |
# | 404         | Not Found             | ❌ The API endpoint or city doesn't exist                               |
# | 500         | Internal Server Error | ❌ Something went wrong on the server's side                            |

