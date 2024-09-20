# get turmeric powder,onion,carrot,masala powder
#cut onion,carrot,corriander
#prepare add water,fry masala items
def getincredients(gms,kg,a,b):
    print(gms,kg,a,b)
    buy_incredients= ["turmeric powder","onion","carrot","masal powder"]
    print("I have bought all the incridents needed for cooking")
    return buy_incredients

def cutincredients(getincredients):
    cut_incredients=["onion","carrot","corriander"]
    print("cut onion,carrot,corriender")
    return cut_incredients

def cookingincredients(cutincredients):
    cook_increadients = ["add water","fry masala items"]
    print("Add water boil for some time and fry the masala items in another....")
    return cook_increadients


mygetincredients=getincredients(200,25,6,100)
mycutincredients=cutincredients(mygetincredients)
cookingincredients(mycutincredients)