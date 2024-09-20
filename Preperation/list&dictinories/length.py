def length(n):
    return len([int(input(f"Enter element {i+1}:")) for i in range(n)])
no_of_element=int(input("Enter number of element:"))
result=length(no_of_element)
print("Length of list:",result)