import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randrange(0, 101))

print("list 1:")
for m in range(len(my_list)):
    print(f"{my_list[m]}", end=" ")


largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
        
print(f"The largest number is {largest}")
    