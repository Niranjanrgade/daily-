import random

choice = input("r for Rock, p for Paper, s for Scissor: ")
choices = ['r', 'p', 's']
computer = random.choice(choices)

if choice == computer:
    print("Tie, try again!")

elif (choice == 'r' and computer == 's') or \
        (choice == 's' and computer == 'p') or \
        (choice == 'p' and computer == 'r'):
    print("You won")

else:
    print("You lost")