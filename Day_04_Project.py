import random

#  ROCK - PAPER - SCISSORS GAME PROJECT


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
images = [rock, paper, scissors]

choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
    print(images[choice])

computer = random.randint(0, 2)
print("Computer chose:")
print(images[computer])


if choice >= 3 or choice < 0:
    print("You choice an invalid number. You lose!")
elif choice == computer:
    print("It's a draw!")
elif choice == 0 and computer == 2:
    print("You win!")
elif computer == 0 and choice == 2:
    print("You lose!")
elif computer > choice:
    print("You lose!")
elif choice > computer:
    print("You win!")
elif choice >= 3 or choice < 0:
    print("You choice an invalid number. You lose!")

