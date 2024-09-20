def len_words(string):
    count=1
    for i in string:
        if " " in i:
            count+=1
    return count
string=input("Enter a sentence:")
result=len_words(string)
print("Length of words in sentence:",result)