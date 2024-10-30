import random

the_list = []
for list in range(0, 1001):
    the_list.append(random.randrange(10, 99))

    
for n in range(len(the_list)):
    print(f"{the_list[n]}", end="  ")