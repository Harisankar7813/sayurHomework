'''Problem #2
Read a passage from a file. 
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg: The king went to the forest with the wife and a servernt. The king shot a deer. 
The king went to the forest again the next day.

answer is 4 (The king, the forest, The King, the next).'''

file = open("F:\seyur homework 2\day3\passage.txt","r")
count = 0
list=[]
passage=file.read().split()
list.extend(passage)
for i in range(len(list)):
    if passage[i].lower() == "the" and passage[i+1].lower() == "the" and "a" not in passage[i+1].lower() :
        count+=1
print(f"Number of times the word 'the followed by another 'the' without 'a' is:{count}")