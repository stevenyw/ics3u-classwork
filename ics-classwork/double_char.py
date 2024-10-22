newinput = input("Type in anything. ")
newerinput = ""
for n in newinput:
    if n in newinput:
        newerinput += n * 2
print(newerinput)