# Hermes Daily Weather Brief (Montréal)

This project adds a custom **Hermes Agent skill** that sends a daily weather briefing for **Montréal, Canada** to Telegram at 8:00 AM (America/Toronto time).

It showcases:
- Writing a small Python integration with the **OpenWeatherMap API**
- Creating a reusable **Hermes skill (SKILL.md)**
- Using Hermes **/goal** and **cron** features to automate a recurring task

---

## Features

- Fetches current weather for **Montréal, CA** (metric units)
- Formats a friendly morning message with:
  - Description (e.g. _Light rain_)
  - Temperature and feels‑like
  - Humidity
- Sends the result to your **Telegram** via Hermes
- Runs automatically every day at **8:00 AM** (configurable)

---

## Requirements

- Hermes Agent running on Linux (tested on Ubuntu)  
- Python 3 with `requests` installed  
- OpenWeatherMap API key  
- Hermes Telegram gateway configured with your Telegram user ID

---

## Setup

1. **Test the OpenWeatherMap API**

   ```bash
   curl "https://api.openweathermap.org/data/2.5/weather?q=Montreal,CA&appid=YOUR_API_KEY&units=metric"
   ```

2. **Create the Hermes skill folder**

   ```bash
   mkdir -p ~/.hermes/skills/weather-brief
   cd ~/.hermes/skills/weather-brief
   ```

3. **Create the Python script**

   ```bash
   nano ~/.hermes/skills/weather-brief/weather.py
   ```

   Paste:

   ```python
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
   ```

   Test it:

   ```bash
   python3 ~/.hermes/skills/weather-brief/weather.py
   ```

4. **Create the SKILL.md**

   ```bash
   nano ~/.hermes/skills/weather-brief/SKILL.md
   ```

   ```markdown
   ---
   name: weather-brief
   description: Fetches current weather for Montréal, Quebec and sends a formatted morning briefing.
   triggers:
     - "morning weather"
     - "weather brief"
     - "daily briefing"
     - "weather in Montreal"
   ---

   ## Steps
   1. Run `python3 ~/.hermes/skills/weather-brief/weather.py`
   2. Send the full output to the user
   ```

5. **Reload skills and verify**

   ```bash
   hermes skills reload
   hermes skills list
   ```

---

## Creating the Daily Goal

From your Hermes chat (terminal or Telegram):

```text
/goal Every day at 8AM Montreal time, use the weather-brief skill and send me the result on Telegram.
```

Hermes will ask for your Telegram numeric user ID (same one you used when setting up the gateway). After that, you can:

- List goals:

  ```text
  /goal status
  ```

- Manually test a run:

  ```text
  /goal run 1
  ```

You should receive a Telegram message like:

```text
🌤 Good morning! Weather in Montréal:
-  Light rain
-  🌡 20.1°C (feels like 20.0°C)
-  💧 Humidity: 71%
```

---

## Timezone

Ensure your server is using the correct timezone:

```bash
timedatectl
sudo timedatectl set-timezone America/Toronto
```

---

## Notes

- Do **not** commit your real API key to a public repo.  
  In `weather.py`, replace `API_KEY` with an environment variable or config file before pushing.
- You can extend this skill later to include:
  - Cybersecurity news
  - Homelab status (Docker, disk usage)
  - Calendar or class reminders
 

<img width="1080" height="2424" alt="1000015986" src="https://github.com/user-attachments/assets/a5429675-6652-488d-9e13-9b3ccde845e6" />
<img width="1021" height="539" alt="image" src="https://github.com/user-attachments/assets/d47afc7f-3c06-49ab-82b7-0312c86786aa" />


