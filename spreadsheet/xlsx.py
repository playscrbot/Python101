headers = (
    "Employee ID",
    "Name",
    "Department",
    "Status"
)

values = ( 
    { "EMP-1001", "Anita", "Operations", "Active" },
    { "EMP-1002", "Ravi", "Billing", "Active" },
    { "EMP-1003", "Rahul", "Administration", "Inactive" }
)

with open("employees.xlsx", "w", encoding="utf-8") as file:
    file.write("\t".join(headers) + "\n")

    for value in values:
        file.write("\t".join(value) + "\n")