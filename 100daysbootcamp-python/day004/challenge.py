import random

rock = '''
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ___
---'   __)__
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose?\n Type 0 for Rock \n Type 1 for Paper\n Type 2 for scissors.")
game_options = [rock,paper,scissors]
random_int = random.randint(0,2) #random integer from ranging [0,2]
computer = game_options[random_int]
p1_select = int(input("Select a number between 0 and 2: "))

if (p1_select >= 3 or p1_select < 0):
    print("You entered an invalid number, you lose!")
else:
    player1 = game_options[p1_select]

    print(f"Player choice: \n {player1}")
    print(f"Computer choice: \n {computer}")

    if (player1 == computer):
        print("It's a draw!")
    elif ((player1 == rock and computer == scissors) or (player1 == scissors and computer == paper) or (player1 == paper and computer == rock)):
        print("You wins")
    else:
        print("You lose")
