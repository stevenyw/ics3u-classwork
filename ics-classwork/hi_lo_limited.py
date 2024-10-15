import random
print("I'm thinking of a number between 1 and 100. Try to guess it. You have 7 guesses.")
x = random.randrange(1, 101)
guess = 0
loop = True

while guess < 7 and loop == True:
    chance = int(input(f"Guess #{guess + 1}: "))
    guess += 1
    
    if chance > x:
        print("You're too high.")
        
    elif chance < x:
        print("You're too low.")
        
    elif chance == x:
        print(f"You got it! It's {x}!")
        loop = False

if guess == 7 and loop == True:        
    print(f"You took more than 7 tries. Game over. The answer was {x}.")
    loop = False
        