"""
    Snake game in Python
        by @rishy
"""

import turtle
     # Import turtle to build window
import time
     # Import time for delay feature between movement across screen
import random
     # Import randomizer

# 0.1 second delay on program
delay = 0.1

# Score
score = 0
high_score = 0

# Screen set up
wn = turtle.Screen( )

# Title of the window
wn.title( "Slither by @rishy" )

# Color of the screen background
wn.bgcolor( "#FFC9D6" )

# Size of the window
wn.setup( width=600, height=600 )

# Screen animation which turns off screen updates
wn.tracer( 0 )

# Snake head
head = turtle.Turtle( )

# Animation speed of the head
head.speed( 0 )

# Shape of the head
head.shape( "square" )

# Color of the snake
head.color( "#697e50" )

# Set turtle to not draw anything
head.penup( )

# Position of the snake spawn
head.goto( 0,0 )

# Freeze snake in the middle at beginning
head.direction = "stop"

# Snake food
food = turtle.Turtle( )

# Animation speed of the food
food.speed( 0 )

# Shape of the food
food.shape( "circle" )

# Color of the food
food.color( "black" )

# Set turtle to not draw anything
food.penup( )

# Position of the food spawn
food.goto( 0 , 100 )


segments = [ ]

# Pen
pen = turtle.Turtle( )
pen.speed( 0 )
pen.shape( "square" )
# Text color
pen.color( "black" )
pen.penup( )
pen.hideturtle( )
pen.goto( 0 , 260 )
pen.write( "Score: 0  High Score: 0" , align = "center" , font = ( "Courier" , 24 , "normal" ) )

# WASD control functions
def go_up( ):
    # Prevent user from colliding with themselves up/down
    if head.direction != "down":
        head.direction = "up"

def go_down( ):
    if head.direction != "up":
        head.direction = "down"

def go_left( ):
    if head.direction != "right":
        head.direction = "left"

def go_right( ):
    if head.direction != "left":
        head.direction = "right"



def move( ):
    # User performs "up" command
    if head.direction == "up":
        y = head.ycor( )
        head.sety( y + 20 )

    # User performs "down" command
    if head.direction == "down":
        y = head.ycor( )
        head.sety( y - 20 )

    # User performs "left" command
    if head.direction == "left":
        x = head.xcor( )
        head.setx( x - 20 )

    # User performs "right" command
    if head.direction == "right":
        x = head.xcor( )
        head.setx( x + 20 )

"""

Keyboard bindings:

"""

# Telling the window to listen for keypresses
wn.listen( )

# WASD controls for the snake head
wn.onkeypress( go_up , "w" )
wn.onkeypress( go_down , "s" )
wn.onkeypress( go_left , "a" )
wn.onkeypress( go_right , "d" )

# End keyboard binds

# Main game loop
while True:
    wn.update( )

    # Check for a collision with the border
    if head.xcor( ) > 290 or head.xcor( ) < -290 or head.ycor( ) > 290 or head.ycor( ) < -290:
        time.sleep( 1 )
        head.goto( 0 , 0 )
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto( 1000, 1000)

        # Clear the segmenets list
        segments.clear( )

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear( )
        pen.write( "Score: {}  High Score: {} ".format( score, high_score ) , align = "center" , font = ( "Courier" , 24 , "normal" ) )

    # Check for snake head collision with food
    if head.distance( food ) < 20:
        # Move the food to a random spot on the screen
        x = random.randint( -290 , 290 )
        y = random.randint( -290 , 290 )
        food.goto( x , y )

        # Add a segment
        new_segment = turtle.Turtle( )
        new_segment.speed( 0 )
        new_segment.shape( "square" )
        new_segment.color( "#ac8bee" )
        new_segment.penup( )
        segments.append( new_segment )

        # Shorten the delay
        delay -= 0.001

        # Increase the score counter
        score += 10

        if score > high_score:
            high_score = score

        pen.clear( )
        pen.write( "Score: {}  High Score: {} ".format( score, high_score ) , align = "center" , font = ( "Courier" , 24 , "normal" ) )

    # Move the end segments first in reverse order
    for index in range( len( segments ) -1 , 0, -1 ):
        x = segments[ index - 1 ].xcor( )
        y = segments[ index - 1 ].ycor( )
        segments[ index ].goto( x , y )

    # Move segment 0 to where the head is
    if len( segments ) > 0:
        x = head.xcor( )
        y = head.ycor( )
        segments[ 0 ].goto( x , y )

    move( )

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance( head ) < 20:
            time.sleep( 1 )
            head.goto( 0, 0 )
            head.direction = "stop"
            
            # Hide the segments
            
            for segment in segments:
                segment.goto( 1000, 1000)

            # Clear the segmenets list
            segments.clear( )

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear( )
            pen.write( "Score: {}  High Score: {} ".format( score, high_score ) , align = "center" , font = ( "Courier" , 24 , "normal" ) )

    time.sleep( delay )

# Keep window open
wn.mainloop( )
