import random
numberthing = random.randrange(1, 101)

guess = int(input("I'm guessing a number between 1 and 100. Try to guess it. Good luck!"))

if guess == numberthing:
    print("Okay what the hell? You actually got it!!! It's {numberthing}!!!")
elif guess > numberthing:
    print(f"Sorry, you're too high. The answer is {numberthing} hahhhaa. Sorry its extremely hard to guess it ikik lol.")
elif guess < numberthing:
    print(f"Sorry, you're too low. The answer is {numberthing} hahhhaa. Sorry its extremely hard to guess it ikik lol.") 
else:
    print("Error, idiot. You big stupid.")