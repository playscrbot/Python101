age = int("twenty")

print("Hello"

number = int("hello")

try:
    with open("employees.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("The employee file was not found.")

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print(f"You entered {number}.")

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
finally:
    print("Program finished.")