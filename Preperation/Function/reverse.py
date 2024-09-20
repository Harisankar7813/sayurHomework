'''def reverse(string):
    reversed_string=string[::-1]
    return reversed_string
string=input("Enter a string:")
result=reverse(string)
print("Reversed string is:",result)'''

def reverse(string):
    reversed_string=""
    for i in range(len(string),0,-1):
        reversed_string+= string[i-1]
    return reversed_string
    
string=input("Enter a string:")
result=reverse(string)
print("Reversed string is:",result)