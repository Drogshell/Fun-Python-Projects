import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode('light')
        super().__init__(fg_color="white")

        self.title("")
        self.geometry("400x400")
        self.iconbitmap(
            r"C:\Active Coding Projects\Python\Simple_Python_TKinter_Projects\QrCodeApp\Images\Logo\empty.ico")

        # Entry Field
        EntryField(self)

        self.mainloop()


class EntryField(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, corner_radius=20, fg_color="#4B0082")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure((0,1),weight=1, uniform="a")

        self.Frame = ctk.CTkFrame(self, fg_color="transparent")
        self.Frame.columnconfigure(0, weight=1, uniform="b")
        self.Frame.columnconfigure(1, weight=4, uniform="b")
        self.Frame.columnconfigure(2, weight=2, uniform="b")
        self.Frame.columnconfigure(3, weight=1, uniform="b")
        self.Frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(self.Frame, fg_color="#380062", border_width=0, text_color="#FFFFFF")
        entry.grid(row=0, column=1, sticky="nsew")

        save_button = ctk.CTkButton(self.Frame, text="Save", fg_color="#380062", hover_color="#260041")
        save_button.grid(row=0, column=2, sticky="nsew", padx=10)

App()
