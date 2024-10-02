answer = input("Are you ready for a quiz?")
print(f"Ready or not, here we go!")
points = 0
print("Q1: What's the capital of Alaska?")
print("1. Melbourne")
print("2. Anchorage")
print("3. Juneau")
answer1 = input()

if answer1 == '3':
    print("That's correct!")
    points += 1
else:
    print("That's not correct, sorry...")
    
print("Q2: In Python, the way you get keyboard input is the keyobard_input function.")
print("1. True")
print("2. False")
answer2 = input()

if answer2 == '2':
    print("That's correct!")
    points += 1
else:
    print("That's not correct, sorry...")
    
print("Q3: What is 9 + 10?")
print("1. 19")
print("2. 109")
print("3. 21")
answer3 = input()

if answer3 == '1':
    print("That's correct!")
    points += 1
elif answer3 == '3':
    print("Wrong! Wait, why did I mark this one as correct?")
    points += 1
else:
    print("That's not correct, sorry...")

print(f"You got {points} out of 3 correct.")