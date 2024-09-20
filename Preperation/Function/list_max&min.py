def max_list():
    list=[]
    n=int(input("Enter number of element in a list:"))
    for i in range(n):
        list_element=int(input(f"Enter element {i+1}:"))
        list.append(list_element)
    maximum=max(list)
    return list,maximum
result=max_list()
print("max element in list:",result)

def min_list():
    list=[]
    n=int(input("Enter number of element in a list:"))
    for i in range(n):
        list_element=int(input(f"Enter element {i+1}:"))
        list.append(list_element)
    minimum=min(list)
    return list,minimum
result=min_list()
print("min element in list:",result)
