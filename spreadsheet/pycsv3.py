import csv

with open("employees2.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file) 
    for employee in reader: 
        hours = float(employee["Hours"]) 
        rate = float(employee["Rate"])
        total = hours * rate 
        print( f"{employee['Name']}: " f"₹{total:.2f}" )