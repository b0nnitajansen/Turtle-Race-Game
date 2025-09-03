from turtle import Turtle, Screen
import random

# Flag to track whether the race is running
is_race_on = False

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to place a bet on a turtle color
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Choose a color:\n"
           "1. Red\n2. Purple\n3. Cyan\n4. Pink\n5. Green\n6. Orange\n"
).lower()

# List of turtle colors and starting y-positions
colors = ["red", "purple", "cyan", "pink", "green", "orange"]
y_positions = [-120, -70, -20, 30, 80, 130]  # aligns with 6 turtles
all_turtles = []

# Create turtles, assign colors, and position them at the start line
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])      # assign color
    new_turtle.penup()                          # lift pen so no lines are drawn
    new_turtle.goto(x=-240, y=y_positions[turtle_index])  # move to starting position
    all_turtles.append(new_turtle)

# Start race ONLY if the user placed a bet
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line (x > 225)
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Check if the user's bet was correct
            if winning_color == user_bet.lower():
                print(f"You won the bet! The {winning_color} turtle has won.")
            else:
                print(f"You lost the bet! The {winning_color} turtle has won.")

            break

        # Move turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# exit program when screen is clicked
screen.exitonclick()
