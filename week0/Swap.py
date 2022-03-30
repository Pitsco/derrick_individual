def swap():
    a = int(input("First Number?: "))
    b = int(input("Second Number?: "))
    if a > b:
        print(b,a)
    else:
        print(a,b)

if __name__ == "__main__":
    swap()