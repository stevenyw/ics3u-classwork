theinput = input("type in anything: ")
rep = int(input("how much of the last characters do you want to repeat?"))
result = ""
length = len(theinput)
starter = length - rep
result = theinput[starter:]
newresult = result*rep

print(newresult)
    