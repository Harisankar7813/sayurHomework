'''Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided'''

num = int(input("Enter a number: "))
count = 0
while num >= 3:
    num /= 3
    count += 1
    print(num)

print("Final number: ", num)
print("Number of divisions: ", count)