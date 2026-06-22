import requests

API_KEY = "your_actual_key_here"  # your OpenWeatherMap key

def get_weather_montreal() -> str:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Montreal,CA",    # controls the city
        "appid": API_KEY,
        "units": "metric"
    }
    data = requests.get(url, params=params).json()
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"]["description"].capitalize()
    humidity = data["main"]["humidity"]
    return (
        f"🌤 Good morning! Weather in Montréal:\n"
        f"• {desc}\n"
        f"• 🌡 {temp}°C (feels like {feels}°C)\n"
        f"• 💧 Humidity: {humidity}%"
    )

print(get_weather_montreal())
