students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('David', 92)]

dict={x:y for (x,y) in students}
print(dict)

for i in dict:
    if dict[i]>=80:
        print(i)
