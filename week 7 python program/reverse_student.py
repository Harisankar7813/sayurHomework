student=[]
no_of_students = int(input("Enter the number of students:"))
for name in range(no_of_students):
    student.append(input("Enter the student name:"))
    print(name)
rev_student = student[::-1]
print(rev_student)
class_mark=[]
for marks in range(len(rev_student)):
    class_mark.append(int(input("Enter the marks of students:")))
total_mark=sum(class_mark)
print("Total marks:",total_mark)
average=total_mark/len(rev_student)
print("Average mark is:",average)

