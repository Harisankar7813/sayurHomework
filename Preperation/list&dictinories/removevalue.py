def removevalue(n,value):
    list=[int(input(f"Enter element {i+1}:")) for i in range(n)]
    list=[j for j in list if j != value]
    return list
no_of_elelment=int(input("Enter number of element:"))
value=int(input("Enter value you want to remove:"))
result=removevalue(no_of_elelment,value)
print("An element removed from a list by index:",result)

