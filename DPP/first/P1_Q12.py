count = int(input("enter the total length of the list:- ")) #asking for total length to take the input
list = [] #defining a list variable

#taking list input form user using for loop
for i in range(0, count):
    element = int(input("enter the element:- "))
    list.append(element)

i = 0 #initializing the iterator for the while loop

#asking for the number user want to search in the list
find = int(input("enter the number you want to find : "))

#searching the frist occurance of number in the list using while loop. 
while i < len(list):
    if list[i] == find:
        print("found the first occurance at",i+1,"position")
        break
    i+=1
