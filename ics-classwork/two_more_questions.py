print("QUESTION TIME!!!!!!!!!!!! >W<!!! Think of something and I'll try to guess it!")

question1 = input("Does it stay inside or outside?")
question2 = input("Is it a living thing?")

if question1 == "inside" and question2 == "yes":
    print("I think it's a houseplant!")
    
if question1 == "inside" and question2 == "no":
    print("I think it's a shower curtain!")
    
if question1 == "outside" and question2 == "yes":
    print("I think it's a homeless guy!")
    
if question1 == "outside" and question2 == "no":
    print("I think it's a dead homeless guy!")
    
if question1 == "both" and question2 == "yes":
    print("I think it's a rat!")

if question1 == "both" and question2 == "no":
    print("I think it's a dead rat!")
    
# I can't put an else statement here bc the instructions say i can't lol