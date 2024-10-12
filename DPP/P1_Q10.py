print("Let's bring some stars to your screen:- ")

def star_print(lev):
    for i in range(1,lev+1):
        for j in range(1,i+1):
            print("*",end="")
        print("")


num = int(input("enter the number of levels you want to print stars:- "))
star_print(num)
