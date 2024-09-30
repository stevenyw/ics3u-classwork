name = input("Hi, what's your name?")
age = int(input(f"Cool name, {name}! How old are you?"))

if age <= 16:
    print(f"Oh, you aren't old enough to drive yet, {name}. What a shame.")
if age > 16 and age < 18:
    print(f"Oh, you aren't old enough to vote yet, {name}. What a shame.")
if age > 18 and age < 21:
    print(f"Oh, you aren't old enough to rent a car yet, {name}. What a shame.")
if age >= 21:
    print(f"Oh my god {name}! You can basically do anything that's legal! Wow!!")
