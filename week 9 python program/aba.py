'''Input string is 'aba1aaba2bab3ababa'. Find the number of times the substring aba appears 
in the input string. 
'''
a =str('aba1aaba2bab3ababa')
subset = "aba"
count = a.count(subset)
print("the count of string is:",count)