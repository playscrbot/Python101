from pathlib import Path

def extract_field(lines, field_name):
    for line in lines:

        if line.startswith(field_name + ":"):
            return line.split(":", 1)[1].strip()

    return None

folder = Path("reports")
employees = []

for file in folder.glob("*.txt"):
    with file.open("r", encoding="utf-8") as document:
        content = document.read()
        lines = content.splitlines()
        
        employee = {
            "name": extract_field(lines, "Employee Name"),
            "employee_id": extract_field(lines, "Employee ID"),
            "department": extract_field(lines, "Department"),
            "status": extract_field(lines, "Status")
        }

        employees.append(employee)

print(employees)