import turtle
from turtle import Turtle,Screen
import random    

#get screen size x and y coordinates
Race_Flag = 'race-flags.gif'
screen = Screen()
screen.title("Turtle_Race")
screen.register_shape(Race_Flag)

#Get input from user
answer = turtle.simpledialog.askstring("Welcome to Turtle Race!", "Who is going to win?")

screenx,screeny =turtle.screensize() 
race_finished = 0
i = -60

#creating turtle objexts
red_Turtle = Turtle()
blue_Turtle = Turtle()
purple_Turtle = Turtle()

#creating list of turtle object and their respective colors
colors = [red_Turtle,blue_Turtle,purple_Turtle]
colos_1 = ["red","blue","purple"]

j=0
#setting property for each turtle
for Color in colors:
    col = colos_1[j]
    Color.color(col)
    Color.shape("turtle")
    Color.hideturtle()
    Color.penup()
    #set the position of turtle initially
    Color.goto(-(screenx-70), 0+i)
    Color.showturtle()
    Color.pendown()    
    i = i +30
    j = j + 1

#Add race_flag image to game
turtle = Turtle(shape=Race_Flag)
turtle.hideturtle()
turtle.penup()
turtle.turtlesize(2, 2, 2)

#add Flag image at the right side of window
turtle.goto(screenx - 90 , 200)
turtle.showturtle()  
  
while race_finished != 1:
    for obj in colors:
        if obj.xcor() >=  screenx-90:
            col = obj.color()
            race_finished = 1
            break
        else:
            random_value = random.choice(range(1,10))
            obj.penup()
            obj.forward(random_value)
            obj.showturtle()
            obj.pendown()
 
if (col[0]== answer):
    print("Won!")
else:
    print("Lost!")
    
screen.colormode(255)    
screen.exitonclick()

    
    
    
    
    
