

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure")

direction = input("Left or Right/L or R\n").lower()
if direction != "left"  and direction != "l":
    print("Fall into a hole.")
    print("Game Over.")
else:
    swim_wait = input("Swim or Wait\n").lower()
    if swim_wait != "wait" and swim_wait != "w":
        print("Attacked by trout.")
        print("Game Over.")
    else:
        door = input("Choose one door, Red, Yellow or Blue.\n").lower()
        if door ==  "yellow" or door == "y":
            print("You Win!")
        else:
            if door ==  "blue"  or door == "b":
                print("Eaten by beasts.\nGame Over.")
            elif door ==  "red" or door == "r":
                print("Burned by fire\nGame Over.")
            else:
                 print("Game Over.")
   