'''Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.'''
def student_marks():
    Student_names=["Hari","sankar","suresh","kumar"]
    cs_marks=[98,90,50,48]
    math_marks=[92,69,95,82]
    english_marks=[92,49,73,70]
    pass_mark = 50
    for i in range(len(Student_names)):
        if all(mark>=90 for mark in [cs_marks[i],math_marks[i],english_marks[i]]):
                print(f"{Student_names[i]} got A in all subjects")
        elif any(mark>=90 for mark in [cs_marks[i],math_marks[i],english_marks[i]]) and all(mark>=80 for mark in [cs_marks[i],math_marks[i],english_marks[i]]):
                print(f"{Student_names[i]} atleast one A and rest B")
        elif any(mark<pass_mark for mark in [cs_marks[i],math_marks[i],english_marks[i]]):
            print(f"{Student_names[i]} got fail mark")
student_marks()

'''output
Hari got A in all subjects
sankar got fail mark
kumar got fail mark 
'''