def swap():
    a = int(input("Enter your first number?: "))
    b = int(input("Enter your second number?: "))
    if a > b:
        print(b,a)
    else:
        print(a,b)

if __name__ == "__main__":
    swap()