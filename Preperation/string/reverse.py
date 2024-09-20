'''def reverse_func(input_string):
    return ''.join(reversed(input_string))#join used to joins the reversed character back to string
input_string=input("Enter a string:")
result=reverse_func(input_string)
print("Reversed string:",result)'''

def reverse_func(input_string):
    return input_string[::-1]
input_string=input("Enter a string:")
result=reverse_func(input_string)
print("Reversed string:",result)