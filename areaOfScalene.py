import math

print("Let's calculate the  area of scalene triangle:-")

s_1 = float(input("enter the length of side 1 :- "))
s_2 = float(input("enter the length of side 2 :- "))
s_3 = float(input("enter the length of side 3 :- "))

sp = (s_1+s_2+s_3)/2

value = sp*((sp-s_1)*(sp-s_2)*(sp-s_3))

print("area of scalene triangle is ", format(math.sqrt(value),".2f"))
