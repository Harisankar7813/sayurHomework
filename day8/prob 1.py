'''
Problem #1.
Write a program for calculating the profit for railways.
For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

Get the price and no of tickets sold for each class and calculate the total profit. 
Identity what calculation in the above problem can be written as a function 
and what the input and output should be.'''

class railway_ticket():
    def first_class(self,a,b):
        percent=25/100*a
        ticket = 100*b
        return percent+ticket
    def second_class(self,a,b):
        percent=15/100*a
        ticket=70*b
        return percent+ticket
    def third_class(self,a,b):
        percent=5/100*a
        return percent*b
tot_ticket=20
railway_profit=railway_ticket()
while tot_ticket > 0:
    price = float(input("Enter Price rs.300, 250, 150 for first class, second class, and third class: "))
    no_of_ticket = int(input("Enter number of tickets: "))
    
    if no_of_ticket > tot_ticket:
        print("Ticket finished.")
        break
    if price==300:
        print(f"profit for first class:Rs{railway_profit.first_class(price,no_of_ticket)}")
    elif price==250:
        print(f"profit for second class:Rs{railway_profit.second_class(price,no_of_ticket)}")
    elif price==150:
        print(f"profit for third class:Rs{railway_profit.third_class(price,no_of_ticket)}")
    else:
        print("check the price you have entered wrong price")
    tot_ticket -= no_of_ticket
class total(railway_ticket):
    def tot_profit(self):
        first_class_profit = super().first_class(price, no_of_ticket)
        second_class_profit = super().second_class(price, no_of_ticket)
        third_class_profit = super().third_class(price, no_of_ticket)
        return first_class_profit + second_class_profit + third_class_profit
tot_railway_profit=total()
total_profit = tot_railway_profit.tot_profit()
print(f"Total profit:Rs.{total_profit}")

'''
output
Enter Price rs.300, 250, 150 for first class, second class, and third class: 250
Enter number of tickets: 10
profit for second class:Rs737.5
Enter Price rs.300, 250, 150 for first class, second class, and third class: 300
Enter number of tickets: 10
profit for first class:Rs1075.0
Total profit:Rs.1970.0
'''
