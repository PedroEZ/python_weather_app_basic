# Import necessary modules
import requests
import datetime
import pytz
from tzlocal import get_localzone

# Get the local timezone of the user's device
timezone = get_localzone()

# Set the API key for OpenWeather API
api_key = '52f91a62b02b5436f13e8f4d24d66971'

# Get the user input for the city they want to check the weather for
user_input = input("Enter city: ")

# Send a request to the OpenWeather API to get the weather data for the city entered by the user
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

# Check if the API returned a valid response
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    # Parse the weather and temperature data from the JSON response
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
    # Print the weather and temperature data to the user
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºC")
    
    # Get the sunset time and convert it to the user's local timezone
    sunset_timestamp = weather_data.json()['sys']['sunset']
    sunset_datetime = datetime.datetime.fromtimestamp(sunset_timestamp)
    local_sunset_datetime = sunset_datetime.astimezone(timezone)
    
    # Print the sunset time to the user
    print(f"The sunset in {user_input} is at {local_sunset_datetime.strftime('%H:%M')}")
