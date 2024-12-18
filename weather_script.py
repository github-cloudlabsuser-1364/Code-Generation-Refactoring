import requests

# Fetch weather data from OpenWeatherMap API

def get_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'appid': api_key, 'q': city, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Error fetching data for {city}: {data['message']}")

if __name__ == '__main__':
    api_key = '64ebeea618bd6496526eed3d784cd3b7'  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(api_key, city)