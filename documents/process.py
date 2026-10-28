from pathlib import Path

def extract_field(lines, field_name):
    for line in lines:
        if line.startswith(field_name + ":"):
            return line.split(":", 1)[1].strip()

    return None

def process_document(file):
    with file.open("r", encoding="utf-8") as document:
        lines = document.read().splitlines()

    employee = {
        "source_file": file.name,
        "name": extract_field(lines, "Employee Name"),
        "employee_id": extract_field(lines, "Employee ID"),
        "department": extract_field(lines, "Department"),
        "status": extract_field(lines, "Status")
    }

    return employee

folder = Path("reports")

employees = []
failed_files = []

for file in folder.glob("*.txt"):
    if not file.is_file():
        continue

    try:
        employee = process_document(file)
        employees.append(employee)

    except OSError as error:
        failed_files.append({
            "file": file.name,
            "error": str(error)
        })


print("\nDOCUMENT PROCESSING REPORT")
print("==========================")

print(f"Documents processed: {len(employees)}")
print(f"Documents failed: {len(failed_files)}")