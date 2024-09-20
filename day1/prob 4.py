'''problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function'''

def same_string(str1,str2):
    if len(str1)!=len(str2):
        return False

    str1=str1+str2
    return str2 in str1

string_1 = input("Enter the first string:")
string_2=input("Enter the second string:")

ans = same_string(string_1,string_2)
print(f"{string_1} and {string_2} are same:{ans}")    

'''
output
Enter the first string:abcbca
Enter the second string:bcaabc
abcbca and bcaabc are same:True
'''
