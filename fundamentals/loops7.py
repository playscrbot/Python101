records = [
    {"name": "John", "valid": True},
    {"name": "Mary", "valid": False},
    {"name": "Ravi", "valid": True}
]

for record in records:
    if not record["valid"]:
        continue

    print(f"Processing {record['name']}")