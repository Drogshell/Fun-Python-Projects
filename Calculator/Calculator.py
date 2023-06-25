import customtkinter as ctk
import darkdetect


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__()



        self.mainloop()


if __name__ == "__main__":
    Calculator(darkdetect.isDark())