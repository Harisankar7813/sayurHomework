'''
Problem 2:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
'''
class letter_remover:
    def remove_letter(self,input_word):
        first_A=input_word.find("A")#3or null
        last_A=input_word.rfind("A")#-2
        for i in range(first_A+1,last_A):#(4,-2)
                print(input_word[i],end="")#inbetween first A and last A
        if first_A!=input_word and last_A!=input_word:#not execute
            first_B=input_word.find("B")
            last_B=input_word.rfind("B")
            for j in range(first_B+1,last_B):
                print(input_word[j],end="") 
            if first_B!=input_word and last_B!=input_word:#not B
                first_C=input_word.find("C")
                last_C=input_word.rfind("C")
                for k in range(first_C+1,last_C):
                    print(input_word[k],end="")
        return True
Removed_letter=letter_remover()
input=input("Enter a word:")
Removed_letter.remove_letter(input)
'''
output
Enter a word:dfeCdfdfdABCsd
dfdfdAB
Enter a word:AsdsdBasdBsdAdA
sdsdBasdBsdAdasd
Enter a word:jsdhBjsBhsB
jsBhs
'''
"""class remove_word():
    def remove_letter(self,input_word):
        for index in range(len(input_word)):
            if input_word[index]=="A":
                remove=input_word.strip("A")
            elif input[index]=="B":
                remove=input_word.strip("B")
            elif input[index]=="C":
                remove=input_word.strip("C")
        print(remove)
        return True
Remove_first_last_letter=remove_word()
input=input("Enter the word:")
Remove_first_last_letter.remove_letter(input)"""
'''
output
Enter the word:AgdhdA
gdhd
Enter the word:BcfdsB
cfds
Enter the word:CdghfdjfgC
dghfdjfg
'''
'''class letter_remover:
    def remove_letter(self,input_word):
        list=[]
        for letter in input_word:
            if letter not in ['A', 'B', 'C']:
                list.append(letter)
        for i in list:
            print(i,end=" ")
        print()
        return True
Removed_letter=letter_remover()
input=input("Enter a word:")
Removed_letter.remove_letter(input)
'''