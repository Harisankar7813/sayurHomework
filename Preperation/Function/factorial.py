def fact(n):
    factorial=1
    for i in range(n,0,-1):
        factorial*=i
    return factorial
n=int(input("Enter a number:"))
c=fact(n)
print(f"Fcatorial of {n} is {c}")
