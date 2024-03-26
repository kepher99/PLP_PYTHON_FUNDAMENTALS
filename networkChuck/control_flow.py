"""if 2 > 3:
    print("Yep,it's true!!")
    print("It's still true!!")
else:
  print("Nope, not true!!")"""
  
name = input("What is your name?\n")

print("Hello " + name + ", THANK YOU so much for coming in today.")
  
#Coffee menu
menu = "Black coffee, Espresso, Latte, Cappuccino, Frappuccino\n"

#print(name + ", what would you like from our menu today? Here is what we are serving.\n\n"
#     + menu)

order = input(name + ", what would you like from our menu today? Here is what we are serving.\n\n"
     + menu)

quantity = input("How many coffees would you like?\n")

if order == "Frappucino":
  price = 500
elif order == "Black coffee":
  price = 300
elif order == "Espresso":
  price = 250
elif order == "Latte":
  price = 150
elif order == "Cappuccino":
  price = 100
else:
  print("Sorry, we don't have that here.")
  price = 0
  
print(price)


