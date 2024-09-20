def palindrome_string(n):
    reversed_string=n[::-1]
    if n==reversed_string:
        print("Palindrome")
    else:
        print("not")
n=input("Enter a string:")
result=palindrome_string(n)


