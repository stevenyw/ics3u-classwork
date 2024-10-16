# The program still works because the code is still true, and it doesn't matter if "again" is yes or no anymore at the start.

import random
while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)
    
    again = input("Would you like to flip again (y/n)? ")
    if again == "n":
        break
