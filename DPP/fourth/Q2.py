def find_maximum(a, b):
    return a if a > b else b

num1,num2 = int(input("enter first number:")),int(input("enter second number:"))

print("the larger number is :",find_maximum(num1,num2))
