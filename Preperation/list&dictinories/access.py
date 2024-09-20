def access_func(n,index):
    list=[int(input(f"Enter element {i+1}:")) for i in range(n)]
    access=list[index-1]
    return access
no_of_element=int(input("Enter number of element:"))
index=int(input("Enter the element you want to index:"))
result=access_func(no_of_element,index)
print("Element we accessed:",result)