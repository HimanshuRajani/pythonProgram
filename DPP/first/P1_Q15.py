fib_no = [0,1]
i=0

while i < 8:
    next = fib_no[i+1] + fib_no[i]
    fib_no.append(next)
    i+=1

i = 0 #reseting value of i "you can also use another iterator"
while i < len(fib_no):
    print(fib_no[i], end=",")
    i+=1