pets = "monkey bat cat dog"

for n in pets.split(" "):
    print(n)
    
numbers = "65, 75, 32, 22"
numbers2 = []
for n in numbers.split(", "):
    numbers2.append(int(n))

for m in numbers2:
    print(m)
    
mystr = "one,two,three,four"
newstring = []
for n in mystr.split(","):
    newstring.append((n))
newerstring = []
for new in range(len(newstring)):
    newerstring.append((new+1))
print(newerstring)

score = "W W L T T W"
scorestring = []
for n in score.split(" "):
    if n == "W":
        scorestring.append(2)
    elif n == "L":
        scorestring.append(0)
    else:
        scorestring.append(1)
print(scorestring)

values = "x:3,x:6,x:14,x:22"
xval = []
for n in values.split(","):
    m = int(n.split(":")[1])
    xval.append(m)
print(xval)

second_values = "x:2,y:5 - x:5,y:11 - x:7,y:14"
nextvalues = []
for pair in second_values.split(" - "):
    for coord in pair.split(","):
        value = int(coord.split(":")[1])
        nextvalues.append(value)
print(nextvalues)

    

    

    
