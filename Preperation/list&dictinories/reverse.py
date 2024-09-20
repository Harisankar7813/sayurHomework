'''def reverse():
    list=[10,222,56,76,11]
    list.reverse()
    return list
result=reverse()
print("Reversed list:",result)'''

def reverse(n):
    list=[]
    for i in range(n):
        element=int(input(f"Enter element {i+1}:"))
        list.append(element)
    list.reverse()
    return list
no_of_elements=int(input("Enter number of elements:"))
result=reverse(no_of_elements)
print("reversed list:",result)
