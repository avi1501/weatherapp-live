from django.conf import settings
import requests

def getweatherdata(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = { 
        'q':city_name,
        'appid': settings.OWM_API_KEY,
        'units':'metric'
    }
    response = requests.get(url, params = params)

    if response.status_code != 200:
        return None

    json_response = response.json()

    weather_data = {

        'temp' : json_response["main"]['temp'],
        'temp_min' : json_response["main"]["temp_min"],
        'temp_max' : json_response["main"]["temp_max"],
        'city_name' : json_response['name'],
        'country' : json_response["sys"]['country'],
        'lat' : json_response['coord']['lat'],
        'lon' : json_response['coord']['lon'],
        'weather': json_response['weather'][0]['main'],
        'weather_desc': json_response['weather'][0]['description'],
        'pressure' : json_response['main']['pressure'],
        'humidity' : json_response['main']['humidity'],
        'wind_speed' : json_response['wind']['speed'],


    }

    return weather_data