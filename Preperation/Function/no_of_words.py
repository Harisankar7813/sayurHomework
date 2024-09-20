def no_of_words(n):
    space=" "
    count=1
    for i in n:
        if space in i:
            count+=1
    return count

n=input("Enter a sentance")
result=no_of_words(n)
print("No of words:",result)