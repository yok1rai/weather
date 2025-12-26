import requests

def conn(city:str, api:str):
    api_key = api

    city = city

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:
        return {
        "City": {data['name']},
        "Weather": f'{data['weather'][0]['description']}',
        "Temperature": f'{data['main']['temp']}°C',
        "Humidity": f'{data['main']['humidity']}%',
        "Wind speed": f'{data['wind']['speed']} m/s'
        }
    else:
        return {"error": data.get('message', 'Unknown error')}

def show(city:str):
    data = conn(city)

    return f"City: {data['City']} \nWeather is {data['Weather']}\nTemperature is {data['Temperature']}\nHumidity level is {data['Humidity']}\nLastly, the wind speed is {data['Wind speed']}"
