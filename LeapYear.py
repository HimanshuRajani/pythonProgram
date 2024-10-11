print("letts check the year is leap year or not")

year = int(input("Enter the year : "))

if year%4==0:
    if year%400==0:
        print("The year is the LEAP year")
    else:
        print("The year is not the LEAP year")
else:
    print("The year is not the LEAP year")
