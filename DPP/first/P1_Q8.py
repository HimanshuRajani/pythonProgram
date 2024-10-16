print("Calculating the average of the numbers given in the list:-")

count = int(input("Enter the total count of item in your list:- "))
list = []
sum = 0

for i in range(0,count):
    item = input("enter the numbers:- ")
    list.append(item)

for i in range(0,count):
    sum += int(list[i])

print("the average of the numbers in the list is :- ",format((sum/count),".2f"))