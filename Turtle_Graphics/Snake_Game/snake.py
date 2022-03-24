# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:21:07 2022

@author: DELL
"""
import random
import turtle
import time
from turtle import Turtle,Screen



def food_random_postion(food,x_range,y_range):
    
    food.hideturtle()
    xpos = random.choice(x_range)
    ypos = random.choice(y_range)
    return xpos,ypos
def move_snake_up():
    if snake.heading() != DOWN:
            snake.setheading(UP)    
def move_snake_left():

   if snake.heading() != RIGHT:
            snake.setheading(LEFT)
   
def move_snake_right():
   if snake.heading() != LEFT:
            snake.setheading(RIGHT)
   
   
def move_snake_down():
   if snake.heading() != UP:
            snake.setheading(DOWN) 

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#set up screen
screen = Screen()

screenx,screeny = turtle.screensize()
screen.bgcolor("black")

#create head of snake
snake = Turtle()
snake.shape("square")
snake.color("white")

#create scoreBoard to add score details
ScoreBoard = Turtle()
ScoreBoard.hideturtle()
ScoreBoard.penup()
ScoreBoard.goto(0,230)
ScoreBoard.color("white")

#create food of the color blue on which the snakes feeds
food = Turtle()
food.shape("circle")
food.color("blue")
food.turtlesize(0.5,0.5,0.5)
food.penup()

#list to store all sankes objects
list_turtle = [snake]
score = 0

ScoreBoard.write(f"Score: {score}", align=ALIGNMENT, font=FONT)

#range within which food can appear
x_range = range(-screenx+100,screenx - 100)
y_range = range(-screeny+100,screeny - 100)

#action to perform on partifular key is pressed
screen.onkeypress(move_snake_up,"Up")
screen.onkeypress(move_snake_left,"Left")
screen.onkeypress(move_snake_right,"Right")
screen.onkeypress(move_snake_down,"Down")
screen.listen()

#get initial postion of food
x_pos,y_pos = food_random_postion(food,x_range,y_range)

#set to 1 once the game ends
game_end = 0
while game_end==0:
    screen.update()
    #move food to random postion
    food.goto(x_pos,y_pos)
    #show food
    food.showturtle()
    #check if snake has reached the food or not
    if (snake.distance(food) < 20):
        #create new object if snake has reached the food
        new = Turtle()
        new.hideturtle()
        new.penup()
        new.shape("square")
        new.color("white")
        new.hideturtle()
        #update food position
        x_pos,y_pos = food_random_postion(food,x_range,y_range)
        #add new object to snake body list
        list_turtle.append(new)
        score = score + 1
        ScoreBoard.clear()
    
    if score == 30:
        snake.speed(10)
    if score == 60:
        snake.speed(0)
    #condition to check if snake has crossed the boundry
    if (snake.xcor() < -(screenx+100) or snake.xcor() > (screenx-100) or snake.ycor() > (screeny-50) or snake.ycor() < (-screeny+50)):
        game_end = 1

    #display all the added sanke objects from the end
    for i in range(len(list_turtle)-1,0,-1):
        x = list_turtle[i-1].xcor()
        y = list_turtle[i-1].ycor()
        list_turtle[i].goto(x,y)
        list_turtle[i].showturtle()
    snake.penup()    
    snake.forward(11)
    for i in range(len(list_turtle)-1,0,-1):
        #in case of colision with any body part then end the ga,e
        if (list_turtle[i].distance(snake)<10):
            game_end = 1
 
    #write updated score
    ScoreBoard.write(f"Score: {score}", align=ALIGNMENT, font=FONT)
    

    
if game_end == 1:
    ScoreBoard.clear()
    ScoreBoard.write(f"Game Over: {score}", align=ALIGNMENT, font=FONT)
    time.sleep(5)
    screen.exitonclick()
    
turtle.mainloop()
