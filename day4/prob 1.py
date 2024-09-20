'''Problem #1
write a program that reads a passage and reverses the order of 
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS'''

def reverse():
    list=[]
    passage=input("Enter the passage:")
    list.extend(passage.split())
    for i in list:
        reversed_string = i[::-1]
        print(reversed_string,end=" ")
reverse()
'''
output
Enter the passage:I am sayur
I ma ruyas 
'''
'''I, am, sayur'''
def reverse_comma():
    list=[]
    passage=input("Enter the passage:")
    list.extend(passage.split())
    for i in list:
        add_comma=i+", "
        print(add_comma.strip(),end=" ")
reverse_comma()