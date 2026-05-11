import turtle
import random

# Setting up the window. I chose a black background so the colors
# from my palette stand out.
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("My Generative Art Project")

# I'm naming my turtle 't' to keep the code clean.
# Setting speed to 0 because I noticed it takes too long to draw otherwise.
t = turtle.Turtle()
t.speed(0)
t.width(2)

# I researched hex codes to create a neon colour palette.
# I put these in a list so I can pick them randomly later.
colors = ["#FF007F", "#7000FF", "#00FFE7", "#FFD700", "#FF5733"]


# I wanted to do a geometric artwork similar to what I have seen already in
# tech and media art class, f.ex. Frieder Nake: Walk through Raster and
# in the last exercise in Tech Basics 1 : Schotter', 1968-1970, from Georg Nees.

def draw_square(size):
    """
    I made this function because I'll be drawing a lot of squares
    and I didn't want to rewrite the 4-step loop every single time.
    """
    for i in range(4):
        t.forward(size)
        t.left(90)


# I'm calculating these coordinates so the grid starts in the top-left
# instead of the middle of the screen.
start_x = -250
start_y = 200
gap = 50

# --- THE ART LOGIC ---

# NESTED LOOPS: This is how I'm building the grid.
# The 'row' loop moves us down, and the 'col' loop moves us across.
for row in range(10):
    for col in range(10):

        # I used penup() here so the turtle 'jumps' to the next
        # grid coordinate without leaving a messy line behind it.
        t.penup()
        current_x = start_x + (col * gap)
        current_y = start_y - (row * gap)
        t.goto(current_x, current_y)
        t.pendown()

        # RANDOM + LIST: Instead of picking one color, I'm telling Python
        # to grab a random item from my 'colors' list for every shape.
        chosen_color = random.choice(colors)
        t.color(chosen_color)

        # CONDITIONALS: I wanted to make the art feel less "perfect."
        # I generate a random number from 1 to 10 to decide what happens next.
        chance = random.randint(1, 10)

        if chance > 8:
            # If the number is 9 or 10, draw a circle to break the pattern.
            t.circle(gap / 4)
        elif chance == 1:
            # If the number is 1, I use 'pass' so it skips this spot.
            # This creates some "negative space" in the mosaic.
            pass
        else:
            # Most of the time, it draws a square.
            # I added another random bit here so the sizes vary slightly.
            square_size = random.randint(15, 45)
            draw_square(square_size)

# This hides the turtle arrow and keeps the window open so you can see the art.
t.hideturtle()
screen.mainloop()
