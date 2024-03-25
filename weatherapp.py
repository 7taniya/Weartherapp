import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the name of the city\n")

url = f'http://api.weatherapi.com/v1/current.json?key=15f4cab8c59f401c996150553241602&q={city}'

r = requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]

engine.say(f'The current weather in the {city} is {w}degrees')
engine.runAndWait()



