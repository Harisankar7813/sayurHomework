#assigning monthly salary for the sales man per month
monthly_salary = 30000
#getting number of phone he sells and it cost
sales = int(input("Enter how much phone he sells:"))
cost = int(input("Enter how much cost he sells in rs:"))
#using if..else for given condition given
if (cost>=15000):
    #calculating commission
    commission = monthly_salary+1000
    print("Total monthly salary after commision:",commission)
elif (cost>=40000):
    commission = monthly_salary+2000
    print("Total monthly salary after commision:",commission) 