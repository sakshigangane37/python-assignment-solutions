def DisplayOdd(Num):
    for i in range(1,Num+1):
        if i % 2 == 1:
            print(i, end=" ")

def main():
    value = int(input("Enter a Number : "))

    DisplayOdd(value)

if __name__ == "__main__":
    main()
