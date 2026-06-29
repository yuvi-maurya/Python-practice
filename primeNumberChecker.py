def primeNumberChecker():
    num = int (input("Enter a number:"))
    isdivided = False

    for i in range (2 , num):
        if (num % i) == 0:
            isdivided = True
            break
    if isdivided == True:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")

primeNumberChecker()

