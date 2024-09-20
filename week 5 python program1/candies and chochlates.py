#you are going to ashop to buy candies and chocolates. 100g of candy is rs.50. 100g of chocolate is rs.150. you buy 100g of candy first.
#Then if you have more money left. you buy 100g of chocolate. you check again and buy candies or chocolate as you can with the money you have.
#Input is your budget, Output is the amount of candy and/or chocolate you bought.
total_amount_candy=0
total_amount_chocolate=0
candy_price100g=50
chocolate_price100g=150
count_candy=0
count_chocolate=0
count=1
budget=int(input("Enter your budget:"))
while budget>=50:
    if(count%2!=0):
        print("100g of candy",candy_price100g)
        count_candy+=1
        budget=budget-candy_price100g
        total_amount_candy+=candy_price100g
        print("Current budget:",budget)
        count+=1
        if(budget<50):
            budget=0
    elif(count%2==0):
        print("100g of chocolate",chocolate_price100g)
        count_chocolate+=1
        budget=budget-chocolate_price100g
        print("Current budget:",budget)
        total_amount_chocolate+=chocolate_price100g
        count+=1
        if(budget<150):
            budget=0