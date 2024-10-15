import random
number = random.randrange(1, 11)
attempts = 0

print("I'm thinking of a number between 1 and 10.")
guess = int(input("Your guess: "))
attempts += 1

while guess != number:
    print("LOL u didn't get it right what a loser imagine being you lol...")
    guess = int(input("Your guess: "))
    attempts += 1
    
print("Oh you got it right. You lucky buffoon.")
print(f"It took you {attempts} attempts.")
    
