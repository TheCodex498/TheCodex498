"""
Guess Me!
My second take at Python Games!
"""

from random import randint

secretNumber = randint(0, 100)

numberOfGuesses = 0
print("****************WELCOME TO GUESS ME!!****************")
print("I'm thinking of a number between 1-100, and your job is to guess it!")
print("Enter a number between 1-100")

while True:
    try:
        num = int(input())
        if num != secretNumber:
            numberOfGuesses += 1
            if num < 0 or num > 100:
                print("out of bounds")
            elif num < secretNumber - 10 or num > secretNumber + 10:
                print("COLD")
                print("Try entering a higher or lower value...")
            else:
                print("WARM")
                print("You almost have it!")
        elif num == secretNumber and numberOfGuesses == 0:
            print("WAIT")
            print("HOLD THE PHONE")
            print("YOU GUESSED IT FIRST TRY")
            print("That's a 0.01% chance!!!!")
            print("BUY A LOTTERY TICKET")
            break
        elif num == secretNumber:
            print("YAY!")
            print("The number was " + str(secretNumber))
            print("You guessed me in " + str(numberOfGuesses) + " guesses!")
            print("Congrats!!")
            break
    except ValueError:
        print("that's not a valid number")
        print("enter a number between 1-100")
        pass
