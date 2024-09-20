'''def removeindex(n,index):
    list=[]
    for i in range(n):
        element=int(input(f"Enter element {i+1}:"))
        list.append(element)
    list.pop(index)
    return list
no_of_elelment=int(input("Enter number of element:"))
index=int(input("Enter index you want to remove:"))
result=removeindex(no_of_elelment,index)
print("An element removed from a list by index:",result)'''

def removeindex(n,index):
    list=[int(input(f"Enter element{i+1}:")) for i in range(n)]
    del list[index-1]
    return list
no_of_elelment=int(input("Enter number of element:"))
index=int(input("Enter index you want to remove:"))
result=removeindex(no_of_elelment,index)
print("An element removed from a list by index:",result)
