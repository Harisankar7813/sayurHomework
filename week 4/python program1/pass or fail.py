'''#Get the marks for 3 subjects from the students.
# If the mark is> than 75 in avg in any two subjects.then print pass and also print the subject where the marks is >75.
#If student scored  in 100 in any subject scored 100 it is pass. print which subject the student scored 100.
#if the above condition not met,print fail.'''

#getting input from user
mark1 = int(input("Enter student mark 1:"))
mark2 = int(input("Enter student mark 2:"))
mark3 = int(input("Enter student mark 3:"))
#using is condition to satisfy the condition
#begins
if(mark1>75 and mark2>75):
    print("passed subjects are mark1 and mark2")
elif(mark2>75 and mark3>75):
    print("passed subjects are mark2 and mark3")
elif(mark3>75 and mark1>75):
    print("passed suject are mark3 and mark1")
if((mark1>75 and mark2>75) or (mark2>75 and mark3>75) or (mark3>75 and mark1>75)):
    print("Pass")
    #using nested if to find passed subjects
    #begin
    if(mark1>75 and mark2>75):
        print("passed subjects are mark1 and mark2")
    elif(mark2>75 and mark3>75):
        print("passed subjects are mark2 and mark3")
    else:
        print("passed suject are mark3 and mark1")
        #ends
elif(mark1>60) and (mark2>60) and (mark3>60):
    print("pass")
elif(mark1==100) or (mark2==100) or (mark3==100):
    print("pass")
    #begins
    if (mark1==100):
        print("mark1")
    elif(mark2==100):
        print("mark2")
    else:
        print("mark3")
        #ends
else:
    print("Fail")
    #ends