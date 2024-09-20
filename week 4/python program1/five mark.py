i=0
count=0
mark=int(input("Enter your mark:"))
for i in mark:
    if(mark<=35):
        print("Fail")
        break
count+=1
i+=mark
total=i/count
print("Total:",total)