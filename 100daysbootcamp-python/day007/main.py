import random
from words import word_list
from art import logo, stages
print(logo)
chosen_word = random.choice(word_list)
lives = 6
display = []              
for char in chosen_word:
    display += "_"
check = True
while check:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed this letter.")
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        print(f"The guessed letter {guess} is not in the word you are looking. You lose a life!")
        lives -= 1
        if lives == 0:
            check = False
            print("You lose!")
            print(f"The word was {chosen_word}.")
    print(f"{' '.join(display)}")
    if '_' not in display:
        check = False
        print("You win!")
        print(f"Our word is {chosen_word}.")
    print(stages[lives])