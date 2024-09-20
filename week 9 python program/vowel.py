'''Get a word from the user. If the word has any vowels, print Has vowels.
 Check if the word has Y. Then also print Has vowel. Check for vowel separately and Y separately. 
Repeat these steps until user gives a word that has Y or X in the word.'''

vowels = ['a','e','i','o','u']
while True:
    word = input("Enter a word:")
    words_lower = word.lower()

    if any (vowel in words_lower for vowel in vowels):
        print("Entered word is vowel")
    if 'y' in words_lower:
        print("entered word is vowel")
    if ('x' in words_lower) or ('y' in words_lower):
        print("terminate")
        break