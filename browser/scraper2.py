import requests
from bs4 import BeautifulSoup

url = "https://gumroad.com/discover"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("Status code:", response.status_code)
print(response.text[:500])