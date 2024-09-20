#getting number of student values from user
no_of_student = int(input("Enter number of students present in class:"))
#assigning the value for total and no of mathmark in different exams
total = 0
no_of_mathmark_differentexams = 5
#using loop for number of student
for i in range(no_of_student):
    print("student number is:",(i+1))
    total_mark_one_student = int(input("Enter total mark of one student in class:"))
    #calculating average mark for total class
    total+=total_mark_one_student
    avg_mark = total/no_of_mathmark_differentexams
    avg_mark_class = avg_mark/no_of_student
    #using elif for given condition 
    if(avg_mark>90):
        print("A grade")
    elif (avg_mark>80):
        print("B grade")
    elif(avg_mark>70):
        print("C grade")
    else:
        print("D grade")
#displaying average mark for total class
print("class average:",avg_mark_class)