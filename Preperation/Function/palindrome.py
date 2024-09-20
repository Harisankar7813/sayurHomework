def palindrome(n):
    reversed_number=0
    number=n
    while(n!=0):
        rem=n%10
        reversed_number=reversed_number*10+rem
        n=int(n/10)
    if(number==reversed_number):
        print("Palindrome")
    else:
        print("not")
n=int(input("Enter a number:"))
palindrome(n)

