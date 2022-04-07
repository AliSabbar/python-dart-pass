def check():
    listy = []
    size = int(input("Enter X Value : "))
    if size > 0 and size <= 10:
        for i in range(size):
            number = int(input())
            listy.append(number)
    else:
        print("Enter Number Between 1 and 10")

    for i in listy:
            if i % 2 == 0:
                print(i,"is even")
            else:
                print(i,"is odd")
# main
check()
    