def remove_whitespace(input_string):
    return input_string.strip()

user_input = input("Enter a string:")
result = remove_whitespace(user_input)
print("Whitespace removed:",result)
