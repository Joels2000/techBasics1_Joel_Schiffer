import random
import turtle

BG_COLOR = "black"
COLORS = ["#FF007F", "#7000FF", "#00FFE7", "#FFD700", "#FF5733"]
ROWS = 10
COLS = 10
START_X = -250
START_Y = 200
GAP = 50


def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)


# My function that takes arguments and returns a value
# I struggled with this because the turtle kept drawing lines when moving,
# so I had to put the penup and pendown inside here to fix it.
def draw_random_shape(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    random_color = random.choice(COLORS)
    t.color(random_color)

    chance = random.randint(1, 10)

    # figuring out what to return was hard, so I'm returning a string
    # to show what actually got drawn at this spot
    if chance > 8:
        t.circle(12.5)  # GAP / 4 is 12.5, just hardcoded it to be safe
        return "circle"
    elif chance == 1:
        return "nothing"
    else:
        random_size = random.randint(15, 45)
        draw_square(t, random_size)
        return "square"


# Main function wrapper
def main():
    window = turtle.Screen()
    window.bgcolor(BG_COLOR)
    window.title("My Refactored Art Project")

    # Creating the turtle player
    bob = turtle.Turtle()
    bob.speed(0)  # 0 is the fastest speed so it doesnt take forever
    bob.width(2)

    # I kept getting confused with the rows and columns grid,
    # but nested loops finally worked.
    for r in range(ROWS):
        for c in range(COLS):

            x_pos = START_X + (c * GAP)
            y_pos = START_Y - (r * GAP)

            # Call the function. We have to pass 'bob' so it knows who is drawing.
            what_drew = draw_random_shape(bob, x_pos, y_pos)

            # Print statement here just to help me debug in the console
            print("Drew a " + what_drew + " at grid spot " + str(r) + "," + str(c))

    bob.hideturtle()
    window.mainloop()


# This runs the main function automatically
main()
