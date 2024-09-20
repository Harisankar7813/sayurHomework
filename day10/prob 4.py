'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"] ["10","5","-","5","*"]["5","5","*"]
stack=["10","2","3"] b=3,a=2 
["10","5"] b=5,a=10
["5","5"] b=5,a=5 
output =  25"
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''
def arthematic(input_arr_str):
    stack=[]
    for i in range(len(input_arr_str)):
        if input_arr_str[i].isdigit():
            input_int=int(input_arr_str[i])
            stack.append(input_int)
        else:
            b=stack.pop()
            a=stack.pop()
            if input_arr_str[i] == '+':
                result = a + b
            elif input_arr_str[i] == '-':
                result = a - b
            elif input_arr_str[i] == '*':
                result = a * b
            elif input_arr_str[i] == '/':
                result = a / b
            stack.append(result)
            result=stack[0]
    return result
input=input("Enter numbers of input in space:")
input_arr_str=list(map(str,input.split()))
result=arthematic(input_arr_str)
print(f"output:{result}")
'''
output
Enter numbers of input in space:10 2 3 + - 5 *
output:25
'''