# Three phases:
# guess 
# 
import random


print("morpline hangman")
words = [
    "man",
    "computer",
    "ressurection",
    "word",
    "death",
    "window",
    "zizyphus",
    "error",
    "cubs",
    "golden",
    "banjo",
    "stars",
    "troll face!"
]
letters = {
    "q":False,
    "w":False,
    "e":False,
    "r":False,
    "t":False,
    "y":False,
    "u":False,
    "i":False,
    "o":False,
    "p":False,
    "a":False,
    "s":False,
    "d":False,
    "f":False,
    "g":False,
    "h":False,
    "j":False,
    "k":False,
    "l":False,
    "z":False,
    "x":False,
    "c":False,
    "v":False,
    "b":False,
    "n":False,
    "m":False,
}
print(f"playing with {len(words)} words")
currentWord = words[round(random.random()*(len(words)-1))]
guessed = False
guess = ""
incorrectGuesses = 0
while (not guessed and not incorrectGuesses > 5):
    string = ""
    for x in range(len(currentWord)) :
        l = currentWord[x]
        if l == " ":
            string+=l
        else:
            if(letters[l]):
                string+=l
            else:
                string+="_"
    print(f"Word : {string} Incorrect guesses: {incorrectGuesses}/6")
    guess = input("Enter a letter, or guess the word: ")
    if len(guess) == 1:
        if letters[guess] :
            print ("you already guessed that")
        else :
            if currentWord.count(guess) > 0 :
                print("correct,")
            else :
                print("incorrect")
                incorrectGuesses+=1
        letters[guess]=True
    else :
        if guess == currentWord:
            guessed=True
            print("Correct")
        else:
            incorrectGuesses+=1
            print("Incorrect")
print(f"Word was {currentWord}")
print("Game over.")
if incorrectGuesses == 6 :
    print("You lose.")
else:
    print("You win")