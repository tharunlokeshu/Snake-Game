import turtle
import time
import random

delay = 0.3
score = 0
high_score = 0

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("white")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 100)

segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 20, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "4")
win.onkeypress(go_down, "0")
win.onkeypress(go_left, "1")
win.onkeypress(go_right, "2")

# Main game loop
while True:
    win.update()

    # Check for collision with border
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 20, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 20, "normal"))

    # Move the end segments first in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 20, "normal"))

    time.sleep(delay)
