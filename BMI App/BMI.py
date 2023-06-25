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

        self.height_int = ctk.IntVar(value=170)
        self.weight_float = ctk.DoubleVar(value=65)
        self.bmi_string = ctk.StringVar()
        self.update_bmi()

        self.height_int.trace('w', self.update_bmi)
        self.weight_float.trace('w', self.update_bmi)

        ResultText(self, self.bmi_string)
        WeightInput(self, self.weight_float)
        HeightInput(self, self.height_int)
        UnitSwitcher(self)

        self.mainloop()

    def update_bmi(self, *args):
        height_in_meters = self.height_int.get() / 100
        weight_in_kg = self.weight_float.get()
        bmi_result = round(weight_in_kg / height_in_meters ** 2, 2)
        self.bmi_string.set(bmi_result)

    def change_title_bar_colour(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(TITLE_HEX_COLOUR)), sizeof(c_int))
        finally:
            pass


class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight="bold")
        super().__init__(master=parent, font=font, text_color=WHITE, textvariable=bmi_string)
        self.grid(column=0, row=0, rowspan=2, sticky="nsew")


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_float):
        super().__init__(master=parent, fg_color=LIGHT_BLACK)
        self.weight_float = weight_float

        self.weight_string = ctk.StringVar()
        self.update_weight()

        self.grid(column=0, row=2, sticky="nsew", padx=10, pady=10)
        self.rowconfigure(0, weight=1, uniform="b")
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=1, uniform="a")
        self.columnconfigure(2, weight=3, uniform="a")
        self.columnconfigure(3, weight=1, uniform="a")
        self.columnconfigure(4, weight=2, uniform="a")

        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, textvariable=self.weight_string, text_color=WHITE, font=font)
        label.grid(row=0, column=2)

        subtract_button = ctk.CTkButton(self,
                                        text="-",
                                        command=lambda: self.update_weight(("subtract", "large")),
                                        text_color=LIGHT_GREY,
                                        fg_color=DARK_SLATE_GREY,
                                        font=font,
                                        hover_color=INDIGO,
                                        corner_radius=BUTTON_CORNER_RADIUS)

        subtract_button.grid(row=0, column=0, sticky="ns", padx=8, pady=8)

        plus_button = ctk.CTkButton(self,
                                    text="+",
                                    command=lambda: self.update_weight(("plus", "large")),
                                    text_color=LIGHT_GREY,
                                    fg_color=DARK_SLATE_GREY,
                                    font=font,
                                    hover_color=INDIGO,
                                    corner_radius=BUTTON_CORNER_RADIUS)
        plus_button.grid(row=0, column=4, sticky="ns", padx=8, pady=8)

        small_plus_button = ctk.CTkButton(self,
                                          text="+",
                                          command=lambda: self.update_weight(("plus", "small")),
                                          height=55,
                                          text_color=LIGHT_GREY,
                                          fg_color=DARK_SLATE_GREY,
                                          font=font,
                                          hover_color=INDIGO,
                                          corner_radius=BUTTON_CORNER_RADIUS)
        small_plus_button.grid(row=0, column=3, padx=4, pady=4)

        small_subtract_button = ctk.CTkButton(self,
                                              text="-",
                                              command=lambda: self.update_weight(("plus", "small")),
                                              height=55,
                                              text_color=LIGHT_GREY,
                                              fg_color=DARK_SLATE_GREY,
                                              font=font,
                                              hover_color=INDIGO,
                                              corner_radius=BUTTON_CORNER_RADIUS)
        small_subtract_button.grid(row=0, column=1, padx=4, pady=4)

    def update_weight(self, info=None):
        if info:
            step_size = 1 if info[1] == "large" else 0.1
            if info[0] == "plus":
                self.weight_float.set(self.weight_float.get() + step_size)
            else:
                self.weight_float.set(self.weight_float.get() - step_size)
        self.weight_string.set(f"{round(self.weight_float.get(), 1)}kg")


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int):
        super().__init__(master=parent, fg_color=LIGHT_BLACK)
        self.grid(column=0, row=3, sticky="nsew", padx=10, pady=10)

        slider = ctk.CTkSlider(master=self,
                               command=self.update_text,
                               from_=100,
                               to=250,
                               fg_color=LIGHT_GREY,
                               button_color=DARK_PURPLE,
                               button_hover_color=INDIGO,
                               progress_color=DARK_PURPLE,
                               variable=height_int)
        slider.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        self.slider_string = ctk.StringVar()
        self.update_text(height_int.get())

        slider_text = ctk.CTkLabel(self,
                                   textvariable=self.slider_string,
                                   text_color=WHITE,
                                   font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE))
        slider_text.pack(side="left", padx=20)

    def update_text(self, amount):
        text_string = str(int(amount))
        meters = text_string[0]
        cm = text_string[1:]
        self.slider_string.set(f"{meters}.{cm}m")


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(master=parent,
                         text_color=DARK_SLATE_GREY,
                         text="Metric",
                         font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight="bold"))

        self.place(relx=0.98, rely=0.05, anchor="ne")


if __name__ == "__main__":
    App()
