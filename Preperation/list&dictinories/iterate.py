def iterate(n):
    return [int(input(f"Enter element {i+1}:")) for _ in range(2) for i in range(n)]
no_of_element=int(input("Enter number of element:"))
result=iterate(no_of_element)
print("iterated loop of element:",result)
