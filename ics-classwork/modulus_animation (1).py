import time


for i in range(80):
    if i % 10 == 0:
        print("Hello, World!")
    elif i % 10 == 1:
        print("   Hello, World!")
    elif i % 10 == 2:
        print("      Hello, World!")
    elif i % 10 == 3:
        print("         Hello, World!")
    elif i % 10 == 4:
        print("             Hello, World!")
    elif i % 10 == 5:
        print("                Hello, World!")
    elif i % 10 == 6:
        print("                   Hello, World!")
    elif i % 10 == 7:
        print("               Hello, World!")
    elif i % 10 == 8:
        print("         Hello, World!")
    elif i % 10 == 9:
        print("     Hello, World!")
    elif i % 10 == 10:
        print("  Hello, World!")
    
    time.sleep(0.1)
