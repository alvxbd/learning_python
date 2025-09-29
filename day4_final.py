import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:\n")
options = [rock, paper, scissors]
computer = random.choice(options)
if computer == rock:
    print(rock)
elif computer == paper:
    print(paper)
else:
    print(scissors)

if choice == 0 and computer == scissors:
    print("You win!")
elif choice == 0 and computer != scissors:
    print("You lose!")
if choice == 1 and computer == rock:
    print("You win!")
elif choice == 1 and computer != rock:
    print("You lose!")
if choice == 2 and computer == paper:
    print("You win!")
elif choice == 2 and computer != paper:
    print("You lose!")