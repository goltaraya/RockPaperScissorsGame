# Day 4 
# Rock, Paper or Scissors game
# Author: Yago Alexandre Goltara Affonso

import random
import time

# Greetings
print("Welcome to my Rock, Paper or Scissors game. Let's see if you can beat me.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get the user's choice
choice = int(input("First of all, choose your weapon:\n0 - Rock\n1 - Paper\n2 - Scissors\n>>> "))

# Get the bot's choice
botsChoice = random.randint(0,2)

# Validation of user's choice
if choice<=2 and choice>=0:
  
    # Print out the user's choice 
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)

    # Print out the bot's choice
    if botsChoice == 0:
        print(rock)
    elif botsChoice == 1:
        print(paper)
    else:
        print(scissors)

    # Compare each choice and choose the beginner... or not, in case of DRAW
    if choice == botsChoice:
        print("Draw! Let's play again.")
    elif (choice == 0) and (botsChoice == 2):
        print("You win!")
    elif (choice == 1) and (botsChoice == 0):
        print("You win!")
    elif (choice == 2) and (botsChoice == 1):
        print("You win!")
    else:
        print("HAHA I win!")
else:
    print("Please, restart the game and write a valid number.")

time.sleep(4)