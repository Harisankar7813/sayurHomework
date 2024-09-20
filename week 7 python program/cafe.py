#Create a list of food items for a cafe. Create another list with price of those items.
#Create another list with the supply of those items (how many items are available in the cafe) in the starting of the day
#Calculate the sales for the cafe. Cafe can have a maximum of 10 transactions.
food_items=['Tea', 'coffee', 'vada']
price_items=['12','20','10']
total_supply_starting_day=['30','35','40']
max_transactions = 10
total_sales = 0
for i in range(max_transactions):
    print('Current supply:', total_supply_starting_day)
    order = input('What would you like to order? ')
    qty=int(input("Enter no.of quantity needed:"))
    if order in  food_items:
        item_index = food_items.index(order)
        if total_supply_starting_day[item_index] >= qty:
            total_supply_starting_day[item_index] -= qty
            total_sales += (price_items[item_index]*qty)
            print('You ordered a', order, 'for', price_items[item_index], ', total sales: ', total_sales)
        
        else:
            print("Stock is not available")
        if total_supply_starting_day==0:
            break
