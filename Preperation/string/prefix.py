def prefix_func(input):
    prefix=['im','non','pre','extra','over','anti']
    for i in prefix:
        if input.startswith(i):
            print("given input has prefix")
    else:
        print("not")
input=input("Enter a string:")
result=prefix_func(input)
