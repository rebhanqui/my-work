# guess1.py and 2.py and 4th lab included in one file here
from random import randint

numberToGuess = randint(1, 100)
guess = int(input("Please guess the number: "))

while guess != numberToGuess:
    print("Wrong")
    #guess = int(input("Please guess again: "))
    if guess < numberToGuess:
       guess = int(input("Too Low! Please guess again: ")) 

    else:
        guess = int(input("Too High! Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)