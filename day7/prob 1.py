'''Problem 1
In the input, find the first A and last A, print all the letters between these two A.'''
'''class Remove_word:
    def remove_A(self,input_word):
        result=input_word.strip("A") 
        print(result)
        return True
remove_letter=Remove_word()
input=input("Enter a Input Word:")
remove_letter.remove_A(input)
'''
'''
output
Enter a Input Word:AnacondA
nacond
'''
'''class letter_remover:
    def remove_letter(self,input_word):
        list=[]
        for letter in input_word:
            if letter not in ['A']:
                list.append(letter)
        for i in list:
            print(i,end=" ")
        print()
        return True
Removed_letter=letter_remover()
input=input("Enter a word:")
Removed_letter.remove_letter(input)'''
'''
output
Enter a word:AhgdshdAds
h g d s h d d s
'''
class letter_remover:
    def remove_letter(self,input_word):
        first_A=input_word.find("A")
        last_A=input_word.rfind("A")
        for j in range(first_A+1,last_A):
                print(input_word[j],end="")
        return True
Removed_letter=letter_remover()
input=input("Enter a word:")
Removed_letter.remove_letter(input)
'''
output
Enter a word:hvdhAsdfAbdhAd
sdfAbdh
'''

