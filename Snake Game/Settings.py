# window info
WINDOW_SIZE = (800, 600)
FIELDS = (20, 15)

# Movement
START_POS = (5, int(FIELDS[1] / 2))
MOVE_DIRECTIONS = {"left": [-1, 0], "right": [1, 0], "up": [0, -1], "down": [0, 1]}
REFRESH_RATE = 250

# Field Limits
LEFT_LIMIT = 0
TOP_LIMIT = 0
RIGHT_LIMIT = FIELDS[0]
BOTTOM_LIMIT = FIELDS[1]

# Colours
SNAKE_BODY_COLOUR = "#4B0082"
SNAKE_HEAD_COLOUR = "#7840A1"
APPLE_COLOUR = "#F9473E"
