import requests

url = "https://gumroad.com/discover"

response = requests.get(url, timeout=15)
response.raise_for_status()

print("Status code:", response.status_code)
print(response.text[:500])