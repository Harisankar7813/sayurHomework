'''
Problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]'''
 
def duplicate(input):
    input_set=set(input)
    removed_duplicate_list=list(reversed(list(input_set)))
    count_duplicates=len(input)-len(input_set)
    for i in range(count_duplicates):
        removed_duplicate_list.append('_')
    return removed_duplicate_list
user_input=input("Enter the numbers in space:")
input_list=list(map(int,user_input.split()))
result=duplicate(input_list)
print(result)
'''
output
Enter the numbers in space:1 2 3 3 3 4 4 7 7 9
[9, 7, 4, 3, 2, 1, '_', '_', '_', '_']'''