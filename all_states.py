import pandas
import turtle

screen = turtle.Screen()
screen.title('India State')

# Set screen size (window size + canvas size)
screen.setup(width=1000, height=900)  # Window size
screen.screensize(900, 800)           # Drawing area size

img = 'india_map.gif'  # Use .gif format
screen.addshape(img)
turtle.shape(img)

# def get_mouse_click_cor(x, y):
#     print(f'{x},{y}')

# turtle.onscreenclick(get_mouse_click_cor)

# Prompt the user for input (title, prompt)
state_name = screen.textinput("State Guess", "Enter the name of an Indian state:")

# print("You entered:", state_name)

df = pandas.read_csv('indian_states.csv')
def get_coords(state_name):
    row = df[df['State Name'].str.lower()==state_name.strip().lower()]
    if not row.empty:
        x = float(row.iloc[0]['x'])
        y = float(row.iloc[0]['y'])
        return x,y
    return None,None

x,y=get_coords(state_name)

print(f'{x},{y}')

# Create a turtle to write text
writer = turtle.Turtle()
writer.hideturtle()         # Hide the turtle arrow
writer.penup()              # Don't draw lines
writer.goto(x, y)           # Move to position
writer.write(state_name, align="center", font=("Arial", 5, "bold"))

turtle.mainloop()
# import csv
# import random

# states = [
#     "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
#     "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
#     "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
#     "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
#     "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
#     "West Bengal"
# ]

# states.sort()

# with open('indian_states.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["State Name", "x", "y"])  # Header
#     for state in states:
#         x = random.randint(-500, 500)  # Adjust as needed for your map scale
#         y = random.randint(-400, 400)
#         writer.writerow([state, x, y])

# print("CSV file 'indian_states_with_coordinates.csv' created successfully.")
import turtle
import pandas as pd

# ----- Setup Screen -----
screen = turtle.Screen()
screen.title('India State Guessing Game')
screen.setup(width=1000, height=900)
screen.screensize(900, 800)

# Set background map image (must be .gif)
img = 'india_map.gif'
screen.addshape(img)
turtle.shape(img)

# ----- Load CSV Data -----
df = pd.read_csv('indian_states.csv')
all_states = df['State Name'].str.strip().str.lower().tolist()
guessed_states = []

# ----- Function to Get Coordinates -----
def get_coordinates(state_name):
    match = df[df['State Name'].str.strip().str.lower() == state_name.strip().lower()]
    if not match.empty:
        x = float(match.iloc[0]['x'])
        y = float(match.iloc[0]['y'])
        return x, y
    return None, None

# ----- Create Writer Turtle -----
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# ----- Main Game Loop -----
while len(guessed_states) < len(all_states):
    answer = screen.textinput(f"{len(guessed_states)}/28 States Correct", "Enter an Indian state (or 'exit' to quit):")

    if not answer or answer.strip().lower() == 'exit':
        break

    answer = answer.strip().lower()

    if answer in all_states and answer not in guessed_states:
        x, y = get_coordinates(answer)
        if x is not None:
            guessed_states.append(answer)
            writer.goto(x, y)
            writer.write(answer.title(), align="center", font=("Arial", 10, "bold"))
    elif answer in guessed_states:
        print("You've already guessed that state.")
    else:
        print("Invalid state name.")

# ----- End Message -----
print(f"Game Over. You guessed {len(guessed_states)} states correctly.")

turtle.mainloop()
