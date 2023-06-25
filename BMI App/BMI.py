import customtkinter as ctk
from Settings import *

# Try importing ctypes for handling Windows API calls
try:
    from ctypes import windll, byref, sizeof, c_int
finally:
    pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BLACK)
        # Set the title and dimensions of the application window
        self.title("")
        self.geometry("600x600")
        self.resizable(False, False)
        self.iconbitmap("C:\Active Coding Projects\Python\Simple_Python_TKinter_Projects\BMI App\Images\Logo\empty.ico")
        self.change_title_bar_colour()

        # Configure grid layout
        self.columnconfigure(0, weight=1, uniform="a")
        for i in range(4):
            self.rowconfigure(i, weight=1, uniform="a")

        # Define variables
        self.metric_flag = ctk.BooleanVar(value=True)
        self.height_int = ctk.IntVar(value=170)
        self.weight_float = ctk.DoubleVar(value=65)
        self.bmi_string = ctk.StringVar()
        # Update BMI value
        self.update_bmi()

        # Set triggers for updates
        self.height_int.trace('w', self.update_bmi)
        self.weight_float.trace('w', self.update_bmi)
        self.metric_flag.trace('w', self.change_units)

        # Create widgets
        ResultText(self, self.bmi_string)
        self.weight_input = WeightInput(self, self.weight_float, self.metric_flag)
        self.height_input = HeightInput(self, self.height_int, self.metric_flag)
        UnitSwitcher(self, self.metric_flag)

        # Start the main loop
        self.mainloop()

    def change_units(self, *args):
        self.height_input.update_text(self.height_int.get())
        self.weight_input.update_weight()

    def update_bmi(self, *args):
        height_in_meters = self.height_int.get() / 100
        weight_in_kg = self.weight_float.get()
        bmi_result = round(weight_in_kg / height_in_meters ** 2, 2)
        self.bmi_string.set(bmi_result)

    # Method to change the title bar color (Windows only)
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
    def __init__(self, parent, weight_float, metric_flag):
        super().__init__(master=parent, fg_color=LIGHT_BLACK)

        # Initialize weight and metric flag variables
        self.weight_float = weight_float
        self.metric_flag = metric_flag

        # Initialize the weight_string variable and update the weight
        self.weight_string = ctk.StringVar()
        self.update_weight()

        # Configure the grid layout
        self.grid(column=0, row=2, sticky="nsew", padx=10, pady=10)
        self.rowconfigure(0, weight=1, uniform="b")
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=1, uniform="a")
        self.columnconfigure(2, weight=3, uniform="a")
        self.columnconfigure(3, weight=1, uniform="a")
        self.columnconfigure(4, weight=2, uniform="a")

        # Set the font for the widget
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)

        label = ctk.CTkLabel(self, textvariable=self.weight_string, text_color=WHITE, font=font)
        label.grid(row=0, column=2)

        # Create the subtract button to decrease the weight
        subtract_button = ctk.CTkButton(self,
                                        text="-",
                                        command=lambda: self.update_weight(("subtract", "large")),
                                        text_color=LIGHT_GREY,
                                        fg_color=DARK_SLATE_GREY,
                                        font=font,
                                        hover_color=INDIGO,
                                        corner_radius=BUTTON_CORNER_RADIUS)

        subtract_button.grid(row=0, column=0, sticky="ns", padx=8, pady=8)

        # Create the plus button to increase the weight
        plus_button = ctk.CTkButton(self,
                                    text="+",
                                    command=lambda: self.update_weight(("plus", "large")),
                                    text_color=LIGHT_GREY,
                                    fg_color=DARK_SLATE_GREY,
                                    font=font,
                                    hover_color=INDIGO,
                                    corner_radius=BUTTON_CORNER_RADIUS)
        plus_button.grid(row=0, column=4, sticky="ns", padx=8, pady=8)

        # Create a smaller plus button for more fine-grained weight adjustment
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

        # Create a smaller subtract button for more fine-grained weight adjustment
        small_subtract_button = ctk.CTkButton(self,
                                              text="-",
                                              command=lambda: self.update_weight(("subtract", "small")),
                                              height=55,
                                              text_color=LIGHT_GREY,
                                              fg_color=DARK_SLATE_GREY,
                                              font=font,
                                              hover_color=INDIGO,
                                              corner_radius=BUTTON_CORNER_RADIUS)
        small_subtract_button.grid(row=0, column=1, padx=4, pady=4)

    def update_weight(self, info=None):
        # Check if the method received information on how to update the weight
        if info:
            # Determine the step size based on the metric flag and size of adjustment
            if self.metric_flag.get():
                step_size = 1 if info[1] == "large" else 0.1
            else:
                step_size = 0.453592 if info[1] == "large" else 0.453592 / 16

            # Update the weight based on the info provided (add or subtract)
            if info[0] == "plus":
                self.weight_float.set(self.weight_float.get() + step_size)
            else:
                self.weight_float.set(self.weight_float.get() - step_size)

        # Format the text to display the weight in the appropriate units
        if self.metric_flag.get():
            self.weight_string.set(f"{round(self.weight_float.get(), 1)} kg")
        else:
            raw_ounces = self.weight_float.get() * 2.20462 * 16
            pounds, ounces = divmod(raw_ounces, 16)
            self.weight_string.set(f"{round(pounds, 1)} lbs\n{round(ounces, 1)} oz")


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int, metric_flag):
        super().__init__(master=parent, fg_color=LIGHT_BLACK)

        # Configure grid layout
        self.grid(column=0, row=3, sticky="nsew", padx=10, pady=10)

        self.metric_flag = metric_flag

        # Create a slider for height input
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

        # Create a label to display the height
        self.slider_string = ctk.StringVar()
        self.update_text(height_int.get())

        # Configure and pack the slider label
        slider_text = ctk.CTkLabel(self,
                                   textvariable=self.slider_string,
                                   text_color=WHITE,
                                   font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE))
        slider_text.pack(side="left", padx=20)

    # Method to update the text displayed for height
    def update_text(self, amount):
        if self.metric_flag.get():
            text_string = str(int(amount))
            meters = text_string[0]
            cm = text_string[1:]
            self.slider_string.set(f"{meters}.{cm}m")
        else:
            feet, inches = divmod(amount / 2.54, 12)
            self.slider_string.set(f"{int(feet)}\'{int(inches)}\"")


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent, metric_flag):
        super().__init__(master=parent,
                         text_color=DARK_SLATE_GREY,
                         text="Metric",
                         font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight="bold"))
        self.metric_flag = metric_flag

        # Bind the label to a click event
        self.bind("<Button>", self.change_units)

        self.place(relx=0.98, rely=0.05, anchor="ne")

    # Method to switch between metric and imperial units
    def change_units(self, event):
        self.metric_flag.set(not self.metric_flag.get())

        if self.metric_flag.get():
            self.configure(text="Metric")
        else:
            self.configure(text="Imperial")


# Run the application if this script is the main module
if __name__ == "__main__":
    App()
