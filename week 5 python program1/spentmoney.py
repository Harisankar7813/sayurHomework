##you are going to a movie with your friends.Each of you buy a ticket and buy a snack or a drink.Each ticket is rs.200.
#popcorn small is Rs.50, Medium is Rs.100. Large is Rs.150. Coke is Rs.800. 
#What is the total cost for each person and total cost for all of your friends.
 
movie_ticket=200
small_popcorn=50
medium_popcorn=100
large_popcorn=150
coke_price=80
total_cost1=0
total_cost2=0
total_cost3=0
total_cost4=0
no_of_friends = int(input("Enter number of friends going for movie:"))
for i in range(no_of_friends):
    buy=input("What snack do you nead(snacks or drink):")
    if(buy=="snacks"):
        popcorn=input("Enter wht size of popcorn needed(small,medium,large):")
        if (popcorn=="small"):
           price=movie_ticket+small_popcorn
           total_cost1=price
           print("Total cost for per person:",total_cost1)
        elif (popcorn=="large"):
           price=movie_ticket+large_popcorn
           total_cost2=price
           print("Total cost for per person:",total_cost2)
        elif(popcorn=="medium"):
            price=movie_ticket+medium_popcorn
            total_cost3=price
            print("Total cost for per person:",total_cost3)
    elif(buy=="drink"):
        price=movie_ticket+coke_price
        total_cost4=price
        print("Total cost for per person:",total_cost4)
if((total_cost1>total_cost2)and(total_cost1>total_cost3)and(total_cost1>total_cost4)):
    print("friend1 spent the more")
elif((total_cost2>total_cost1)and(total_cost2>total_cost3)and(total_cost2>total_cost4)):
    print("friend2 spent the more")
elif((total_cost3>total_cost2)and(total_cost3>total_cost1)and(total_cost3>total_cost4)):
    print("friend3 spent the more")
total_cost=(total_cost1+total_cost2+total_cost3+total_cost4)
print("Total for all friends:",total_cost)    