invoices = [ 
    {"customer": "John", "quantity": 2, "price": 500, 'member': True }, 
    {"customer": "Priya", "quantity": 3, "price": 750, 'member': True }, 
    {"customer": "Arun", "quantity": 1, "price": 1200, 'member': False } 
] 

def calculate_total(quantity, price): 
        return quantity * price 

def calculate_discount(total, is_member): 
        if total >= 2000:         
            return total * 0.10 
        else: 
            return 0 

for invoice in invoices: 
        total = calculate_total( invoice["quantity"], invoice["price"] )
        discount = calculate_discount(total, invoice['member']) 
        final_amount = total - discount

        if final_amount >= 2000:
           category = "Large"
        elif final_amount >= 1000:
           category = "Standard"
        else:
           category = "Small"

        if not invoice["member"]:       
           customer_type = "Regular"
        else: 
           customer_type = "Member"

        print(f'Customer: {invoice["customer"]}') 
        print(f'Total: ₹{total:.2f}')
        print(f'Discount: ₹{discount:.2f}')
        print(f'Final amount: ₹{final_amount:.2f}')
        print(f'Category: {category}')
        print(f'Customer type: {customer_type}')
        print("-" * 30)