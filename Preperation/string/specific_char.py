def specific_char(input_string):
    character="a"
    count=0
    for i in input_string:
        if i==character:
            count+=1
    return count
input_string=input("Enter a input string:")
result=specific_char(input_string)
print("number of times specified character occured:",result)