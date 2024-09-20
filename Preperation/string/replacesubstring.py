def replace_substring(input_string,old_string,new_string):
    return input_string.replace(old_string,new_string)
input_string=input("Enter a input:")
old_string=input("Enter old string:")
new_string=input("Enter new string:")
result=replace_substring(input_string,old_string,new_string)
print(result)