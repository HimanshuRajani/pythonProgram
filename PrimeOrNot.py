num = int(input("Enter the number :-"))
# if num > 1:
  
#     for i in range(2, (num//2)+1):
      
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

if num==0 and  num==1:
    print(num,"is neither prime nor composite")
elif num >1:
    for i in range(2,(num//2)+1):
        if (num%i)==0:
            print(num,"is a composite number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a valid number")
        
