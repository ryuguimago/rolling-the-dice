#THIS IS A DICE ROLLING PROGRAM.
#prompt user input / dont forget to convert to int
# catch errors 
x = 0
anzahl = 0
while x == 0:
    try:
        anzahl = int(input("How Many Dice Do You Want To Roll? [1-6]\n"))
    except ValueError:
        print("You're only allowed to use whole numbers")
    if anzahl not in (1,2,3,4,5,6):
        print("please enter a number between 1 and 6")
    else:
        print("lets go")
        x = 1
