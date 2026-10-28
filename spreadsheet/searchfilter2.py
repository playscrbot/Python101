import csv

with open("employees3.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        salary = float(row["Salary"])

    if row["Department"] == "Billing" and row["Status"] == "Active" and salary > 30000:
       print(row)