import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randrange(0, 51))

print("list 1:")
for m in range(len(my_list)):
    print(f"{my_list[m]}", end=" ")


search = int(input("Which number do you wanna search?"))
e = 0
for n in range(len(my_list)):
    if search == my_list[n]:
        print(f"{search} is on the list")
        e += 1
        break
    
# Note to self: Put the last statement outside of the loop.
if e == 0:
    print(f"{search} does not appear on the list")
    

    