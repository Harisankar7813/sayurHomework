'''
Problem 3:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B. 
  
  If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 
'''
class letter_remover:
    def remove_letter(self,input_word):
        first_A=input_word.find("A")
        last_A=input_word.rfind("A")
        for i in range(first_A+1,last_A):
                print(input_word[i],end="")
        if first_A!=input_word or last_A!=input_word:
            first_B=input_word.find("B")
            last_B=input_word.rfind("B")
            for j in range(first_B+1,last_B):
                print(input_word[j],end="") 
            if first_B!=input_word or last_B!=input_word:
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
Enter a word:ghfBAshbxhbBf
Ashbxhb
'''
