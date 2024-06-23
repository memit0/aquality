import requests

url = "https://api.openaq.org/v3/countries?order_by=id&sort_order=asc&limit=15&page=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)