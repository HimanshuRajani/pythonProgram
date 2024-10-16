def mul(list):
    multiply=1
    for i in range(0,len(list)):
        multiply *= int(list[i])
    return multiply

list1=[30,2]
print(mul(list1))
