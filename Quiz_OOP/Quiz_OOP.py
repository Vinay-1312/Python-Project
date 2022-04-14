# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:19:51 2022

@author: DELL
"""

import random
from IPython import get_ipython
class Quiz:
    def __init__(self):
        self.__question_answers = {"Tiger is national Animal":True,
                                 "Larget population":True,
                                 "Great Education":False,
                                 "Corruption free":False
                                 }
        self.__score = 0
        
    def display_question(self,i):
        return list((self.__question_answers.keys()))[i]

    def checkAnswer(self,question,answer):
        answer_check = ""
        if self.__question_answers[question] == True and (answer == "True" or answer == "T" or answer == "true"):
            self.__score = self.__score + 1
            answer_check = "The answer is correct"
        elif self.__question_answers[question] == False and (answer == "False" or answer == "F" or answer == "false"):
            self.__score = self.__score + 1
            answer_check = "The answer is correct"
        else:
            answer_check = "The answer is wrong"
            
        return answer_check
    def getScore(self):
        return self.__score
            

q = Quiz()
get_ipython().magic('clear')
i=0
question_number = [0,1,2,3]
while i!=4:
    q_no = random.sample(question_number,1)
    
    question = q.display_question(q_no[0])
    answer = input(question+"? ")
    answer_check = q.checkAnswer(question,answer)
    print(answer_check)
    print("Score = {}/4".format(q.getScore()))
    i = i+1
    
print("Total score = {} ".format(q.getScore()))    