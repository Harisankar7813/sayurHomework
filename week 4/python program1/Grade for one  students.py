#getting math mark for different exams from user
exam1_math_paper = int(input("Enter the exam 1 maths mark: "))
exam2_math_paper = int(input("Enter the exam 2 maths mark: "))
exam3_math_paper = int(input("Enter the exam 3 maths mark: "))
exam4_math_paper = int(input("Enter the exam 4 maths mark: "))
exam5_math_paper = int(input("Enter the exam 5 maths mark: "))
#calculating average for one student
total = exam1_math_paper+exam2_math_paper+exam3_math_paper+exam4_math_paper+exam5_math_paper
avg = total/5
#using elif for given condition
if (avg>90):
    print("A grade")
elif (avg>80):
    print("B grade")
elif (avg>70):
    print("C grade")
else:
    print("Fails")
