'''Problem #1
1. Check whether the given string input is a valid ip address.
Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
etc)
Write all constraints.
Get an input as string. Return if it is valid or not. 
Use string functions.'''

def valid_ip(input):
    #spllit the ip
    divide=input.split('.')
    
    #check >3
    for i in divide:
        #check digit
        if not i.isdigit():
            return False
        num=int(i)
        if len(i)>3:
            return False
        #check 0 to 255 numbers included
        if not 0<=num<=255:
            return False
        #check first number
        if i[0]=='0':
            return False
    return True
input_ip=input("Enter a ip address:")
ip_address=valid_ip(input_ip)
#check valid or not
if ip_address:
    print(f"{input_ip} is a valid IP")
else:
    print(f"{input_ip} not a valid IP")
