number = int(input("Count from: "))
number2 = int(input("Count to: "))
number3 = int(input("Count by: "))

print("Output:")
for n in range(number, number2+1, number3):
    print(f"{n}")
    