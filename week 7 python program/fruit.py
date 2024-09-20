#Write an app for the fruit shop. The owner keeps track of the list of fruits and their supply. 
#On Monday, he has full supply of all the fruits. End of monday, he sells 50% apples, 50% of oranges, but only 10 (number) each of other fruits
#By Tuesday end, all apples are sold out, 75% of all oranges are sold out, and only 30 more of each of  other fruits.
#By Wednesday, all fruits are sold out.
#Apple costs Rs 25 per apple, Orange cost Rs 15 per orange, all the other fruits Rs 10 each.in python


fruits = {
    "apples": 100,
    "oranges": 100,
    "bananas": 50,
    "mangoes": 50,
    "kiwis": 50
}

prices = {
    "apples": 25,
    "oranges": 15,
    "bananas": 10,
    "mangoes": 10,
    "kiwis": 10
}

# Monday sales
fruits["apples"] -= 50
fruits["oranges"] -= 50
for fruit in fruits:
    if fruit != "apples" and fruit != "oranges":
        fruits[fruit] -= 10

# Tuesday saels
fruits["apples"] = 0
fruits["oranges"] = int(fruits["oranges"] * 0.25)
for fruit in fruits:
    if fruit != "apples" and fruit != "oranges":
        fruits[fruit] -= 30

# Wednesday sales
for fruit in fruits:
    fruits[fruit] = 0

# Calculate total sales
total_sales = 0
total_apple=100
total_orange=100
total_other_fruit=150

total_sales_apple = total_apple * prices["apples"]
total_sales_orange = total_orange * prices["oranges"]
total_sales_other_fruits= total_other_fruit*prices["bananas","mangoes","kiwis"]
total_sales=total_sales_apple+total_sales_orange+total_sales_other_fruits

print("Total sales: Rs", total_sales)