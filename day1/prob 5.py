'''problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students studying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks in all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.'''
avg_marks_class=[]
no_of_department=2
marks=[]
failed_students=0
failed_students_class=[]
clg_mark=[]

for i in range(no_of_department):
    dept_name=input("Enter name of the department:")
    no_of_class=int(input(f"Enter number of class in department {dept_name}:"))

    for j in range(no_of_class):
        class_name=input("Enter each class name:")
        no_of_student= int(input(f"Enter number of Students studing python in class {class_name}:"))

        for k in range(no_of_student):
            marks_input = input(f"Enter mark of {no_of_student} student:")
            marks_for_each=[int(mark) for mark in marks_input.split(',')]
            marks.extend(marks_for_each)

            if any(mark<50 for mark in marks_for_each):
                failed_students+=1
                failed_students_class.append(failed_students)

        top_3_students = sorted(marks, reverse=True)[:3]
        print(f"top 3 student of class {class_name}:{top_3_students}")

        avg_mark=sum(marks)/len(marks)
        avg_marks_class.append(avg_mark)
        print(f"Average mark of class {class_name}:{avg_mark}")
        clg_mark.extend(marks)

    top_3_class=sorted(clg_mark, reverse=True)[:3]
    print(f"top 3 class mark:{top_3_class}")

avg_mark_class=sum(avg_marks_class)/len(avg_marks_class)
print(f"Average of all combained classes:{avg_mark_class}")
#best and least failure
'''
output
Enter name of the department:CSE
Enter number of class in department CSE:2
Enter each class name:A
Enter number of Students studing python in class A:2
Enter mark of 2 student:90,98,97
Enter mark of 2 student:87,76,65
top 3 student of class A:[98, 97, 90]
Average mark of class A:85.5
Enter each class name:B
Enter number of Students studing python in class B:2
Enter mark of 2 student:55,44,33
Enter mark of 2 student:33,44,55
top 3 student of class B:[98, 97, 90]
Average mark of class B:64.75
top 3 class mark:[98, 98, 97]
Enter name of the department:ECE
Enter number of class in department ECE:1
Enter each class name:A
Enter number of Students studing python in class A:1
Enter mark of 1 student:99,66
top 3 student of class A:[99, 98, 97]
Average mark of class A:67.28571428571429
top 3 class mark:[99, 98, 98]
Average of all combained classes:72.51190476190476
'''