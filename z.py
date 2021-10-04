import random

x = random.randint(1,9)

chances = 0

print(" Guess a number between 1 and 9 ")

while chances < 5:
    guess = int(input ("Enter the number you feel it is : "))

    if guess == x :
        print ( "Congratulations!!!! You have told the number which I had chosen!!!!")
        break;


    elif guess < x :
        print ( "Choose a higher number : " )

    else :
        print ( " Choose a smaller number : " )


    chances+=1        


if not chances < 5:
    print(" Sorry you are not right")
    print (" The number was " , x )
