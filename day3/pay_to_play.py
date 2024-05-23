#File:pay_to_play.py
#Description: check if a player can play a game
#Functions used: input(), int(), print(), >=
#Skills learned: if-else statement, boolean expressions, type conversion

print("Welcome to the game.")

height=int(input("How tall are you in cm? "))
if height>=120:
    print("You are tall enough to play the game.")
    age=int(input("How old are you? "))
    if age<=5:
        print("WARNING: You lied about your height.")
        print("WARNING: This game is not for children under 6.")
    elif age<=12:
        print("Please pay $5.")
    elif age<=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You are too short to play the game.")
# End of file