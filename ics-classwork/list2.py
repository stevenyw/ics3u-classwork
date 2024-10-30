import random

the_list = []
for list in range(0, 10):
    the_list.append(random.randrange(0, 100))

for n in range(len(the_list)):
    print(f"Slot {n} contains a {the_list[n]}")

