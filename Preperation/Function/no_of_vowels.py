def vowels(n):
    count=0
    vowel=["a","e","i","o","u"]
    for i in n:
        if i in vowel:
            count+=1
    return count

n=input("Enter a string:")
c=vowels(n)
print("number of vowels:",c)