# some = ['i','me','myself']
# print(type(some))
# # Lists are mutable in pythom amd collection of any datatype including strig,int,float,list,dict etc.

# #to add any value at the end of the list append() function is used
# some.append('salubhai')
# print('salubhai' in some)

# #to check the lemgth of a list len() fun is used
# print(len(some))

# #to insert any value at any position insert() fun is used
# some.insert(2 , 'vivek')
# print(some)

# #to print any values between given position slice method is used i.e  some[start:stop:step]
# print(some[1:3])

# #to remove any item from the list remove() fun is used
# some.remove('vivek')
# print(some)

# mine = list(input("enter value:-"))
# print(mine)

# for i in range(0 , len(mine)):
#     mine.remove(' ')
    
# print(mine)
# table=[i*7 for i in  range(1,11)]

# # for i in range(1,11):
# #     table.append(i*7)
# print(table)

even = [x for x in range(1,11) if x%2==0]
print(even)

#to sort the list items sort() fun is used
sort1 = [20,54,10,9,56]
sort1.sort()
print(sort1)

sort1.reverse()
print(sort1)