def is_even(n: int):
    if n % 2 == 0:
        return("True")
    else:
        return("False")

def main():
    while True:
        try:
            answer = int(input("Number"))
            print(is_even(answer))
            break
        except ValueError:
            print("Gimmie an integer stupid")
    
if __name__ == "__main__":
    main()