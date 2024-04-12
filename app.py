import requests

url = "https://api.coinlore.net/api/global/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
