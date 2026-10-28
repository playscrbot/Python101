count = 1

while count <= 5:
    print(count)

numbers = [10, 20, 30, 40, 50]
for number in numbers:
    if number == 30:
        break
    print(number)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)