# Nothing happens when you change the name. Most likely its named "n" for simplicity of the loop.
# It will go from 0 to 4. It's pretty much the range of how much it will repeat.
# Its to add the initial number by that number until it reaches the last.
# It goes from 0 to 6.
# It goes from 3 to 8 adding up by 1.
# 

print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 21, 2):
    print(f"{n}. {message}")