import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Define colors
colors = ["red", "yellow", "green", "blue", "purple"]

# Function to draw rangoli design
def draw_rangoli():
    for _ in range(24):  # Repeat 24 times for a complete rangoli
        for _ in range(7):  # Draw 7 petals
            t.color(random.choice(colors))
            t.begin_fill()
            for _ in range(9):  # Draw a triangle
                t.forward(100)
                t.left(120)
            t.end_fill()
            t.left(60)  # Rotate for the next petal
        t.right(15)  # Rotate for the next iteration

# Function to move turtle to a new position
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Move turtle to starting position
move_to(0, -200)

# Draw the rangoli design
draw_rangoli()

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()
