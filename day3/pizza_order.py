#File:pizza_order.py
#Description: calculate the total bill for a pizza order
#Functions used: input(), int(), print(), *, +, >=
#Skills learned: if-else statement, boolean expressions, type conversion, arithmetic operators

bill = 0
size = input("What size pizza do you want? S, M, or L: ")
peperoni = input("Do you want peperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
if size == "S" or size == "s":
    bill = bill + 15
elif size == "M" or size == "m":
    bill = bill + 20
else: 
    bill = bill + 25

if peperoni == "Y" or peperoni == "y":
    if size == "S" or size == "s":
        bill = bill + 2
    else:
        bill = bill + 3
if cheese == "Y":
    bill = bill + 1
print ("Thannk you for your order at Python Pizza.")
print(f"Your total bill is ${bill}.")

