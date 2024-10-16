num = int(input("enter the number you want to calculate factorial of:- "))
factorial = 1

while num >= 1:
    factorial = num * factorial
    num = num - 1

print(factorial)