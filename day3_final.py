# Treasure Island Game: https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYour're at a cross road. Where do you want to go?")
direction = input("Type 'left' or 'right'\n").lower()
if direction == "right":
    print("Fall into a hole. Game over.")
    quit()
print("You've come to a lake. There is an island in the middle.")
swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
if swim == "swim":
    print("Eaten by a shark. Game over.")
    quit()
print("You arrive at the island unharmed. There is a house with 3 doors.")
door = input("On red, one yellow and one blue. Which colour do you choose?\n").lower()
if door == "red":
    print("Burned by fire. Game over")
    quit()
elif door == "blue":
    print("Eaten by beasts. Game over.")
    quit()
elif door == "yellow":
    print("You win!")
else:
    print("Game over.")