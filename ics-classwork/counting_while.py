print("Type a message, and it'll display it 5 times.")
message = input("Message: ")

n = 0
while n < 5:
    print(f"{n + 1}. {message}")
    n += 1