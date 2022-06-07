print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
small_pizza=15
medium_pizza=20
large_pizza=25
#small_pizza_pepperoni=2
#med_lar_pepperoni=3
cheese=1
if (size=="S"):
    price=small_pizza
elif (size=="M"):
    price=medium_pizza
else:
    price=large_pizza
if(add_pepperoni=="Y"):
    if (size=="S"):
        price=price+2
    else:
        price=price+3
if(extra_cheese=="Y"):
    price=price+1
print("Your final bill is: $"+str(price)+".")
