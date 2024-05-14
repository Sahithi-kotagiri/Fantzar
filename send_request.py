import requests

url = 'http://127.0.0.1:5000/orders'
payload = {"components": ["I", "A", "D", "F", "K"]}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
