import customtkinter as ctk
import darkdetect
from Buttons import *
from Settings import *
from PIL import Image

# Prevent errors on MAC
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        # Set up
        super().__init__(fg_color=(WHITE, BLACK))
        # Set appearance
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        # Set window size
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        # Hide title and Icon
        self.title('')
        self.iconbitmap('C:\Active Coding Projects\Python\Simple_Python_TKinter_Projects\Calculator\Images\empty.ico')
        self.title_bar_colour(is_dark)

        # Layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')

        # Data
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='test')

        # Widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):

        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        OutPutLabel(self, 0, 'SE', main_font, self.formula_string)
        OutPutLabel(self, 1, 'E', result_font, self.result_string)

        Button(parent=self,
               func=self.clear,
               text=OPERATORS['clear']['text'],
               col=OPERATORS['clear']['col'],
               row=OPERATORS['clear']['row'],
               font= main_font)

        Button(parent=self,
               func=self.percent,
               text=OPERATORS['percent']['text'],
               col=OPERATORS['percent']['col'],
               row=OPERATORS['percent']['row'],
               font=main_font)
        invert_image = ctk.CTkImage(
            light_image= Image.open(OPERATORS['invert']['image path']['dark']),
            dark_image= Image.open(OPERATORS['invert']['image path']['light'])
        )
        ImageButton(
            parent=self,
            func= self.invert,
            col= OPERATORS['invert']['col'],
            row= OPERATORS['invert']['row'],
            image= invert_image
        )

        for num, data in NUM_POSITIONS.items():
            NumberButton(
                parent= self,
                text= num,
                func=self.num_press,
                col=data['col'],
                row=data['row'],
                font= main_font,
                span=data['span'])

        for operator, data in MATH_POSITIONS.items():
            if data['image path']:
                divide_image = ctk.CTkImage(
                    light_image= Image.open(data['image path']['dark']),
                    dark_image= Image.open(data['image path']['light'])
                )
                MathImageButton(
                    parent=self,
                    text=data['character'],
                    operator=operator,
                    func=self.compute,
                    col=data['col'],
                    row=data['row'],
                    image=divide_image,
                )
            else:
                MathButton(
                    parent=self,
                    text=data['character'],
                    operator=operator,
                    func=self.compute,
                    col=data['col'],
                    row=data['row'],
                    font=main_font,
                )

    def clear(self):
        print('Get clear!')

    def percent(self):
        print('Division anyone?')

    def invert(self):
        print('Inverted')

    def num_press(self, value):
        print(value)

    def compute(self, value):
        print(value)

    def title_bar_colour(self, is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOUR = TITLE_BAR_HEX_COLOURS['dark'] if is_dark else TITLE_BAR_HEX_COLOURS['light']
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOUR)), sizeof(c_int))
        except:
            pass


class OutPutLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)


if __name__ == "__main__":
    #Calculator(darkdetect.isDark())
    Calculator(True)
