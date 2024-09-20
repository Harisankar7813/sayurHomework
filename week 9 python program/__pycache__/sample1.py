# order food
#no.of.food,type of food,price.of.food,hotelname,quantity,items...
# call friend
#no.of.friends,name,location
#function orderfood
def orderfood(type_of_food,ordered_food,price,hotel,qantity):
    print(type_of_food,ordered_food,price,hotel,qantity)
    order_food= ["food"]
    print("food have been ordered")
    return order_food
#function callfriend
def callfriends(name,location,phno):
    print(name,location,phno)
    call_friends=["friends"]
    print("friends have been invated")
    return call_friends
#add two numbers
def add(a,b):
    c=a+b
    print("Added two number")
    print(c)
    return 

#main
orderfood("indian","sambar",100,"srisakthi",1)
orderfood("indian","chicken curry",100,"srisakthi",4)
orderfood("chinese","grill",300,"srivel",2)
orderfood("chinese","chicken fried rice",80,"srisakthi",8)
callfriends("hari","madurai",90000000001)
callfriends("sankar","trichy",8000000003)
callfriends("kumar","salem",876999999999)
callfriends("siva","chennai",97888888888)
add(3,4)
