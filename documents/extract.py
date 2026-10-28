with open("employee.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

if "Department:" in content:
    print("Department information found.")

lines = content.splitlines()

for line in lines:
    print(line)

print(content.count("Status:"))

line = "Department: Operations"
parts = line.split(":", 1)

parts = ["Department", "Operations"]
value = parts[1].strip()

print(value)