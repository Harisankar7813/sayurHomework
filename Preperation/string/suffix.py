def suffix_func(user_input):
    suffix=['y','ly','ty','ity','ry','al','er','est','age','ful','ment','ness','able']
    for i in suffix:
        if user_input.endswith(i):
            print("Given string is a suffix")

user_input=input("Enter ur string:")
result=suffix_func(user_input)


