def join_delimiter(userinput,delimiter):
    return delimiter[0].join(userinput)
userinput=input("Enter a string:")
delimiter=["good","bad"]
result=join_delimiter(userinput,delimiter)
print("joined string:",result)