employees = [
    {
        "name": "John Doe",
        "active": True
    },
    {
        "name": "Jane Doe",
        "active": False
    }
]

def employee_status(employee):
    if employee["active"]:
        return "Active"
    else:
        return "Inactive"

for employee in employees:
    status = employee_status(employee)

    print(
        f"{employee['name']} - "
        f"{status}"
    )