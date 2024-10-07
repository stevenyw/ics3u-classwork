import random
me = random.randrange(1, 4)

print("You come up to Mr. Morpheus' table for a Matrix-like game. You place a bet of $10,000. This is life or death.")
print("He glances at you. He has three pills. He places them in front of you. [gotta keep it pg here :3]")
print("Which one is the correct pill?")
print("#        #       #")
guess = int(input(("1        2       3")))
if guess == me:
    print("The pill does nothing. You won. You get your bag and leave with the stacks of cash.")
# I don't know how to do that cool hashtag thingie with the aces so I just skipped that lol
else:
    print("The pill makes your lungs explode, which prevents you from breathing and you die. Morpheus stares at you with zero emotion, and walks away.")