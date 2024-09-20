#we have 3 collages each collage has a  diiferent cutoff mark for engineering collage admission.
#Get the 5 marks from the student.
#calculate the average.
#find out which collages the student is eligible.
# assigning cutoff for each collge  
clg1_cutoff = 93
clg2_cutoff = 87
clg3_cutoff = 97
#getting input from the user
mark1 = int(input("Enter the mark1:"))
mark2 = int(input("Enter the mark2:"))
mark3 = int(input("Enter the mark3:"))
mark4 = int(input("Enter the mark4:"))
mark5 = int(input("Enter the mark5:"))
#calculating the averge cutoff
total = mark1+mark2+mark3+mark4+mark5
cutoff = total/5
#using if condition for given conditions
if (cutoff>85) and (cutoff<95):
    print("Eligible for collage 1 and collage 2")
elif(cutoff >= 97):
    print("Eligible for collage 3")
else:
    print("He is not eligible for this top three collages,better luck next time ")