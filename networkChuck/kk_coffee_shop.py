#Lets build a robot Barista!!

#Greet your customer
print("Hello, welcome KK coffee shop!!!!")

#Ask your customer their name with the input()function and store in the variable NAME.
name = input("What is your name?\n")

if name == "Ben":
  evil_status = input("Are you evil?\n")
  if evil_status == "yes":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
  else:
    print("Oh , so you are one of those good Bens. Come on in!!")
else:
  print("Hello " + name + ", THANK YOU so much for coming in today.\n\n\n")
  
  beard_length = int(input("How long is your beard?\n"))
  if beard_length >= 1:
    print("Oh , hello good sir, nice beard.You may go to the front of the line.")

print("Hello " + name + ", THANK YOU so much for coming in today.")

#Coffee menu
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