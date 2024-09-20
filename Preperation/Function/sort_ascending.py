def sort_ascending():
    list=[]
    n=int(input("Enter number of element in a list:"))
    for i in range(n):
        list_element=int(input(f"Enter element {i+1}:"))
        list.append(list_element)
    ascending=list.sort()
    return list,ascending

result=sort_ascending()
print("max element in list:",result)
