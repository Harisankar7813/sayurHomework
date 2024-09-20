def prime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                print("given nuber is not prime")
                break
        else:
                print("prime")
    else:
        print("Not a prime")
n=int(input("Enter a number:"))
prime(n)
            