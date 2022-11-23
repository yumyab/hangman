#########################################################################
#
#  Python Project - Hangman Original
#
#  File:       Project/Hangman-original.py
#  Project:    AAW-Classwork
#  Author:     Andrew Wilson (andrew.wilson@nmtafe.wa.edu.au)
#  Copyright:  © Copyright 2019, Andrew Wilson
#
#########################################################################
#
# importing modules
# import only system from os

import os
from os import system, name
# import sleep to show output for some time period
import time
# import random to generate word from txt file
import random
#
#
#########################################################################
# CONSTANTS

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAX_LIVES = 10
SCORE_AMOUNT = 10
   




##########################################################################
# INPUT FUNCTIONS

def askName():
    clearScreen()
    global playerName
    playerName = input("What is your name? ")

def askUserForSingleCharacter(options=[], prompt="Enter a character"):
    choice = ""
    if len(options) == 0:
        options = ALPHABET
    optionsList = ",".join(options)
    while options.count(choice) <= 0:
        print("Options are: " + optionsList)
        choice = input(prompt + ": ")
        if options.count(choice) <= 0:
            print("OOPS! You made an error...")
        #end if
    #end while
    return choice

##########################################################################
# UTILITY FUNCTIONS
#
# define the clear screen function
def clearScreen():
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux (here os.name is 'posix')
    else:
        _ = system('clear')
#
# Display a line of characters with end characters different if required
def displayLine(char="=", lineLength=10, endChar="*"):
    print(endChar + char * (lineLength - len(endChar) * 2) + endChar)
#
#


#The "Welcome user" statements should be converted to a function that accepts the Players name and provides playing instructions
def playerWelcome():
    displayLine("-", 80, "-")

    # Welcome the user
    print("\nHello, " + playerName, "\nTime to play Hangman!")
    print()

    # wait for 1 second
    time.sleep(1)

    print("Good luck!")
    time.sleep(0.5)
    displayLine("=", 80, "=")
    filelist()
    

#display the list of files within the working directory. Displays it as a list split into 4 columns. 
def filelist():
    #change directory to assignment folder
    path = "word-lists/"
    print("Hello, please select a text file from", path,)
    #assign list directory to a variable
    dir_list = os.listdir(path)
    # prints all files
    print("~ ~ ~ ~ ~    Files and directories in /", path, " ~ ~ ~ ~ ~ ")
     # split list into n(4) columns then print
    dirlines = [x.strip() for x in dir_list]
    n = 4
    chunks = ((dirlines[i:i+n], ", ") for i in range(0, len(dirlines), n))
    for chunk in chunks:
        # print(dir_list)
        print("~ ", *chunk, "~")
    #call next function
    start()


# ask for filename, call next function
def start():
    global userinput
    userinput = input("What's your filename?:   ")
    openPath()

# open file in path
def openPath():
    #create a global variable for user submitted filename
    global filename
    
    #addend .txt to user code
    filename = userinput + '.txt'

    #create global variable for filename within the word-lists path
    global filePath
    filePath = os.path.normcase("word-lists/{0}".format(filename))

    #print that function has run successfully and the file will be opened
    print("opening..", filePath)
    fileWrite()

# if file exists, open in 'a', otherwise create as 'w'
def fileWrite():
    if os.path.exists(filePath):
        print('File exists')
        checkSize()
    else:
        print('File does not exist. Please reenter a filename')
        start()    

#check if file is empty or not
def checkSize():
    size = os.path.getsize(filePath)
    #test if size of text file is 0kb
    if size > 0:
        print ("A secret word will be selected from the file. Good luck and have fun!")
        fileOpen()
    else:
        print ("The file is empty. Please try again.")


def fileOpen():
   
    with open(filePath, "r") as file:
        allText = file.read()

       
        word_list = list(map(str, allText.split()))
        global word
        word = random.choice(word_list).lower()
        
    gameLoop()




def gameLoop():
    
    #restore the alphabet list upon gameLoop() call
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # create a guesses variable with an empty value
    guesses = ''

    # create a variable for the score
    score = 0

    # determine the number of lives
    lives = MAX_LIVES

    # list of letters not used
    letters = ALPHABET
    
    # Create a while loop
    # check if the lives are more than zero
    while lives > 0:
        # make a counter that starts with zero
        failed = 0

        print("\nGuess the word: ", end="")
        # for every character in the secret word
        for char in word:
            # see if the character is in the players guesses
            if char in guesses:
                # print then out the character
                print(char, end="")
            else:
                # if not found, print a dash
                print("-", end="")
                # and increase the failed counter by one
                failed += 1
        #if failed is equal to zero
        # print You Won
        if failed == 0:
            print("\nYou won")
            # exit the script
            finish()
            break
      
            
            

        print("\n\n")
        # ask the user to guess a character
        guess = askUserForSingleCharacter(letters, "Enter a character")
        # add the guess to the list of characters used so far...
        guesses += guess

        # remove the guess from the list of available letters
        letters.remove(guess)

        # if the guess is not found in the secret word
        if guess not in word:
            # lives counter decreases by 1
            lives -= 1
            # print wrong
            print("Guessed Wrong!\n")
        else:
            # increase the player score
            score = score + SCORE_AMOUNT

        # how many lives are left
        print("You have", + lives, 'more guesses\n')

        # if the lives are equal to zero
        if lives == 0:
            # print "You Lose"
            print("You Lose")
            print("The word was", word)
            finish()
            break
        
def finish():
    fin = input("Play again? y/n    ")
    if fin == "y":
        playerWelcome()
    else:
        print("Goodbye " + playerName)
        quit()
        
        
       
        

#########################################################################
# THE MAIN PROGRAM
#########################################################################



clearScreen()

askName()

#run the playerWelcome function    
playerWelcome()

gameLoop()
