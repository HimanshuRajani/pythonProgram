print("lets Check the largest number")

num_1 = int(input("enter the first number :- "))
num_2 = int(input("enter the second number :- "))
num_3 = int(input("enter the third number :- "))

if num_1>num_2:
    if num_1>num_3:
        print(num_1,"is greater than ",num_2,num_3)
    elif num_1==num_3:
        print(num_1,num_3,"are equal and  greater than ",num_2)
    else:
        print(num_3,"is greater than",num_1,num_2)
else:
    if num_2>num_3:
        print(num_2,"is greater than",num_1,num_3)
    elif num_2==num_3:
        print(num_2,num_3,"are equal and  greater than ",num_1)
    else:
        print(num_3,"is greater than",num_2,num_1)