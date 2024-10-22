def monthly_payment(principal,rate,years):
    payment = principal*((rate*(1+rate)**years)/(((1+rate)**years)-1))

    return payment

princ = int(input("Enter the principle amount:- "))
rate = int(input("Enter the rate :- "))
years = int(input("Enter the number of years:- "))

print("Monthly payment is:- ",int(monthly_payment(princ,rate/12,years*12)))