import customtkinter as ctk
from Settings import *

try:
    from ctypes import windll, byref, sizeof, c_int
finally:
    pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BLACK)
        self.title("")
        self.geometry("600x600")
        self.resizable(False, False)
        self.iconbitmap("C:\Active Coding Projects\Python\Simple_Python_TKinter_Projects\BMI App\Images\Logo\empty.ico")
        self.change_title_bar_colour()

        self.columnconfigure(0, weight=1, uniform="a")
        for i in range(4):
            self.rowconfigure(i, weight=1, uniform="a")

        ResultText(self)
        WeightInput(self)
        HeightInput(self)
        UnitSwitcher(self)

        self.mainloop()

    def change_title_bar_colour(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(TITLE_HEX_COLOUR)), sizeof(c_int))
        finally:
            pass


class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight="bold")
        super().__init__(master=parent, text=500.00, font=font, text_color=WHITE)
        self.grid(column=0, row=0, rowspan=2, sticky="nsew")


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=LIGHT_BLACK)
        self.grid(column=0, row=2, sticky="nsew", padx=10, pady=10)

        self.rowconfigure(0, weight=1, uniform="b")
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=1, uniform="a")
        self.columnconfigure(2, weight=3, uniform="a")
        self.columnconfigure(3, weight=1, uniform="a")
        self.columnconfigure(4, weight=2, uniform="a")

        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text="80kg", text_color=WHITE, font=font)
        label.grid(row=0, column=2)

        subtract_button = ctk.CTkButton(self, text="-", text_color=LIGHT_GREY, fg_color=DARK_SLATE_GREY,
                                        font=font, hover_color=INDIGO, corner_radius=BUTTON_CORNER_RADIUS)
        subtract_button.grid(row=0, column=0, sticky="ns", padx=8, pady=8)

        plus_button = ctk.CTkButton(self, text="+", text_color=LIGHT_GREY, fg_color=DARK_SLATE_GREY, font=font,
                                    hover_color=INDIGO, corner_radius=BUTTON_CORNER_RADIUS)
        plus_button.grid(row=0, column=4, sticky="ns", padx=8, pady=8)

        small_plus_button = ctk.CTkButton(self, text="+", height=55, text_color=LIGHT_GREY, fg_color=DARK_SLATE_GREY,
                                          font=font,
                                          hover_color=INDIGO, corner_radius=BUTTON_CORNER_RADIUS)
        small_plus_button.grid(row=0, column=3, padx=4, pady=4)

        small_subtract_button = ctk.CTkButton(self, text="-", height=55, text_color=LIGHT_GREY,
                                              fg_color=DARK_SLATE_GREY, font=font,
                                              hover_color=INDIGO, corner_radius=BUTTON_CORNER_RADIUS)
        small_subtract_button.grid(row=0, column=1, padx=4, pady=4)


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=LIGHT_BLACK)
        self.grid(column=0, row=3, sticky="nsew", padx=10, pady=10)

        slider = ctk.CTkSlider(master=self,
                               fg_color=LIGHT_GREY,
                               button_color=DARK_PURPLE,
                               button_hover_color=INDIGO,
                               progress_color=DARK_PURPLE)
        slider.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        slider_text = ctk.CTkLabel(self, text="1.80m", text_color=WHITE,
                                   font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE))
        slider_text.pack(side="left", padx=20)


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(master=parent,
                         text_color=DARK_SLATE_GREY,
                         text="Metric",
                         font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight="bold"))

        self.place(relx=0.98, rely=0.05, anchor="ne")


if __name__ == "__main__":
    App()
