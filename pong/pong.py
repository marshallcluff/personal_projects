# Simple game of Pong

import turtle

win = turtle.Screen()
win.title("Pong") # change title
win.bgcolor("dim gray") # change color
win.setup(width = 800, height = 600) # change size
win.tracer(0) # need manual updates

# adding paddles and ball
# player 1 - uses wasd
player_1 = turtle.Turtle()
player_1.speed(0) # max speed
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid = 5, stretch_len= 1)
player_1.penup() # no line drawing
player_1.goto(-350, 0)

# player 2 - uses arrow keys
player_2 = turtle.Turtle()
player_2.speed(0) # max speed
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid = 5, stretch_len= 1)
player_2.penup() # no line drawing
player_2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0) # max speed
ball.shape("square")
ball.color("white")
ball.penup() # no line drawing
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# scoring
score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0    Player 2: 0", align="center", font=("courier", 24, "bold"))

score_1 = 0
score_2 = 0

# movement of player's paddles
def player_1_north():
    player_1.sety(250 if player_1.ycor() + 20 > 250 else player_1.ycor() + 20)

def player_1_south():
    player_1.sety(-250 if player_1.ycor() - 20 < -250 else player_1.ycor() - 20)

def player_2_north():
    player_2.sety(250 if player_2.ycor() + 20 > 250 else player_2.ycor() + 20)

def player_2_south():
    player_2.sety(-250 if player_2.ycor() - 20 < -250 else player_2.ycor() - 20)

# Keyboard
win.listen()
win.onkeypress(player_1_north, "w") 
win.onkeypress(player_1_south, "s")
win.onkeypress(player_2_north, "Up") 
win.onkeypress(player_2_south, "Down")

# main game
while 1:
    win.update() # update the screen

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -(ball.dy)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = -(ball.dy)

    if ball.xcor() > 390:
        score_1 += 1
        ball.goto(0,0) # back to center
        ball.dx = -(ball.dx)
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(score_1, score_2) , align="center", font=("courier", 24, "bold"))


    if ball.xcor() < -390:
        score_2 += 1
        ball.goto(0,0) # back to center
        ball.dx = -(ball.dx)
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(score_1, score_2) , align="center", font=("courier", 24, "bold"))


    # paddle collisions
    if ball.xcor() > 340 and ball.xcor() < 360 and ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() - 40:
        ball.setx(340)
        ball.dx = -(ball.dx)

    if ball.xcor() < -340 and ball.xcor() > -360 and ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() - 40:
        ball.setx(-340)
        ball.dx = -(ball.dx)

