import requests

r = requests.get("https://api.coingecko.com/api/v3/ping")

print(r)