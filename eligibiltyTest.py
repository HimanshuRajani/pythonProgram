print("are you eligible??")

age = int(input("Enter your age :- "))

if age>=18 and age<=100:
    print("congratulations!!! You can vote")
elif age>=1 and age<18:
    print("sorry!!! You are not")
else:
    print("enter valid age ")