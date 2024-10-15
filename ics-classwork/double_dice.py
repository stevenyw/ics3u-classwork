import random
roll1 = random.randrange(1, 7)
roll2 = random.randrange(1, 7)
while roll1 != roll2:
    print(f"Dice #1: {roll1}")
    print(f"Dice #2: {roll2}")
    answer = roll1 + roll2
    print(f"The total is {answer}!")
    
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)

print(f"Dice #1: {roll1}")
print(f"Dice #2: {roll2}")
answer = roll1 + roll2
print(f"The answer is {answer}!")