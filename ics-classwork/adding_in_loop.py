import random
print("I'll add all the numbers you give me.")
total = 0
x = int(input("Number: "))
while x != 0:
    total += x
    print(f"The total so far is {total}.")
    x = int(input("Number: "))
    
print(f"The answer is {total}.")
