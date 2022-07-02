import random

cert_numbers = []
for i in range(1, 7):
    cert_number = random.randint(1, 9)
    cert_numbers.append(cert_number)

print(*cert_numbers)

while True:
    my_number = [int(_) for _ in input().split()]
    if my_number == cert_numbers:
        print("OKAY")
        break
    else:
        print("WRONG")
