def min_func(n):
    return min([int(input(f"Enter element {i+1}:")) for i in range(n)])
no_of_element=int(input("Enter number of element:"))
result=min_func(no_of_element)
print("Minimum element in list:",result)

def max_func(n):
    return max([int(input(f"Enter element {i+1}:")) for i in range(n)])
no_of_element=int(input("Enter number of element:"))
result=max_func(no_of_element)
print("Maximum element:",result)