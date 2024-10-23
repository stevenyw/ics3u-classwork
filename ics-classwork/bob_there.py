message = input("Type in a message ")
for m in range(len(message) - 2):  
    if message[m] == 'b' and message[m+2] == 'b':
        print("True")
        break
    else:
        print("False")
        break