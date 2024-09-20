#getting number section for 10th
no_of_section = int(input("Enter number of sections:"))
#assigning value for total and student
total = 0
student = 0
#using loop for no of section
for i in range(no_of_section):
    no_of_student = int(input("Enter number of students present in class:"))
#using loop for number of student
    for i in range(no_of_student):
        total_mark_one_student = int(input("Enter total mark of one student:"))
        #calculating average mark for whole 10th
        student = no_of_student * no_of_section 
        total += total_mark_one_student
        avg_mark = total/5
        total_avg_mark = avg_mark/student
print("average for whole 10th",total_avg_mark)