def DisplayEven(Num):
    for i in range(1,Num+1):
        if i  % 2 == 0:
            print(i, end=" ")

def main():
    value = int(input("Enter a Number : "))

    DisplayEven(value)

if __name__ == "__main__":
    main()