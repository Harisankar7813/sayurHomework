#Get two names. If the length of the two names is not equal, add 'a' at the end of the short name.
#Untill the length is equal.
name_1=input("Enter the name:")
name_2=input("Enter the  another name:")
if len(name_1)==len(name_2):
    print(name_1, name_2)
else:
    if len(name_1)<len(name_2):
        name_1+='a'*(len(name_2) - len(name_1))
        print(name_1)
    else:
        name_2+='a'*(len(name_1) - len(name_2))
        print(name_1,name_2)
