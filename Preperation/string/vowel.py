def vowel_func(input_string):
    vowel=['a','e','i','o','u']
    count=0
    for i in vowel:
        for j in input_string:
            if i == j:
                count+=1
    return count
input_string=input("Enter an input string:")
result=vowel_func(input_string)
print("no of vowels in string:",result)