def sum_list():
    list=[]
    n=int(input("Enter number of elements in list:"))
    for i in  range (n):
        list_element=int(input(f"Enter list element {i+1}:"))
        list.append(list_element)
    sum=0
    for j in list:
        sum+=j
    return list,sum
result=sum_list()
print("sum of element in list:",result)