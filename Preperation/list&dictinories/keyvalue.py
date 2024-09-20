def key_value(n):
    return {input(f"Enter key {i+1}:"):input(f"Enter value {i+1}:") for i in range(n)}
no_of_elements=int(input("Enter number of elements:"))
result=key_value(no_of_elements)
print(f"dictionaries:{result}")