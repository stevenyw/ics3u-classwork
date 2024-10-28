a = input("Type something: ")
b = input("Type something else: ")
result = ""

if len(a) > len(b):
    shorterstring = len(b)
else:
    shorterstring = len(a)

for i in range(shorterstring):
    result += a[i] + b[i]
    
if len(a) > len(b):
    result += a[shorterstring:] # learned what slice notation is :)
else:
    result += b[shorterstring:]
    

print(result)
    