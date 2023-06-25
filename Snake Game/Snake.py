import customtkinter as ctk
from Settings import *
from random import randint
from sys import exit


class Game(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Snake Game")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

        # Configure columns and rows for layout
        for i in range(FIELDS[0]):
            self.columnconfigure(i, weight=1, uniform="a")

        for i in range(FIELDS[1]):
            self.rowconfigure(i, weight=1, uniform="a")

        # Initialize snake with starting position
        self.snake = [START_POS, (START_POS[0] - 1, START_POS[1]), (START_POS[0] - 2, START_POS[1])]
        # Set initial moving direction
        self.direction = MOVE_DIRECTIONS["right"]
        # Bind keyboard input to the get_input method
        self.bind("<Key>", self.get_input)

        # Place the first apple
        self.place_apple()
        # Initialize a list to store drawn frames
        self.draw_frames = []
        # Start the animation
        self.animate()

        self.mainloop()

    def animate(self):
        # Calculate new head position based on current direction
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        # Insert new head at the beginning of the snake
        self.snake.insert(0, new_head)

        # Check if snake ate the apple
        if self.snake[0] == self.apple_pos:
            self.place_apple()
        else:
            self.snake.pop()

        # Check if the snake has hit a wall or itself
        self.check_win_state()

        self.draw()
        # Recursive call to animate after 250 milliseconds
        self.after(250, self.animate)

    def check_win_state(self):
        # Get snake head position
        snake_head = self.snake[0]
        # Check conditions for game over
        if snake_head[0] >= RIGHT_LIMIT \
                or snake_head[1] >= BOTTOM_LIMIT \
                or snake_head[0] < LEFT_LIMIT \
                or snake_head[1] < TOP_LIMIT \
                or snake_head in self.snake[1:]:
            # Destroy the window and exit the program
            self.destroy()
            exit()

    def get_input(self, event):
        match event.keycode:
            case 37:
                self.direction = MOVE_DIRECTIONS["left"] \
                    if self.direction != MOVE_DIRECTIONS["right"] else self.direction
            case 38:
                self.direction = MOVE_DIRECTIONS["up"] \
                    if self.direction != MOVE_DIRECTIONS["down"] else self.direction
            case 39:
                self.direction = MOVE_DIRECTIONS["right"] \
                    if self.direction != MOVE_DIRECTIONS["left"] else self.direction
            case 40:
                self.direction = MOVE_DIRECTIONS["down"] \
                    if self.direction != MOVE_DIRECTIONS["up"] else self.direction

    def place_apple(self):
        self.apple_pos = (randint(0, FIELDS[0] - 1), randint(0, FIELDS[1] - 1))

    def draw(self):
        # If there are any previous frames, forget them
        if self.draw_frames:
            for frame, pos in self.draw_frames:
                frame.grid_forget()

            self.draw_frames.clear()

        # Create an apple frame
        apple_frame = ctk.CTkFrame(self, fg_color=APPLE_COLOUR)
        # Add the apple frame to the list of drawn frames
        self.draw_frames.append((apple_frame, self.apple_pos))

        # Loop through each segment of the snake
        for index, position in enumerate(self.snake):
            colour = SNAKE_BODY_COLOUR if index != 0 else SNAKE_HEAD_COLOUR
            snake_frame = ctk.CTkFrame(self, fg_color=colour, corner_radius=0)
            # snake_frame.grid(column=position[0], row=position[1])
            self.draw_frames.append((snake_frame, position))

        for frame, position in self.draw_frames:
            frame.grid(column=position[0], row=position[1])


if __name__ == "__main__":
    Game()
