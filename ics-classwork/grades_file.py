import random
name = input("Whats your first name?")
name2 = input("Whats your last name?")
n=0


print(f"First name: {name}")
print(f"First name: {name2}")
print(f"Filename: marks.txt")
print("Here are your randomly selected grades. Sorry if you fail, not my problem >w<")
list = []
for i in range(0, 5):
    list.append(random.randrange(0, 101))
for m in range(len(list)):
    n+=1
    print(f"Grade {n}: {list[m]}")
    
print("Data saved in marks.txt")