#Generate two random numbers. If both numbers are even, print All even. 
#If both numbers are odd, print No even. Otherwise print Some even.
# Generate two random numbers between 1 and 10
import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("All even")

# Check if both numbers are odd
elif num1 % 2 == 1 and num2 % 2 == 1:
    print("No even")
else:
    print("Some even")
