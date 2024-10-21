number = int(input("Put in a number. "))
total = 0
for n in list(range(1, number+1)):
    total += n
    print(n)
    print(f"The sum is {total}.")