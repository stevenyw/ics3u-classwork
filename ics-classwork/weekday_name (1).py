number = input()

if number == '1':
    print("Weekday 1: Monday")
    number = "Monday"
    
elif number == "2":
    print("Weekday 2: Tuesday")
    number = "Tuesday"

elif number == "3":
    print("Weekday 3: Wednesday")
    number = "Wednesday"
    
elif number == "4":
    print("Weekday 4: Thursday")
    number = "Thursday"
elif number == "5":
    print("Weekday 5: Friday")
    number = "Friday"

elif number == "6":
    print("Weekday 6: Saturday")
    number = "Saturday"

elif number == "7" and "0":
    print(f"Weekday {number}: Sunday")
    number = "Sunday"
    
else:
    print(f"Weekday {number}: error")
    number = "error"
    

print(f"Today is {number}!")