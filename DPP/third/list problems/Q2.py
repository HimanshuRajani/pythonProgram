import math
number = [3, 8, 2, 10, 6]
for i in range(0,len(number)):
    if i==0 or i==math.ceil(len(number)%2) or i==len(number)-1:
        print(number[i],end=" ")
    
    
