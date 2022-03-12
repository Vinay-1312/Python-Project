# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:11:23 2022

@author: DELL
"""

from ui import QuizInterface
from brain import QuizBrain

quiz_brain = QuizBrain()
quiz_brain.get_data("https://opentdb.com/api.php?amount=50&type=boolean")
quiz_ui = QuizInterface(quiz_brain)