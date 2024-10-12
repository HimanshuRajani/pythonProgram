#ARMSTRONG number is a number whose sum of the cube of the individual digits is equal to the number

num_1 = int(input("Enter the number you want to check is ARMSTRONG  or not: "))
num = num_1
sum = 0
while num > 0:
    remainder = num % 10
    sum += (remainder ** 3)
    num = num // 10

if sum == num_1:
    print(num_1,"is an armstrong number ")
else:
    print(num_1,"is not an armstrong number ")