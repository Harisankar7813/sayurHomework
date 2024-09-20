'''
Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"] ["5","*","5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25'''

def arthematic(input_arr_str):
    stack=[]
    def operation():
        b=stack.pop()
        a=stack.pop()
        c=stack.pop()
        if c=="+":
            result = a+b
        elif c=="-":
            result = a-b
        elif c=="*":
            result = a*b
        elif c=="/":
            result = a/b
        stack.append(result)

    for i in range(len(input_arr_str)+1):
        if input_arr_str[i] in {"+","-","*","/"}:
            stack.append(input_arr_str[i])
        elif input_arr_str[i].isdigit() and input_arr_str[i-1].isdigit():
            stack.append(int(input_arr_str[i]))
            operation()
            for j in stack:
                operation()
        elif input_arr_str[i].isdigit():
            stack.append(int(input_arr_str[i]))
    return stack
input=input("Enter numbers of input in space:")
input_arr_str=list(map(str,input.split()))
result=arthematic(input_arr_str)
print(f"output:{result}")