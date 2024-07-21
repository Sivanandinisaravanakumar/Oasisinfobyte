import requests
import sys

API_KEY = 'd48b4e28ba02c8effd9cbd7bfee9d926' 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def display_weather(data):
    if data['cod'] == 200:
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        print(f"Temperature: {temperature - 273.15:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {description.capitalize()}")
    else:
        print("City not found. Please check the name and try again.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_app.py <london>")
        sys.exit(1)
    
    city_name = sys.argv[1]
    data = get_weather(city_name)
    display_weather(data)

if __name__ == "__main__":
    main()
