name = input("Hi! What's your name? Sorry, I have dementia.")
age = int(input(f"Wow, what a GREAT name {name}! I'm kidding. Just give me your age already..."))

if age < 16:
    print(f"Haha {name}! You can't drive! What are you, a fetus?")
elif age >= 16 and age < 18:
    print(f"Cool {name}! You can drive but you can't vote! What are you, a teenager?")
elif age >= 18 and age < 21:
    print(f"Cool {name}! You can drive & vote, but you can't rent a car! What are you, a young adult?")
else:
    print("Oh you can do anything basically. What are you, an adult?")