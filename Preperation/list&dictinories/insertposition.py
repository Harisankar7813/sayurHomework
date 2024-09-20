def insert_position(n,position,value):
    list=[int(input(f"Enter element {i+1}:")) for i in range(n)]
    list.insert(position-1,value)
    return list
no_of_elements=int(input("Enter number of elements:"))
position=int(input("Enter position:"))
value=int(input("Enter the element u want to insert:"))
result=insert_position(no_of_elements,position,value)
print("reversed list:",result)
