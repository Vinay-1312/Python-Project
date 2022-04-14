# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:11:51 2022

@author: DELL
"""
import html
import requests
import random
class QuizBrain():
    __Score =0
    data = dict()
    quetion_index_list = random.sample(range(0,50),50)
    __index = -1
    def get_data(self,URL):
       self.data = requests.get(url = URL )
       self.data = self.data.json()
    def next_question(self):
        print(self.__index)
        self.__index = self.__index + 1
        if self.__index <49:
            self.correct_Answer = self.data['results'][self.__index]['correct_answer'] 
            return html.unescape(self.data['results'][self.__index]['question'])
    def check_answer(self,ans):
        if ans == self.correct_Answer:
            self.__Score += 1
            return True
        else:
            return False
        
    def score(self):
        return self.__Score 
    def still_has_questions(self):
        if self.__index > 49:
            return False
        else:
            return True