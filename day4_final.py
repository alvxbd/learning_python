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
options = [rock, paper, scissors]

while True: # infinite loop - not part of day 4 lessons ctrl + c to exit
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if choice >= 3 or choice < 0:
        print("Invalid choice. You lose!")
    else:
        print("You chose: \n", options[choice])

    computer = random.randint(0, 2)
    print("Computer chose:\n", options[computer])

    if choice == computer:
        print("It's a tie!")
    elif (choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")