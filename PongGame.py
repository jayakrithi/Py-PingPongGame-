# Pong Game in Python 

#turtle is module can draw intricate shapes and is
# better for virtual represenations 

import turtle 

""" Turtle Screen is a singleton object 
    The function Screen() returns a subclass of TurtleScreen
    this function is used when turtle is used as a standalone tool 
    for doing graphics 
"""
wn = turtle.Screen() 
wn.title("Play Pong!")
wn.bgcolor("black")
wn.setup(width=800,height=600)
# Turns the turtle animation off or on
wn.tracer(0) 


# Paddle A
paddle_a = turtle.Turtle() # paddle_a is a turtle object which
                           # is from the class Turtle 
paddle_a.speed(0) #Sets the speed
paddle_a.shape("square") # sets the size 
paddle_a.color("white") # sets the colour
paddle_a.shapesize(stretch_wid = 5, stretch_len =1) # adjusts the default (20/20) size
paddle_a.penup() #object will move around the screen without drawing the pen on the screen 
paddle_a.goto(-350,0) # initial position of the object 


# Paddle B 

paddle_b = turtle.Turtle() # paddle_b is a turtle object which
                           # is from the class Turtle 
paddle_b.speed(0) #Sets the speed
paddle_b.shape("square") # sets the size 
paddle_b.color("white") # sets the colour
paddle_b.shapesize(stretch_wid = 5, stretch_len =1) # adjusts the default (20/20) size
paddle_b.penup() #object will move around the screen without drawing the pen on the screen 
paddle_b.goto(350,0) # initial position of the object 

# Ball

ball = turtle.Turtle() # ball is a turtle object which
                           # is from the class Turtle 
ball.speed(0) #Sets the speed
ball.shape("square") # sets the size 
ball.color("white") # sets the colour
ball.penup() #object will move around the screen without drawing the pen on the screen 
ball.goto(0,0) # initial position of the object 
ball.dx = 2   # this is movement of the ball diagonally 
ball.dy = -2 


# Function 
def paddle_a_up():
    y = paddle_a.ycor() #Get the cuurent y coordinate
    y +=20 # add 20 pixels to y coordinate , therefore moves up 
    paddle_a.sety(y)

# Function 
def paddle_a_down():
    y = paddle_a.ycor() #Get the cuurent y coordinate
    y -=20 # add 20 pixels to y coordinate , therefore moves up 
    paddle_a.sety(y)

# Function 
def paddle_b_up():
    y = paddle_b.ycor() #Get the cuurent y coordinate
    y +=20 # add 20 pixels to y coordinate , therefore moves up 
    paddle_b.sety(y)

# Function 
def paddle_b_down():
    y = paddle_b.ycor() #Get the cuurent y coordinate
    y -=20 # add 20 pixels to y coordinate , therefore moves up 
    paddle_b.sety(y)


#KeyBoard binding 
wn.listen() #Listen for keyboard input 
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#Main Loop 
while True:
    wn.update()
  # Move the ball 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

   # check the border

   #top border 
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1 # Reverse the direction 

   #Bottom border 
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1 # Reverse the direction 
    
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
      
    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
    
    # Paddle and ball collision 
    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1 
    
      # Paddle and ball collision 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 
    

    # Scores Pen 
    scoreboard = turtle.Turtle()
    scoreboard.speed(0)
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0,260)
    scoreboard.write("Player A : 0 PlayerB : 0", align= "center", font=("Courier",18,"normal"))
