PIN = "12345"
tries = 0
max_lockout = 4

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and max_lockout < 4:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= max_lockout:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")