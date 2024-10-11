print("print the even numbers between given range:-")

min = int(input("enter the number you want to start with:- "))
max = int(input("enter the number you want to end with:- "))

while  min <= max:
    if min%2==0:
        print(min)
    min+=1
