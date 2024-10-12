print("finding the largest number in the loop")

list = [20, 10, 30, 45, 84, 9, 2]
max_num = list[0]

# finding the largest number in the list
for  i in range(0,len(list)):
    if list[i] > max_num:
        max_num = list[i]

print("The largest number in the list is: ", max_num)

print("Have A Nice Day!!!")

