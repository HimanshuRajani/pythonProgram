# def monthly_payment(principal,rate,years):
#     payment = principal*((rate*(1+rate)**years)/(((1+rate)**years)-1))

#     return payment

# princ = int(input("Enter the principle amount:- "))
# rate = int(input("Enter the rate :- "))
# years = int(input("Enter the number of years:- "))

# print("Monthly payment is:- ",int(monthly_payment(princ,rate/12,years*12))
def monthly_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    total_payments = years * 12
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)
    return monthly_payment

principal = int(input("Enter the loan amount you want to lend :- "))
rate = int(input("the rate on which you got the principal amount :- "))
years = int(input("For hoe much years :- "))

payment = monthly_payment(principal, rate, years)
print(f"Monthly mortgage payment: {payment:.2f} rs")