from customtkinter import CTkButton
from Settings import *


class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span=1, colour='purple'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING['corner-radius'],
            font=font,
            fg_color=COLOURS[colour]['fg'],
            hover_color=COLOURS[colour]['hover'],
            text_color=COLOURS[colour]['text'])

        self.grid(column=col, columnspan=span, row=row, sticky='NSEW', padx=STYLING['gap'], pady=STYLING['gap'])


class ImageButton(CTkButton):
    def __init__(self, parent, func, col, row, image, text='', colour='purple'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING['corner-radius'],
            image=image,
            fg_color=COLOURS[colour]['fg'],
            hover_color=COLOURS[colour]['hover'],
            text_color=COLOURS[colour]['text']
        )

        self.grid(column=col, row=row, sticky='NSEW', padx=STYLING['gap'], pady=STYLING['gap'])


class NumberButton(Button):
    def __init__(self, parent, text, func, col, row, font, span, colour='light-purple'):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(text),
            col=col,
            row=row,
            font=font,
            colour=colour,
            span=span
        )


class MathButton(Button):
    def __init__(self, parent, text, operator, func, col, row, font, colour='purple'):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(operator),
            col=col,
            row=row,
            font=font,
            colour=colour,
        )

class MathImageButton(ImageButton):
    def __init__(self, parent, text, operator, func, col, row, image, colour='purple'):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(operator),
            col=col,
            row=row,
            image=image,
            colour=colour,
        )