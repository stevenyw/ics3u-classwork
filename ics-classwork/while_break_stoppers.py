a = -1
while a < 10:
    a += 1
    if a == 7:
        continue
    print(a)
print("Finished loop")

b = 5
number = 0
while b < 20:
    number += b
    print(number)
    b += 1
    if b % 3 == 0:
        continue
print("Loop done")

c = int(input("Give me a number."))
d = int(input("Give me another number HIGHER than the first."))
number = 0

while c < d:
    number += c
    print(number)
    c += 1
    if number == 13 or c == 31:
        break
    
while True:
    wordie = input("Choose a word.")
    if wordie == "stop":
        print("Goodbye!")
        break
    print(f"{wordie}")