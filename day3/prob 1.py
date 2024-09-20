'''Problem 1
Print the following pattern
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

Observe how the nunmbers in the triangle are calculated. 
Do it in two steps. Work on the generating the numbers first in right angle triangle
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

And then work on the final output using proper indendation'''


rows = int(input("Enter the number of rows: "))
def right_triangle():
     for i in range(rows):
          current_value = 1
          for j in range(i+1):
               print(current_value, end=" ")
               current_value = current_value * (i - j) // (j + 1)
          print()
right_triangle()
def space_trianle():
     for i in range(rows):
          current_value = 1
          for j in range(0,rows):
               print("*"*(rows+i))
               
space_trianle()