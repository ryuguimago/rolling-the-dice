#THIS IS A DICE ROLLING PROGRAM.
#prompt user input / dont forget to convert to int
try:
    anzahl = int(input("How Many Dice Do You Want To Roll? [1-6]\n"))
except ValueError:
    print("please enter a number between 1 and 6")
    
if anzahl in (1,2,3,4,5,6):
    print("lets go")
else:
    print("please enter a number between 1 and 6")
