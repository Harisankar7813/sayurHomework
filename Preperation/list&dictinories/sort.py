def sort(n):
    return sorted([int(input(f"Enter elements {i+1}")) for i in range(n)])
no_of_elements=int(input(("Enter number of elements:")))
result=sort(no_of_elements)
print("Sorted list in ascending order:",result)
