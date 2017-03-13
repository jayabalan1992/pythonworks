
a,b=0,1
print(a,b,end=" ")
num=int(input("\n\nEnter the number to check if in fib?"))
while True:
    c=a+b
    print(c,end=" ")
    if c<=num:
        if c==num:
            print("\nYes! It is in the fib series")
            break
    else:
        print("\n NO! It is not in the fibonacci series")
        break
    a,b=b,c



