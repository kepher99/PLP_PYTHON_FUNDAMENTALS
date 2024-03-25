#Lets build a robot Barista!!

print("Hello, welcome KK coffee shop!!!!")

name = input("What is your name?\n")

print("Hello " + name + ", THANK YOU so much for coming in today.")

menu = "Black coffee, Espresso, Latte, Cappuccino\n"

#print(name + ", what would you like from our menu today? Here is what we are serving.\n\n"
#     + menu)

order = input(name + ", what would you like from our menu today? Here is what we are serving.\n\n"
     + menu)

price = 250

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: KSh" + str(total))

print("Sounds good " + name + " , we'll have your "+ quantity + " " + order + " ready for you in a moment.")

