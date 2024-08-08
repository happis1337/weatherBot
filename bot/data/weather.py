import requests

def get_weather_day():
    url = f"https://api.weatherapi.com/v1/forecast.json?key=cd561d4bc365492682c45737242007&q=40.3833,71.7833&days=1"
    response = requests.get(url).json()['current']
    last_updated = response["last_updated"]
    temp_c = response['temp_c']
    wind_kph = response['wind_kph']
    humidity = response['humidity']
    cloud = response['cloud']
    result = f"""
time : {last_updated} 🕝
temperature: {temp_c}°C 🌡
wind speed: {wind_kph} 🌬
cloud: {cloud} % ☁️
humidity: {humidity} 💧
"""
    return result


def get_weather_week():
    url = f"https://api.weatherapi.com/v1/forecast.json?key=cd561d4bc365492682c45737242007&q=40.3833,71.7833&days=7"
    response = requests.get(url).json()['forecast']['forecastday']
    result = "weather:\n"
    for i in response:
        date = i['date']
        maxtemp_c = i['day']['maxtemp_c']
        mintemp_c = i['day']['mintemp_c']
        avgtemp_c = i['day']['avgtemp_c']
        maxwind_kph = i['day']['maxwind_kph']
        avghumidity = i['day']['avghumidity']

        result_day = f"""
data: {date}
Max temperature: {maxtemp_c}°C 🌡
Min temperature: {mintemp_c}°C 🌡
average temperature : {avgtemp_c}°C 🌡
max wind speed: {maxwind_kph} 🌬
humidity : {avghumidity} 💧
"""
        result += result_day
    return result


def get_weather_hours():
    url  = 'https://api.weatherapi.com/v1/forecast.json?key=cd561d4bc365492682c45737242007&q=40.3833,71.7833&days=7'
    response = requests.get(url).json()['forecast']['forecastday'][0]['hour']
    result = "weather:\n""'"
    for i in response:
        time = i['time']
        temp_c = i['temp_c']
        wind_kph = i['wind_kph']
        humidity = i['humidity']

        result_hour = f"""
        time = {time}
        temperature : {temp_c}°C
        wind speed : {wind_kph}
        humidity: {humidity} 
        """
        result += result_hour
    return result
