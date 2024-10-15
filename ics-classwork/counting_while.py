# n+1 increases the value of n so that it goes to print the next message until the number is bigger than 10.

print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

n = 0
while n < 10:
    print(f"{(n * 10) + 10}. {message}")
    n += 1
