import hangtools as hang
import colors as c
import title
from string import ascii_lowercase
import os

os.system('mode con: cols=130 lines=30')


def menu():
    print("\n" + c.tcyan + "Press [1] to START new game")
    print(c.tcyan + "Press [0] to QUIT game")
    minput = input("> ")
    if minput == "1":
        hangman()
    elif minput == "0":
        quit()
    else:
        print("\n" + c.tred2 + "Not a valid input\n")


def hangman():
    word = hang.get_word().lower()
    hung = list(hang.graphics())
    guesses = 0
    letters = list("_" * len(word))
    guessed = [[], []]
    while True:
        print("\n" + c.bgreen + "Guessed right:" + c.tgreen + " " + c.endc + " ".join(guessed[0]))
        print(c.bred + "Guessed wrong:" + c.tred + " " + c.endc + " ".join(guessed[1]))
        print(c.tyellow + hung[guesses])
        print("\n" + c.tcyan + " ".join(letters))
        guess = input("\nGuess a letter or the word... ").lower()
        if guess == word:
            print(c.tgreen + """
                \O/
                 |
                / \\""")
            print("\n" + c.tgreen + "Congratulations! You guessed the word!\n")
            c.input_colorama(c.bgreen, "---Press ENTER to continue---")
            break
        elif guess not in ascii_lowercase or len(guess) > 1:
            print("\n" + c.tyellow + "Please, enter a single letter or the secret word\n")
            c.input_colorama(c.bcyan, "---Press ENTER to continue---")
        elif guess.upper() in guessed[0] or guess.upper() in guessed[1]:
            print("\n" + c.tyellow + "Letter already used\n")
            c.input_colorama(c.bcyan, "---Press ENTER to continue---")
        elif guess not in word:
            print("\n" + c.tred + "Wrong! Try Again!\n")
            c.input_colorama(c.bcyan, "---Press ENTER to continue---")
            guesses += 1
            guessed[1].append(guess.upper())
            if guesses == 9:
                print(c.tred + hung[guesses])
                print("\n" + c.tred + "You Died!\n")
                c.input_colorama(c.bred, "---Press ENTER to continue---")
                break
        else:
            for index, letter in enumerate(word):
                if guess == letter:
                    letters[index] = guess.upper()
            guessed[0].append(guess.upper())
            print("\n" + c.tgreen + "Right! Keep going!\n")
            c.input_colorama(c.bcyan, "---Press ENTER to continue---")
            if "_" not in letters:
                print(c.tgreen + """
                    \O/
                     |
                    / \\""")
                print("\n" + c.tgreen + "Congratulations! You guessed all the letters!\n")
                c.input_colorama(c.bgreen, "---Press ENTER to continue---")
                break


while True:
    title.title()
    menu()

# TODO livelli di difficoltà
