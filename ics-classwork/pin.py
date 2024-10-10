PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("INCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("PIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")