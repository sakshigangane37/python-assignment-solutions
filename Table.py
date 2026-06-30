def Table(Num):
    for i in range(1, 11):
        print(Num * i, end=" ")    #end=" " : replaces this new line with a space, keeping the next output on the same line

def main():
    value = int(input("Enter a number : "))

    Table(value)

if __name__ == "__main__":
    main()


