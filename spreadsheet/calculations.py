import csv 

employees = []
invalid_records = []

with open("employees4.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for employee in reader:
       try: 
          hours = float(employee["Hours"]) 
          rate = float(employee["Rate"])
          
          employee["Total"] = hours * rate
          employees.append(employee)

          print(f"{employee['Name']}: " f"₹{employee['Total']:.2f}")

       except ValueError as error:
          invalid_records.append({"employee": employee, "reason": str(error)})
          print(f"Invalid record: {employee['Name']}")

          continue