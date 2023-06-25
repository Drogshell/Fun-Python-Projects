# Sizing
APP_SIZE = (400,700)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

# Text
FONT = "Roboto"
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
    "gap": 0.5,
    "corner-radius": 0
}

NUM_POSITIONS = {
    '.': {"col": 2, "row": 6, "span": 1},
    0: {"col": 0, "row": 6, "span": 2},
    1: {"col": 0, "row": 5, "span": 1},
    2: {"col": 1, "row": 5, "span": 1},
    3: {"col": 2, "row": 5, "span": 1},
    4: {"col": 0, "row": 4, "span": 1},
    5: {"col": 1, "row": 4, "span": 1},
    6: {"col": 2, "row": 4, "span": 1},
    7: {"col": 0, "row": 3, "span": 1},
    8: {"col": 1, "row": 3, "span": 1},
    9: {"col": 2, "row": 3, "span": 1}
}

MATH_POSITIONS = {
    '/': {"col": 3, "row": 2, "character": '', "operator": '/', "image path": "Images/divide_light.png"},
    '*': {"col": 3, "row": 3, "character": 'x', "operator": '*', "image path": None},
    '-': {"col": 3, "row": 4, "character": '-', "operator": '-', "image path": None},
    '=': {"col": 3, "row": 6, "character": '=', "operator": '=', "image path": None},
    '+': {"col": 3, "row": 5, "character": '+', "operator": '+', "image path": None}
}

OPERATORS = {
    'clear': {"col": 0, "row": 2, "text": 'AC', "image path": None},
    'invert': {"col": 1, "row": 2, "text": '', "image path": {"light": "Images/invert_light.png", "dark": "Images/invert_dark.png"}},
    'percent': {"col": 2, "row": 2, "text": '%', "image path": None}
}

BLACK = "#000000"
WHITE = "#FFFFFF"

COLOURS = {
    "primary": {"fg": ("#6200EE", "#BB86FC"), "hover": ("#3700B3", "#3700B3"), "text": ("#FFFFFF","#000000")},
    "secondary": {"fg": ("#018786", "#03DAC6"), "hover": ("#efefed", "#686868"), "text": ("#FFFFFF","#000000")},

}

TITLE_BAR_HEX_COLOURS = {
    "dark": 0x00000000,
    "light": 0x00FFFFFF
}