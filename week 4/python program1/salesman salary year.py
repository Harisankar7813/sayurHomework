#getting number of months
no_of_months = int(input("Enter the number of months:"))
#getting number of phone the salesman sells
no_ph_sell = int(input("Enter number of phone he sells:"))
#assigning total 
total = 0
#using loop for no_of_months
for i in range(no_of_months):
    print("month is:",(i+1))
    total_monthly_salary =int(input("Enter monthly salary:"))
    total+=total_monthly_salary
    print(total)
#declaring if..else for given condition 
if (no_of_months==12) and (no_ph_sell>=20):
    print("year salary",total+5000)
else:
    print("Sorry,Give your best next time")