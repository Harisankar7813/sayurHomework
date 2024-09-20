#Get two names. If the length of the two names is not equal,add 'a' at the end of the short name
#untill the length is equall.
#same program as above.Instead of adding 'a' at the end of the short name,add the last letter.
name_1=input("Enter the name:")
name_2=input("Enter another name:")
if len(name_1)==len (name_2):
     print(name_1,name_2)
else:
     if len(name_1) < len (name_2):
          lastLtr=name_1 [-1] 
          print (lastLtr)
          name_1+=lastLtr *(len(name_2) - len(name_1))
     else:
      lastLtr=name_2[-1]
      print(lastLtr)
      name_2+=lastLtr*(len(name_1)-len(name_2))
      print(name_1,name_2)
                          
                                            