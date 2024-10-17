while True:
    print("Enter three integers.")
    int1 = int(input("Side 1: "))
    if int1 <= 0:
        print("Try again.")
        continue
        
    while True:
        int2 = int(input("Side 2: "))
        if int2 < int1:
            print("Try again.")
            continue
        
        while True:
            int3 = int(input("Side 3: "))
            if int3 < int2:
                print("Try again.")
                continue
                
            if int3 > int2  and int2 > int1:
                print("This is a right triangle")
            else:
                print("no")
                
            break
        break
    break