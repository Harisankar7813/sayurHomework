def access_dict(n,value):
    dict= {input(f"Enter key {i+1}:"):input(f"Enter value {i+1}:") for i in range(n)}
    access ={key:j for key,j in dict.items() if j==value}
    return access
no_of_element=int(input("Enter number of elements:"))
value=input("Enter the value:")
result=access_dict(no_of_element,value)
print("Value you need to access:",result)