def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))
    
number=int(input("enter the number you want to find factorial:"))

print("the factorial of",number,"is:-",factorial(number))

