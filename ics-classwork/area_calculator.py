import math

def main():
    while True:
        print("What shape do you wanna choose?")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Quit")
        answer = int(input())
        if answer == 1:
            length = int(input("Length:"))
            width = int(input("Width:"))
            output = triangle(length, width)
            print(f"The area is {output}")
        if answer == 2:
            length = int(input("Length:"))
            width = int(input("Width:"))
            output = rect(length, width)
            print(f"The area is {output}")
        if answer == 3:
            length = int(input("Length:"))
            output = square(length)
            print(f"The area is {output}")
        if answer == 4:
            radius = int(input("Radius:"))
            output = circle(radius)
            print(f"The area is {output}")
        if answer == 5:  
            print("Die")
            break
def triangle(a, b):
    return (a*b)/2
def rect(a, b):
    return (a*b)
def square(a):
    return(a*a)
def circle(a):
    return(math.pi)*(a**2)
    
    

if __name__ == "__main__":
    main()
