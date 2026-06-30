def Factorial(Num):
    factorial = 1
    for i in range(1,Num+1):
        factorial = factorial * i
        
    print(factorial)

def main():
    value = int(input("Enter a number : "))

    Factorial(value)

if __name__ == "__main__":
    main()
    
