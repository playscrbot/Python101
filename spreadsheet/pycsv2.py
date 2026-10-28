headers = [ "Employee ID", "Name", "Department", "Status" ]
row = [ "EMP-1001", "Anita", "Operations", "Active" ]

record = dict(zip(headers, row))
print(record)