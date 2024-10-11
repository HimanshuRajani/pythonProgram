print("lets calculate the BMI ")

weight = int(input("Enter your weight in Kgs:- "))
height = float(input("Enter your weight in meters:- "))

BMI = weight / (height*height)

if BMI < 18.5:
    print("your BMI is ", format(BMI,".2f") ,"You are underweight gain some healthy weight")
elif BMI>=18.5 and BMI<25:
    print("your BMI is ", format(BMI,".2f") ,"you are on a healthy weight keep it up!!")
elif BMI>=25 and BMI<30:
    print("your BMI is ", format(BMI,".2f") ,"you are slightly overweight loos a little weight")
else:
    print("your BMI is ", format(BMI,".2f") ,"you have to look your weight do some exercise and dieting")

print("Have a good day!")