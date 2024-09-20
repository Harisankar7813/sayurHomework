'''Same as above. Use regex.'''
import re
def valid_ip(input):
    divide=re.split(r'\.',input)
    for i in divide:
        if not re.findall("[0-9]",i):
            return False
        if not re.match(r'^\d+$', i):
            return False
        num=int(i)
        if len(i)>3:
            return False
        if not (0<=num<=255):
            return False
        if i[0]=='0':
            return False
    return True
input_ip=input("Enter a IP address:")
ip_address=valid_ip(input_ip)
if ip_address:
    print(f"{input_ip} is a valid IP address.")
else:
    print(f"{input_ip} is not a valid IP address.")