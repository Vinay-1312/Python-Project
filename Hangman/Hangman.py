# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:50:52 2022

@author: DELL
"""
import re
import random
import time
from nltk.corpus import words
word_list = words.words()
# prints 236736
#print(random.choice(word_list))

class Hangman:
    def getRandomWord(self,wordList):
        return random.choice(wordList)
    
    def getDasheString(self,length):
        return "_ "*length
    def checkLetterinWord(self,letter,OutputWord):
        return letter in OutputWord
    def updateDashedWord(self,dashedword,letter,outputword):
        indices = [i.start() for i in re.finditer(letter, outputword)]
        for i in indices:
            dashedword[i] = letter
        
        return " ".join(dashedword)
    
Hang = Hangman()
outputWord = Hang.getRandomWord(word_list)
print(outputWord)

guessedWord = Hang.getDasheString(len(outputWord))
counter =1

limit = 6
guessedLetters = []
while('_' in guessedWord and counter !=6):
    letter = input("Enter a letter ")
    guessWordList = guessedWord.split(" ")
    checkLetter = Hang.checkLetterinWord(letter,outputWord)
    if len(letter) != 1:
        print("please Enter only one letter at a time")
        continue 
    if letter in guessedLetters:
        print("Letter Already guessed")
        continue
    else:
        guessedLetters.append(letter)
            
    if checkLetter == True:
        guessedWord = Hang.updateDashedWord(guessWordList,letter,outputWord)
        print(guessedWord)
        print("Correct guess. " + str(limit - counter) + " Wrong guesses remaining\n")
    else:
        counter = counter +1
        print("Wrong guess. " + str(limit - counter ) + " Wrong guesses remaining\n")
    if counter == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        

    elif counter == 2 :
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
      

    elif counter == 3 :
       time.sleep(1)
       print("   _____ \n"
             "  |     | \n"
             "  |     |\n"
             "  |     | \n"
             "  |      \n"
             "  |      \n"
             "  |      \n"
             "__|__\n")
       

    elif counter == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        

    elif counter == 5:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |         \n"
              "__|__\n")
    elif counter == 6:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        
if(counter ==6):
    print("Hanged")
    
else:
    print("Passed")