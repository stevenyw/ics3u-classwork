import random
number = random.randrange(1, 11)

print("I'm thinking of a number between 1 and 10.")
guess = int(input("Your guess: "))

if guess == number:
    print("Wtf? You actually got it right? Why don't you go to the casino right now or something, luck piece of garbage.")
else:
    print("LOL u didn't get it right what a loser imagine being you lol...")