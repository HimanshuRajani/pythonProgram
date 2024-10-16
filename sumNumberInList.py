def sum_list(list):
    sum=0
    for i in range(0,len(list)):
        sum += int(list[i])
    return sum

list1=[20,20,50,80]
print(sum_list(list1))

# lsit=[11,15,16,13]
# print(sum(lsit))