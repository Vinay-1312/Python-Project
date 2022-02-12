# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:40:27 2022

@author: DELL
"""
import turtle
from turtle import Turtle,Screen
import random

#get screen size x and y coordinates
screenx,screeny =turtle.screensize()
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)

timmy_the_turtle = Turtle()
#color list for dots
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

timmy_the_turtle.shape("turtle")
timmy_the_turtle.hideturtle()
timmy_the_turtle.penup()
#set the position of turtle
timmy_the_turtle.goto(-350, -screeny + 30)
timmy_the_turtle.showturtle()
timmy_the_turtle.pendown()
ypos = -200
counter = 0
#loop till top is not reached
while ypos!=screeny - 10 :
    timmy_the_turtle.pendown()
    timmy_the_turtle.dot(20,random.choice(color_list))
    timmy_the_turtle.penup() #to avoid drawing a line as turtle draws line
    timmy_the_turtle.forward(30)
    #get current poistion of turtle
    xpos,ypos = timmy_the_turtle.position()
  
 
    # if right side of screen is reached then rotate the turtle by 90 on the left side so it goes to the above row
    if xpos  == screenx - 30:
        timmy_the_turtle.left(90)
        timmy_the_turtle.pendown()
        timmy_the_turtle.dot(20,random.choice(color_list))
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(30)
       
        
        #timmy_the_turtle.hideturtle()
        #timmy_the_turtle.penup()
        xpos,ypos = timmy_the_turtle.position()
        timmy_the_turtle.right(90)
        timmy_the_turtle.hideturtle()
        timmy_the_turtle.penup()
        timmy_the_turtle.goto(-350,ypos)
        timmy_the_turtle.showturtle()
        timmy_the_turtle.pendown()

       
    if ypos>=screeny:
        break
    

 


screen = Screen()
screen.colormode(255)

screen.onscreenclick(buttonclick,1)
screen.listen() 
screen.title("Timmy_the_Turtle")

#screen.exitonclick()

"""
tess=turtle.Turtle() 
 
# self defined function to print coordinate
def buttonclick(x,y):
    print(turtle.window_height())
    print("You clicked at this coordinate({0},{1})".format(x,y))
 
 #onscreen function to send coordinate
turtle.onscreenclick(buttonclick,1)

turtle.listen()  # listen to incoming connections
turtle.speed(10) # set the speed
turtle.done()    # hold the
"""