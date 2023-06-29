import os
from pprint import pprint
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

city = input('Enter city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_KEY + '&q=' + city

weather_data = requests.get(base_url).json()

pprint(weather_data)