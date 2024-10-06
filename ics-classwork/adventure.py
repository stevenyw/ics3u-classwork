print("Welcome to this adventure!")

option1 = input("You're in this creepy house. Do you wanna go to the 'kitchen' or go 'upstairs'?")

if option1 == "kitchen":
    print("There is a long countertop with dirty dishes everywhere.  Off to one side there is, as you'd expect, a refrigerator. You may open the 'refrigerator' or look in a 'cabinet'.")
    option2 = input()
    if option2 == "refrigerator":
        print("Inside the refrigerator you see food and stuff.  It looks pretty nasty. Would you like to eat some of the food?")
        option3 = input()
        if option3 == "yes":
            print("You die from the food being laced with cyanide. Loser.")
        elif option3 == "no":
            print("You die from starvation. Loser.")
# cabinet option
    elif option2 == "cabinet":
        print("Inside the cabinet you see a bottle of Advil. Do you take it?")
        option3 = input()
        if option3 == "yes":
            print("You die from a drug overdose. Loser.")
        elif option3 == "no":
            print("You die from starvation, hahahaha Loser.")
# upstairs option
elif option1 == "upstairs":
    option2 = input("You see a hallway.  At the end of the hallway is the master 'bedroom'.  There is also a 'bathroom' off the hallway.  Where would you like to go?")
    if option2 == "bedroom":
            option3 = input("You see a large sized king bed. You're feeling quite tired. Do you sleep in it?")
            if option3 == "yes":
                print("Your soul gets possessed by the devil by sleeping in that bed. Mwahahahhaha.")
            elif option3 == "no":
                print("You faint on the floor in fatigue, causing you to get a concussion and dying. Mwahahhahaha.")
    elif option2 == "bathroom":
        option3 = input("You see a mirror on the wall with some red coloured creepy lady on the other side of it. You're feeling the urge to say Bloody Mary three times. Do you give in?")
        if option3 == "yes":
            print("Your soul gets snatched and you lose your life. You're kind of stupid for doing that honestly.")
        elif option3 == "no":
            print("You try to run away but you slip on a banana peel, causing you to trip get a hemmorrage and dying. Idiot.")
else:
    print("PLEASE CHOOSE SOMETHING. STOP GOING OFF DIALOGUE.")
