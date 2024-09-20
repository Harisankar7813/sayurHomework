'''Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0)'''

def pattern():
    num_rows = int(input("Enter the number of rows: "))

    for row in range(1, num_rows + 1):
        for col in range(row, 0, -1):
            print(col, end="")
        for col in range(2, row + 1):
            print(col, end="")
        print()
pattern()

'''
output
1
212
32123
4321234
'''





















