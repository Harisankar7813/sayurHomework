'''
Problem #3

Same as above. But, from profit, entertainmant tax need to be subtracted. 
Tax is 5% of the cost of the ticket.
'''

class thetre_ticket():
    def vip_ticket(self,a,b):
        percent=30/100*a
        ticket = 120*b
        return percent+ticket
    def general_ticket(self,a,b):
        percent=20/100*a
        ticket=80*b
        return percent+ticket
    def matinee_ticket(self,a,b):
        percent=15/100*a
        return percent*b
    
tot_ticket=20
thetre_profit=thetre_ticket()
while tot_ticket > 0:
    price = float(input("Enter Price rs.300, 250, 150 for VIP, General and Matinee show tickets: "))
    no_of_ticket = int(input("Enter number of tickets: "))
    
    if no_of_ticket > tot_ticket:
        print("Ticket finished.")
        break
    if price==300:
        print(f"profit for VIP tickets:Rs{thetre_profit.vip_ticket(price,no_of_ticket)}")
    elif price==250:
        print(f"profit for General Tickets:Rs{thetre_profit.general_ticket(price,no_of_ticket)}")
    elif price==150:
        print(f"profit for Matinee Tickets:Rs{thetre_profit.matinee_ticket(price,no_of_ticket)}")
    else:
        print("check the price you have entered wrong price")
    tot_ticket -= no_of_ticket
class total(thetre_ticket):
    def tot_profit(self):
        vip_profit = super().vip_ticket(price, no_of_ticket)
        general_profit = super().general_ticket(price, no_of_ticket)
        matinee_profit = super().matinee_ticket(price, no_of_ticket)
        return vip_profit + general_profit + matinee_profit
tot_thetre_profit=total()
total_profit = tot_thetre_profit.tot_profit()
print(f"Total profit:Rs.{total_profit}")