name = input("What's your last name?")
if name <= "Carswell":
    print(f"It's gonna be a really short time, {name}!")
elif name > "Carswell" and name <= "Jones":
    print(f"It's not gonna be bad, {name}!")
elif name > "Jones" and name <= "Smith":
    print(f"It's gonna be a little bit of a wait, {name}.")
elif name > "Smith" and name <= "Young":
    print(f"It's gonna be a little long of a wait, {name}.")
else:
    print(f"It's gonna be a damn long time, {name}.")