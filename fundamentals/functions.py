invoices = [
    {"customer": "John", "quantity": 2, "price": 500},
    {"customer": "Priya", "quantity": 3, "price": 750},
    {"customer": "Arun", "quantity": 1, "price": 1200}
]

def calculate_total(quantity, price):
    return quantity * price

for invoice in invoices:
    total = calculate_total(
        invoice["quantity"],
        invoice["price"]
    )

    print(f'{invoice["customer"]}: ₹{total:.2f}')