import requests
import pprint

with open('api.txt', "r") as file:
    access_key = file.read().strip()


# print(api_key)
query = input("What city would you like to know the weather for?")

url = f"http://api.weatherstack.com/current?access_key={access_key}&query={query}"

response = requests.post(url)
pprint.pprint(response.json())