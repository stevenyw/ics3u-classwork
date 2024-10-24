newinput = input("Type in anything: ")
for a in range(len(newinput)):
    if newinput[a] == ".":
        if newinput[a+1] == "x" and newinput[a+2] == "y" and newinput[a+3] == "z":
            print("False")
            break
    elif newinput[a] != "." and newinput[a] == "x" and newinput[a+1] == "y" and newinput[a+2] == "z":
        print("True")
        break