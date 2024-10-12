months = {"January":"31-days","February":"28-days in regualr year and 29-days in a leap year","March":"31-days","April":"30-days","May":"31-days","June":"30-days","July":"31-days","August":"31-days","September":"30-days","October":"31-days","November":"30-days","December":"31-days",}

user = input("enter the month name :")

if user == "January" or user == "january":
    print(months["January"])
elif user == "February" or user == "february":
    print(months["February"])
elif user == "March" or user == "march":
    print(months["March"])
elif user == "April" or user == "april":
    print(months["April"])
elif user == "May" or user == "may":
    print(months["May"])
elif user == "June" or user == "june":
    print(months["June"])
elif user == "July" or user == "july":
    print(months["July"])
elif user == "August" or user == "august":
    print(months["August"])
elif user == "September" or user == "september":
    print(months["September"])
elif user == "October" or user == "october":
    print(months["October"])
elif user == "November" or user == "november":
    print(months["November"])
elif user == "December" or user == "december":
    print(months["December"])
else:
    print("INVALID INPUT!!")