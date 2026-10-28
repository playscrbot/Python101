import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

for book in soup.select("article.product_pod"):
    title_element = book.select_one("h3 a")
    price_element = book.select_one(".price_color")
    availability_element = book.select_one(".availability")

    if not all([
        title_element,
        price_element,
        availability_element,
    ]):
        print("Skipping an incomplete listing.")
        continue

    title = title_element.get("title") or title_element.get_text(strip=True)
    price = price_element.get_text(strip=True)
    availability = " ".join(
        availability_element.stripped_strings
    )

    print("Title:", title)
    print("Price:", price)
    print("Availability:", availability)
    print("-" * 30)