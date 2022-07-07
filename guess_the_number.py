#RanjeetKumbhar01
import random

randno = random.randint(1, 5)

guess = 0
userguess = None
while (userguess != randno):
    userguess = int(input("Enter your guess: "))
    guess += 1
    if userguess == randno:
        print("You got it!!!!")
    else:
        if userguess < randno:
            print("You guessed wrong!! Enter larger number ")
        else:
            print("You guessed wrong!! Enter smaller number ")

print(f"You guess the number in {guess} guesses")
with open("highscore.txt", "r") as f:
    hiscore = int(f.read())
if (hiscore < guess):
    print("You broken the highest score!!!")
    with open("highscore.txt", "w") as f:
        f.write(str(guess))
