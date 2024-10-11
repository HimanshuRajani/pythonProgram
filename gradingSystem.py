print(" Be Ready to watch your grade:-")

percentage = float(input("enter your percentage:- "))

if percentage > 80:
    print("Grade A+")
elif  percentage > 70 and percentage <= 80:
    print("Grade A")
elif   percentage > 60 and percentage <= 70:
    print("Grade B")
elif percentage > 50 and percentage < 60:
    print("Grade C")
elif percentage  > 40 and percentage <= 50:
    print("Grade D")
elif percentage >= 35 and percentage  <= 40:
    print("Grade E")
elif percentage < 35:
    print("You Are FAILED To Pass!!!!")
else:
    print("Enter the valid percentage")


print("Thanks for using the grade calculator")



