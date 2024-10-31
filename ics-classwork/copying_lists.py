# What it does is that it just copies the entire string, and not the list, and also keeps the -7 at the end.

import random

the_list = []
for list in range(0, 10):
    the_list.append(random.randrange(1, 101))

for i in range(len(the_list)):
    last_letter = the_list[i]
    
the_list.pop()
the_list.append(-7)

print("List 1:")   
for n in range(len(the_list)):
    print(f"{the_list[n]}", end="  ")

print()
print("List 2:")
for m in range(len(the_list)):
    print(f"{the_list[m]}", end="  ")
    the_list.pop()
    the_list.append(last_letter)