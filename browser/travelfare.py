import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("IGNAV_API_KEY")

if not API_KEY:
    raise RuntimeError("Add IGNAV_API_KEY to your .env file")

url = "https://ignav.com/api/fares/one-way"

payload = {
    "origin": "DCA",
    "destination": "EAS",
    "departure_date": "2026-11-20",
}

response = requests.post(
    url,
    headers={
        "X-Api-Key": API_KEY,
        "Content-Type": "application/json",
    },
    json=payload,
    timeout=30,
)

print("HTTP status:", response.status_code)
response.raise_for_status()

print(response.text)

data = response.json()

print("Route:", data.get("origin"), "to", data.get("destination"))
print("Travel date:", data.get("departure_date"))
print("Observed at:", data.get("observed_at"))

for flight in data.get("itineraries", []):
    price = flight.get("price", {})
    outbound = flight.get("outbound", {})
    segments = outbound.get("segments", [])

    print("\nAirline:", outbound.get("carrier"))
    print("Fare:", price.get("amount"), price.get("currency"))
    print("Duration:", outbound.get("duration_minutes"), "minutes")
    print("Stops:", max(0, len(segments) - 1))