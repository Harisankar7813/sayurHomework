'''you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.'''
def mark_sheet():
    student_name= ["Hari","Sankar","Suresh","Ramesh"]
    Marks=[98,34,67,89]
    pass_mark = 50
    Passed_students=[]
    failed_students=0
    for i in range(len(student_name)):
        if Marks[i]>=pass_mark:
            Passed_students.append(f"{student_name[i]}:{Marks[i]}")
        else:
            failed_students+=1
    for j in Passed_students:
        print(j)
    
    print("no of failed Students:",failed_students)
mark_sheet()

'''output
Hari:98
Suresh:67
Ramesh:89
no of failed Students: 1
'''



