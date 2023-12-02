from customtkinter import CTkButton
from Settings import *


class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, colour='primary'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING['corner-radius'],
            font=font,
            fg_color= COLOURS[colour]['fg'],
            hover_color=COLOURS[colour]['hover'],
            text_color=COLOURS[colour]['text'])

        self.grid(column=col, row=row, sticky='NSEW')
