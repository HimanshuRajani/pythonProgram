print("Congratulation!!! For buying a new bike")

rate=int(input("Enter the price at which you brought the bike:- "))

if rate>=100000:
    print("you have to pay the road tax ",rate*0.15)
elif rate>=50000 and rate<100000:
    print("you have to pay the road tax ",rate*0.10)
elif rate <50000:
    print("you have to pay the road tax ",rate*0.05)
else:
    print("Invalid price")
