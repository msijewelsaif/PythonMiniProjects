from tkinter import *
import random

# Game constants
Game_width = 700
Game_height = 700
Speed = 200
Space_Size = 50
Body_Part = 3
Snake_color = "red"
Food_color = "yellow"
Background_Color = "black"

class Snake:
    def __init__(self):
        self.body_size = Body_Part
        self.coordinates = []
        self.squares = []

        for i in range(0, Body_Part):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + Space_Size, y + Space_Size, fill=Snake_color, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        self.coordinates = self.random_food_location()
        canvas.create_oval(self.coordinates[0], self.coordinates[1],
                           self.coordinates[0] + Space_Size, self.coordinates[1] + Space_Size,
                           fill=Food_color, tag="food")

    def random_food_location(self):
        x = random.randint(0, (Game_width/Space_Size)-1) * Space_Size
        y = random.randint(0, (Game_height/Space_Size)-1) * Space_Size
        return [x, y]

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= Space_Size
    elif direction == "down":
        y += Space_Size
    elif direction == "left":
        x -= Space_Size
    elif direction == "right":
        x += Space_Size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + Space_Size, y + Space_Size, fill=Snake_color)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        root.after(Speed, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= Game_width or y < 0 or y >= Game_height:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 - 50,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 50,
                       font=('consolas', 30), text="Press 'R' to Restart", fill="white", tag="restart")

def reset_game():
    global snake, food, score, direction
    canvas.delete(ALL)
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    snake = Snake()
    food = Food()
    next_turn(snake, food)

# Initialize the game window
root = Tk()
root.title("Snake Game")
root.resizable(False, False)

score = 0
direction = 'down'

frame = Frame(root)
frame.pack()

label = Label(frame, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(frame, bg=Background_Color, height=Game_height, width=Game_width)
canvas.pack()

# Center the game window
root.update()
window_height = root.winfo_height()
window_width = root.winfo_width()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Start the game
snake = Snake()
food = Food()

root.bind('<Left>', lambda event: change_direction('left'))
root.bind('<Right>', lambda event: change_direction('right'))
root.bind('<Up>', lambda event: change_direction('up'))
root.bind('<Down>', lambda event: change_direction('down'))
root.bind('r', lambda event: reset_game())

next_turn(snake, food)

root.mainloop()
