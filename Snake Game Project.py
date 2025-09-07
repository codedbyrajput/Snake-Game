import turtle
import time
import random

# game speed delay thing
delay = 0.1  

# score vars
score = 0
highScore = 0   

# -------- setup screen stuff --------
wn = turtle.Screen()
wn.title("Compuer Project Game")   
wn.bgcolor("red") 
wn.setup(width=600, height=600)
wn.tracer(0)   # stops the auto update

# snake head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("circle")
snakeHead.color("black")
snakeHead.penup()
snakeHead.goto(0, 1)   # not exactly centered but works
snakeHead.direction = "stop"

# food for snake
foodTurtle = turtle.Turtle()
foodTurtle.speed(0)
foodTurtle.shape("circle")
foodTurtle.color("yellow") 
foodTurtle.penup()
foodTurtle.goto(0, 100)

segments = []   # body pieces list

# the score writing pen thing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")  # doesn’t matter since it’s hidden
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# ------ functions (controls etc) ------

def go_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"

def go_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"

def go_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"

def go_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"

def move():
    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + 20)  # 20 = step size
    if snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)
    if snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)
    if snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)


# key bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# ------ main game loop ------
while True:
    wn.update()

    # check borders 
    if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() < -290:
        time.sleep(1)
        snakeHead.goto(0, 0)
        snakeHead.direction = "stop"

        # hide body pieces
        for seg in segments:
            seg.goto(9999, 9999)  # offscreen 
        segments.clear()

        # reset score
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    # check food collision
    if snakeHead.distance(foodTurtle) < 20:
        # move food somewhere random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        foodTurtle.goto(x, y)

        # add a new body square
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("grey")  # maybe make rainbow?? later
        body.penup()
        segments.append(body)

        delay -= 0.001  # faster

        # update score
        score += 10  # maybe should be +5? idk
        if score > highScore:
            highScore = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    # move body parts
    for idx in range(len(segments)-1, 0, -1):
        x = segments[idx-1].xcor()
        y = segments[idx-1].ycor()
        segments[idx].goto(x, y)

    # move first body part to head
    if len(segments) > 0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        segments[0].goto(x, y)

    move()

    # check if snake hits itself
    for seg in segments:
        if seg.distance(snakeHead) < 20:
            time.sleep(2)   # 9 was too long lol
            snakeHead.goto(0, 0)
            snakeHead.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # controls snake speed
