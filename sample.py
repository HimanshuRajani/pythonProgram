# print(1234//10)
count=0
num = 12345
for i in range(5):
    while num != 0:
        num=num%10
        count+=1
print(count)
