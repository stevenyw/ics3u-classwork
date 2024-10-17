import random
while True:
    x = random.randrange(0, 7)
    y = random.randrange(0, 7)
    
    if x != y:
        print(f"Roll 1: {x}")
        print(f"Roll 2: {y}")
        z = x + y
        print(f"The total is {z}")
    if x == y:
        print(f"Roll 1: {x}")
        print(f"Roll 2: {y}")
        z = x + y
        print(f"The total is {z}")
        break