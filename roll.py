#THIS IS A DICE ROLLING PROGRAM.
#
import random
#ascii art in dictionary
dice_art = {
    1: [
        " _____ ",
        "|     |",
        "|  o  |",
        "|_____|"
    ],
    2: [
        " _____ ",
        "|o    |",
        "|     |",
        "|____o|"
    ],
    3: [
        " _____ ",
        "|o    |",
        "|  o  |",
        "|____o|"
    ],
    4: [
        " _____ ",
        "|o   o|",
        "|     |",
        "|o___o|"
    ],
    5: [
        " _____ ",
        "|o   o|",
        "|  o  |",
        "|o___o|"
    ],
    6: [
        " _____ ",
        "|o   o|",
        "|o   o|",
        "|o___o|"
    ]
}

#roll_dice function
def roll_dice():
    return random.randint(1,6)
   

#TUI function for user input
def user_input():
    while True:                                                             
        try:
            anzahl = int(input("How Many Dice Do You Want To Roll? [1-6]")) #prompt user input / convert to int
            if anzahl in range(1,7):
                return anzahl
            else:                                                           #catch wrong numbers
                print("Please enter a number between 1 and 6")
        except ValueError:                                                  #catch ValueError
            print("You're only allowed to use whole numbers")

# Function to print the dice faces
def print_dice(values):
    for line in range(4):  # There are 4 lines in each dice ASCII art
        for value in values:
            print(dice_art[value][line], end=" ")   #goes through the lines and prints them side by side
        print()
def main():
    anzahl = user_input()
    values = [roll_dice() for i in range(anzahl)]         # a whole for loop in one line. calls roll_dice function multiple times and stores output in values[]
    print_dice(values)

if __name__ == "__main__":
    main()