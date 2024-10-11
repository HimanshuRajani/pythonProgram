print("Mahavitran electric board")

units = int(input("Enter the unit you have used :-"))

if units<=100:
    print("your electricity bill is :- ",units,"rs")
elif units>100 and units<=200:
    print("your electrivity bill is :- ",units*5,"rs")
elif units>200:
    print("your electicity bill is :- ",units*10,"rs")
else:
    print ("enter valid input")

