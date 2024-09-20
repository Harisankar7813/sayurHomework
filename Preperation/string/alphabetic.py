def alphabetic_verification(n):
    return n.isalpha()

string=input("Enter the sentence:")
if alphabetic_verification(string):
    print("the string contains only alphabetic charater")
else:
    print("the string contains non-alphabetic charater")
