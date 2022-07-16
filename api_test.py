import requests

api_url = "https://api.agify.io?name=michael"

response = requests.get(api_url)

print(response.json())