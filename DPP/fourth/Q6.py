def find_greater_than(lst,n):
    new_list=[]
    for i in range(0,len(lst)):
        if lst[i] > n:
            new_list.append(lst[i])
        else:
            continue
    return new_list

lst1 = [1,3,5,10,6,9,20,15,12,13,25]
num = 10

print(find_greater_than(lst1,num))
