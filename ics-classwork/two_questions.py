# It says to use nested if statements, which I don't know what those mean so I used chatgpt and copied its definition. Sorry for not using the and or & but booleans

print("Two questions, think of an object and I'll try to guess it, I guess. I don't know anymore.")

answer1 = input("Is it an animal, vegetable, or mineral?")
answer2 = input("Is it bigger than a breadbox?")

if answer1 == 'animal':
    if answer2 == 'yes':
        print("I think it's a moose!")
    elif answer2 == 'no':
        print("I think it's a squirrel!")
        
elif answer1 == 'vegetable':
    if answer2 == 'yes':
        print("I think it's a watermelon!")
    elif answer2 == 'no':
        print("I think it's a carrot!")

elif answer1 == 'mineral':
    if answer2 == 'yes':
        print("I think it's a Camaro!")
    elif answer2 == 'no':
        print("I think it's a paper clip!")
        
else:
    print("What the heck is even that?")
