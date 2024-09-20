'''def palindrome_string(n):
    reversed_string=n[::-1]
    if n==reversed_string:
        print("palindrome")
    else:
        print("not")
n=input("Enter a string:")
palindrome_string(n)'''

def palindrome_string(n):
    reversed_string=""
    for i in range(len(n),0,-1):
        reversed_string+=n[i-1]
    if n==reversed_string:
        print("palindrome")
    else:
        print("not")
n=input("Enter a string:")
palindrome_string(n)