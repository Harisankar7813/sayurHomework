'''Program 2
Given a collection of two numbers that specify an interval, merge all overlapping intervals. 
For example, 
Input [[1,3],[2,6],[8,10],[15,20],[16,25] ]
Output [[1,6],[8,10],[15,25]].'''

def merge(a,b):
    if a[1]>=b[0]:
        return [a[0],b[1]]
    else:
        return b

input=[[1,3],[2,6],[8,10],[15,20],[16,25]]
ans_list=[]
for i in range(len(input)-1):
    first_list=input[i]
    second_list=input[i+1]
    if i>=1:
        first_list=ans_list[i-1]
    result=merge(first_list,second_list)
    ans_list.append(result)
print("Output:",ans_list)

        