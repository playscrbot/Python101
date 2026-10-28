employee = {}

with open("employee.txt", "r", encoding="utf-8") as file:
    content = file.read()
    
    lines = content.splitlines()
    
    for line in lines:
        if ":" not in line:
            continue
        
        key, value = line.split(":", 1)
        
        key = key.strip()
        value = value.strip()
        
        employee[key] = value

print(employee)