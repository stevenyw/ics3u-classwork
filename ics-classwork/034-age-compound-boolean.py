name = input("What's your name?")
age = int(input(f"Hi {name}! Ok honestly im tired of putting on this sweet persona just gimmie your name already ive had a long day."))

if age < 16:
    print(f"Haha, you can't drive, {name}. What a loser.")
if age >= 16 and age < 18:
    print(f"Haha, you can drive, but you can't vote {name}. What a loser.")
if age >= 18 and age < 24:
    print(f"Haha, you can drive & vote, but you can't rent a car {name}. What a loser.")
if age == 24 or age > 24:
    print(f"Wow, you can basically do anything...Are you God?")