import random
number = random.randrange(1, 11)

print("I'm thinking of a number between 1 and 10.")
guess = int(input("Your guess: "))
while number != guess:
    print("That's wrong, try again.")
    guess = int(input("Your guess: "))

print(f"That's correct! It's {number}!")
    