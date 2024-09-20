'''def odd_or_even(n):
    if n%2==0:
        print("given number is even")
    else:
        print("given number is odd")

n=int(input("Enter a number:"))
odd_or_even(n)'''

def odd_or_even(n):
    print(f"given number is","even"if n%2==0 else"odd")

n=int(input("Enter a number:"))
odd_or_even(n)
