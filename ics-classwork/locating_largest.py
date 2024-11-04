import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randrange(0, 101))

print("list 1:")
for m in range(len(my_list)):
    print(f"{my_list[m]}", end=" ")

z = 0
largest = my_list[0]

for i in range(len(my_list)):
    if my_list[i] > largest:
        z = i
        largest = my_list[z]
print(f"The largest number is {largest}")
print(f"It is at index {z}")
    