names = ["John", "Mary", "Ravi"]
departments = ["Billing", "Support", "Sales"]

for name, department in zip(names, departments):
    print(f"{name} - {department}")