'''Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba


look at the output and find the pattern. Hint - add next letter in the alphabet in each row'''

def pattern():
    a='abcdefg'
    b = ""
    for i in range(7):  
        b += a[i]
        if i > 0:
            b += b[:-1]

        print(b)
pattern()

'''
output
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
'''