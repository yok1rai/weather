import requests

SERVER_URL = "http://127.0.0.1:5000/weather"

def conn(city: str):
    try:
        response = requests.get(SERVER_URL, params={"city": city}, timeout=5)
        data = response.json()
        return data
    except requests.RequestException as e:
        return {"error": str(e)}

def show(city: str):
    data = conn(city)
    if 'error' in data:
        return f"Error: {data['error']}"

    return (
        f"City: {data.get('name', city)}\n"
        f"Weather is {data.get('weather', [{}])[0].get('description', 'N/A')}\n"
        f"Temperature is {data.get('main', {}).get('temp', 'N/A')}°C\n"
        f"Humidity level is {data.get('main', {}).get('humidity', 'N/A')}%\n"
        f"Lastly, the wind speed is {data.get('wind', {}).get('speed', 'N/A')} m/s"
    )
