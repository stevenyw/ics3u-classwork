import random
attempts = 1
number = random.randrange(1, 11)

print("I'm thinking of a number between 1 and 10.")
while True:
    guess = int(input("Your guess: "))

    if guess != number:
        print("LOL u didn't get it right what a loser imagine being you lol...")
        guess = int(input("Your guess: "))
        attempts += 1
    
    if guess == number:
        print("Oh you got it right. You lucky buffoon.")
        print(f"It took you {attempts} attempts.")
        break
    