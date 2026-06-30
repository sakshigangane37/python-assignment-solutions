def Sum(Num):
    count = 0

    for i in range(1, Num+1):
        count = count + i

    print(count)

def main():
    value = int(input("Enter a Number : "))

    Sum(value)

if __name__ == "__main__":
    main()