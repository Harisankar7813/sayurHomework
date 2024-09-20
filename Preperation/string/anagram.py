def anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)

string1=input("Enter string1:")
string2=input("Enter string2:")
if anagram(string1,string2):
    print("The string are anagram")
else:
    print("The string is not a anagram")