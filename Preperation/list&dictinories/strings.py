def string(n):
    return [input(f"Enter string {i+1}:") for i in range(n)]
no_of_strings=int(input("Enter number of string:"))
result=string(no_of_strings)
print("String:",result)