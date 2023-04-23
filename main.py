import requests
import datetime
import pytz
from tzlocal import get_localzone

timezone = get_localzone()

api_key = '52f91a62b02b5436f13e8f4d24d66971'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

#print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºC")

    sunset_timestamp = weather_data.json()['sys']['sunset']
    sunset_datetime = datetime.datetime.fromtimestamp(sunset_timestamp)
    local_sunset_datetime = sunset_datetime.astimezone(timezone)
    print(f"The sunset in {user_input} is at {local_sunset_datetime.strftime('%H:%M')}")