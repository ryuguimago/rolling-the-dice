#THIS IS A DICE ROLLING PROGRAM.
#
import random
#important how to save the ascii art
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
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
final =[]
for value in values:
  final.append(dice_art[value])
print(values)
print(final)
