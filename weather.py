import requests
import pprint

with open('api.txt', "r") as file:
    access_key = file.read().strip()


# print(api_key)
query = input("What city would you like to know the weather for?")

url = f"http://api.weatherstack.com/current?access_key={access_key}&query={query}"

response = requests.post(url)
# pprint.pprint(response.json())

print(f"You queried for {query}. Here is the information about this city.")

country = response.json().get('location', {}).get('country', {})
print(f"Located in {country}")

local_time = response.json().get('location', {}).get('localtime', {})
time = local_time[-5:]
date = local_time[:-5]
print(f"Local time is {time}")
print(f"The date is {date} formatted in Year Month Day")

timezone = response.json().get('location', {}).get('timezone_id', {})
print(f"Time zone is {timezone}")
