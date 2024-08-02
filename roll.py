#THIS IS A DICE ROLLING PROGRAM.
#
import random
dice_art = {
    1: """
 _____
|     |
|  o  |
|_____|
""",
    2: """
 _____
|o    |
|     |
|____o|
""",
    3: """
 _____
|o    |
|  o  |
|____o|
""",
    4: """
 _____
|o   o|
|     |
|o___o|
""",
    5: """
 _____
|o   o|
|  o  |
|o___o|
""",
    6: """
 _____
|o   o|
|o   o|
|o___o|
"""
}

#roll_dice function
def roll_dice():
    result = random.randint(1,6)
    return result

#TUI
x = 0
anzahl = 0
while x == 0:                                                             #catch errors
    try:
        anzahl = int(input("How Many Dice Do You Want To Roll? [1-6]")) #prompt user input / convert to int
    except ValueError:
        print("You're only allowed to use whole numbers")
    if anzahl not in (1,2,3,4,5,6):
        print("please enter a number between 1 and 6")
    else:
        x = 1
# the actual rolling of the dice
values = []
for i in range(anzahl):
   pips = roll_dice()
   values.append(pips)     #saves the result in a list
for value in values:
    print(dice_art[value])
    
