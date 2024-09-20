def split_delimiter(username,delimiter):
    return username.split(delimiter)
username=input("Enter a string:")
delimiter="-"
result=split_delimiter(username,delimiter)
print("splited string:",result)