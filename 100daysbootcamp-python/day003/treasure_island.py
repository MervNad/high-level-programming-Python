#File: treasure_island.py
#Description: a text-based adventure game
#Functions used: print(), input(), ==, or, and
#Skills learned: if-else statement, boolean expressions, type conversion, arithmetic operators

print("Welcome to Treasure Island.")   
print("Your mission is to find the treasure.")
choice1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?: ").lower()
        if choice3 == "red":
            print("You are burned by fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You are eaten by beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You are attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
# End of file