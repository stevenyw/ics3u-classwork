import random
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and outrun the natives.")
miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance = -20
drinks = 3
lucky = 7
done = False
while done == False:
    print("A. Drink from your canteen. ")
    print("B. Ahead moderate speed. ")
    print("C. Ahead full speed. ")
    print("D. Stop for the night. ")
    print("E. Status check. ")
    print("Q. Quit. ")
    user_choice = input()
        
    if user_choice == "Q":
        done = True

    elif user_choice == "E":
        print(f"Miles traveled: {miles_traveled}")
        print(f"Drinks in Canteen: {drinks}")
        print(f"The natives are {distance} miles behind you.")
        
    elif user_choice == "D":
        camel_tiredness = 0
        print("Your camel is happy. -w-")
        random_distance = random.randrange(7, 15)
        distance = distance + random_distance
        deathnatives = miles_traveled + distance
        if deathnatives <= 0 and not done:
            print("The natives caught up to you and they extradite you to be executed on the rope.")
            done = True
        if deathnatives > 0 and deathnatives <= 15 and not done:
            print("The natives are catching up to you!!")
        guesser = random.randrange(1, 21)   
        if guesser == lucky and not done:
            print("You found an oasis! Your thirst and camel have been reset.")
            thirst = 0
            drinks = 3
            camel_tiredness = 0
        
    elif user_choice == "C":
        random_sprint = random.randrange(10, 21)
        thirst += 1
        print(f"You ran {random_sprint} miles.")
        miles_traveled = miles_traveled + random_sprint
        random_tiredness = random.randrange(1, 4)
        random_distance = random.randrange(7, 15)
        distance = distance + random_distance
        deathnatives = miles_traveled + distance
        if deathnatives <= 0 and not done:
            print("The natives caught up to you and they extradite you to be executed on the rope.")
            done = True
        if deathnatives > 0 and deathnatives <= 15 and not done:
            print("The natives are catching up to you!!")
        camel_tiredness = camel_tiredness + random_tiredness
        guesser = random.randrange(1, 21)   
        if guesser == lucky and not done:
            print("You found an oasis! Your thirst and camel have been reset.")
            thirst = 0
            drinks = 3
            camel_tiredness = 0
        
    elif user_choice == "B":
        random_run = random.randrange(5, 13)
        miles_traveled = miles_traveled + random_run
        thirst += 1
        print(f"You ran {random_run} miles.")
        camel_tiredness += 1
        random_distance = random.randrange(7, 15)
        distance = distance + random_distance
        deathnatives = miles_traveled + distance
        if deathnatives <= 0 and not done:
            print("The natives caught up to you and they extradite you to be executed on the rope.")
            done = True
        if deathnatives > 0 and deathnatives <= 15 and not done:
            print("The natives are catching up to you!!")
        guesser = random.randrange(1, 21)   
        if guesser == lucky and not done:
            print("You found an oasis! Your thirst and camel have been reset.")
            thirst = 0
            drinks = 3
            camel_tiredness = 0
            
    elif user_choice == "A":
        if drinks > 0:
            thirst = 0
            drinks -= 1
        else:
            print("No more drinks left!")
            
    if not done and thirst > 4 and thirst < 6:
        print("You are thirsty.")
    elif not done and thirst >= 6:
        print("You died of thirst!")
        done = True
        
    if camel_tiredness > 5 and camel_tiredness < 8 and not done:
        print("Your camel is getting tired.")
    elif camel_tiredness >= 8 and not done:
        print("Your camel is dead.")
        done = True
        
    if miles_traveled >= 200 and not done:
        print("You run away with your camel. You won. GG!")
        
    
        
        
    
        
        

    