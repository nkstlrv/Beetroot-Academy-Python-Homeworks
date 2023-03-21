import requests
import time
import datetime
API_KEY = "20fca90e9840c31f863055091efb8b32"


# Function to convert time in Unix timestamp format into human-readable format
def time_converter(unix_timestamp):
    date_time = datetime.datetime.fromtimestamp(unix_timestamp)
    return date_time.strftime('%H:%M:%S %d-%m-%Y')


# Main input script
print('\nHello there 👋\n'
      'This is Terminal Weather v0.1 ⛅\n\n'
      'I can tell you current weather in the given city 🏙️\n')

city = input("Just type any wished city and press ENTER: ").title()

print("\nThanks 😊\n"
      "🤖Performing your data...\n")
time.sleep(1.5)


try:
    weather_api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
                               f"&units=metric")
    weather_data = weather_api.json()

# Converts cloud sky coverage from % to octanes
    clouds_info = 0
    if 12.5 >= weather_data['clouds']['all'] > 0:
        clouds_info = 1
    elif 25 >= weather_data['clouds']['all'] > 12.5:
        clouds_info = 2
    elif 37.5 >= weather_data['clouds']['all'] > 25:
        clouds_info = 3
    elif 50 >= weather_data['clouds']['all'] > 37.5:
        clouds_info = 4
    elif 62.5 >= weather_data['clouds']['all'] > 50:
        clouds_info = 5
    elif 75 >= weather_data['clouds']['all'] > 62.5:
        clouds_info = 6
    elif 87.5 >= weather_data['clouds']['all'] > 75:
        clouds_info = 7
    elif weather_data['clouds']['all'] > 87.5:
        clouds_info = 8

# Weather description
    description = f"{'*' * 50}\n" \
                  f"\n{city} {weather_data['coord']['lat'], weather_data['coord']['lon']}\n" \
                  f"{time_converter(weather_data['dt'])}\n" \
                  f"{'-' * 50}\n" \
                  f"Weather --> {(weather_data['weather'][0]['main']).title()}\n" \
                  f"Description --> {(weather_data['weather'][0]['description']).title()}\n" \
                  f"Clouds --> {weather_data['clouds']['all']} % ({clouds_info} Octanes)\n" \
                  f"{'-' * 50}\n" \
                  f"Temperature --> {weather_data['main']['temp']} °C\n" \
                  f"Feels like --> {weather_data['main']['feels_like']} °C\n" \
                  f"Today's MIN --> {weather_data['main']['temp_min']} °C\n" \
                  f"Today's MAX --> {weather_data['main']['temp_max']} °C\n" \
                  f"{'-' * 50}\n" \
                  f"Wind:\n" \
                  f"Speed --> {weather_data['wind']['speed']} kph\n" \
                  f"Direction --> {weather_data['wind']['deg']}°\n" \
                  f"Gusts --> {weather_data['wind'].get('gust', 0)} kph\n" \
                  f"{'-' * 50}\n" \
                  f"Visibility --> {weather_data['visibility']} meters\n" \
                  f"{'-' * 50}\n" \
                  f"Humidity --> {weather_data['main']['humidity']} %\n" \
                  f"{'-' * 50}\n" \
                  f"Pressure --> {weather_data['main']['pressure']} hPa\n" \
                  f"{'-' * 50}\n" \
                  f"Sunset --> {(time_converter(weather_data['sys']['sunset']))[0:8]}\n" \
                  f"Sunrise --> {(time_converter(weather_data['sys']['sunrise']))[0:8]}" \
                  f"\n{'*' * 50}\n"


    print(f"😍🥳Here are the current weather in {city}")
    print(description)
    print("🤞Hope to see you soon. Bye👋\n")
except Exception:
    print(f"🙄😓😭 Can't find the weather by the given city --> {city}...\n"
          f"Try to check the city's spelling and try again")

