newinput = input("Type in anything: ")
newerinput = input("Type in another thing: ")

a = len(newinput)
b = len(newerinput)
if newinput[a - 1] == newerinput[b - 1]:
    print("True")
else:
    print("False")