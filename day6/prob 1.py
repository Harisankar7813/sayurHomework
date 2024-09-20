'''
Program #1
Write a program to check if a given string of parentheses, brackets, and braces is balanced. 
For instance, "({[]})" is balanced, but "({[)})" is not
Input - (Abc[i]) or (Abc[2])
Output true
Input ((Abc[i]) or (Abc[2])) 
Output true
Input ((Abc[i]) or Abc[2)])
Output False'''

class CheckBrackets:
    def __init__(self):
        self.bracket_list = []

    def is_balance(self, a):
        for i in a:
            if i in '(){}[]':
                self.bracket_list.append(i)
        return True

    def check_order(self):
        reversed_list = list(reversed(self.bracket_list))
        for j in range(len(self.bracket_list)):
            if self.bracket_list[j] == reversed_list[j]:
                print("True")
        
instance = CheckBrackets()
user_input = input("Enter a string of parentheses, brackets, and braces to check if balanced: ")
instance.is_balance(user_input)
instance.check_order()
