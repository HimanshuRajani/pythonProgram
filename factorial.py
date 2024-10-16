def fact(number):
    if number <= 0:
        print("number not valid")
    elif number == 1:
        return 1
    else:
        return number * fact(number - 1)
    
num = int(input("enter the number you want to calculate factorial of :- "))
print(fact(num))
