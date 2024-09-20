'''
Problem #1
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed 
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_] 
'''
def duplicates(input):
    remove_duplicate= set(input)
    remove_duplicate_list=list(remove_duplicate)
    count_duplicates=len(input)-len(remove_duplicate)
    for i in range (count_duplicates):
        remove_duplicate_list.extend('_')
    return remove_duplicate_list
input_str=input("Enter a numbers in space:")
input_list=list(map(int,input_str.split()))
result=duplicates(input_list)
print(result)
'''
output
Enter a numbers in space:1 2 3 3 3 4 4 7 7 9
[1, 2, 3, 4, 7, 9, '_', '_', '_', '_']
'''