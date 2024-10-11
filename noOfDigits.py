print("lets count the digits in the number:-")

number = int(input("enter the number :-"))
count = 0

while number != 0:
    number = number // 10
    count = count + 1
print("the number of digits in the number is:-", count)
