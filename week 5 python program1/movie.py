##you are going to a movie with your friends.Each of you buy a ticket and buy a snack or a drink.Each ticket is rs.200.
#popcorn small is Rs.50, Medium is Rs.100. Large is Rs.150. Coke is Rs.800. 
#What is the total cost for each person and total cost for all of your friends.
 
movie_ticket=200
small_popcorn=50
medium_popcorn=100
large_popcorn=150
coke_price=80
total_cost=0
no_of_friends = int(input("Enter number of friends going for movie:"))
for i in range(no_of_friends):
    buy=input("What snack do you nead(snacks or drink):")
    if(buy=="snacks"):
        popcorn=input("Enter wht size of popcorn needed(small,medium,large):")
        if (popcorn=="small"):
           price=movie_ticket+small_popcorn
           total_cost=price
           print("Total cost for per person:",total_cost)
        elif (popcorn=="large"):
           price=movie_ticket+large_popcorn
           total_cost=price
           print("Total cost for per person:",total_cost)
        elif(popcorn=="medium"):
            price=movie_ticket+medium_popcorn
            total_cost=price
            print("Total cost for per person:",total_cost)
    elif(buy=="drink"):
        price=movie_ticket+coke_price
        total_cost=price
        print("Total cost for per person:",total_cost)
total_cost*=no_of_friends
print("Total for all friends:",total_cost)    