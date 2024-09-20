'''
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)'''

def addtwolist(list1,list2):
    add=[]
    reverse_list1=list(reversed(list1))
    reverse_list2=list(reversed(list2))
    for i in range(len(reverse_list1)):
        add_list=reverse_list1[i]+reverse_list2[i]
        if add_list>=10:
            remainder = add_list % 10
            carry = add_list // 10
            add.append(remainder)
            add.append(carry)
        else:
            add.append(add_list)
    return list(reversed(add))
input_1=[1,2,3]
input_2=[5,6,7]
result=addtwolist(input_1,input_2)
print(f"answer:{result}")

'''
output
answer:[6, 8, 1, 0]'''


'''def get_input():
    str_input=input(f"Enter the numbers in space:")
    input_list=list(map(int,str_input.split()))
    return input_list
no_input=int(input("Enter number of input_list:"))
input=[get_input() for i in range(no_input)]   
result=addtwolist(*input)
print(result)'''