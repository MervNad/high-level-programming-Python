#File: pay_to_play_(v2.0).py
#Description: check if a player can play a game and calculate the cost  
#Functions used: input(), int(), print(), >=
#Skills learned: nested if-else statement, boolean expressions, type conversion, arithmetic operators

print("Welcome to the game.")

height=int(input("How tall are you in cm? "))
if height>=120:
    print("You are tall enough to play the game.")
    age=int(input("How old are you? "))
    if age<=5:
        print("WARNING: You lied about your height.")
        print("WARNING: This game is not for children under 6.")
    elif age<=12:
        bill = 5
        print("child ticket is $5.")
    elif age<=18:
        bill = 7
        print("teenager ticket is $7.")
    else:
        bill = 12
        print("adult ticket is $12.")
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y" or "y":
        bill += 3
        print("Photo costs $3.")
    print(f"Your total bill is ${bill}.")
else:
    print("You are too short to play the game.")
# End of file

