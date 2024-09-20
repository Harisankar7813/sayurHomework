def slice_func(input_string,start_index,end_index):
    return input_string[start_index:end_index]
input_string=input("Enter a string:")
start_index=int(input("Enter starting index:"))
end_index=int(input("Enter ending index:"))
result=slice_func(input_string,start_index,end_index)
print("After sliced:",result)
