#THIS IS A DICE ROLLING PROGRAM.
#
import random

#roll function
def rolling():
    dice = random.randint(1,6)
    print(dice)             #for testing purposes 

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
        print("lets go")
        x = 1
for i in range(anzahl):
    rolling()
    
