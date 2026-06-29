count = 9

while count >= 1:
    num = 1
    while num <= count:
        print("*", end="")
        num = num + 1
    print()
    count = count - 2
count = 1
while count <= 5:
    num = 1
    while num <= count*2 - 1 :
        print("*", end="")
        num = num + 1
    print()
    count = count + 1



count =1 
while count <= 5 :
    num = 1
    while num <= count:
        print(count , end="")
        num = num + 1
    print()
    count = count + 1

num = int(input("Enter the number of rows: "))
i = 1
while i <= num:
    j = 1
    while j <= num:
        if i== 1 or i == num or j == 1 or j == num:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1