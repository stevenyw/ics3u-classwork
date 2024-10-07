gender = input("Are you a male or a female? No LGBT people here, sorry guys. I'm not racist.")
fname = input("First name: ")
lname = input("Last name: ")
age = int(input("Age: "))

if age >= 20:
    married = input(f"Are you married, {fname}?")
    
    if gender == "male":
        if married == "yes":
            if age >= 20:
                print(f"I shall call you Mr. {lname}.")
    elif gender == "female":
        if married == "yes":
            print(f"I shall call you Mrs. {lname}.")
        elif married == "no":
            print(f"I shall call you Ms. {lname}.")
    
else:
    if gender == "male" and age < 20:
        print(f"I shall call you {fname} {lname}.")
    elif gender == "female" and age < 20:
        print(f"I shall call you {fname} {lname}.")