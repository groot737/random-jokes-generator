import json
import requests
# name = str(input("enter superhero name: "))
url = 'https://official-joke-api.appspot.com/random_joke'
response = requests.get(url)
response.raise_for_status()
# print(response.text)
x = json.loads(response.text)
print(f"{x['setup']} \n{x['punchline']}")
