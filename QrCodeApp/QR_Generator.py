import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
import qrcode

# Try importing additional modules for Windows GUI attributes
try:
    from ctypes import windll, byref, sizeof, c_int
finally:
    pass


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode('light')
        super().__init__(fg_color="white")
        self.update_title_bar()
        self.title("")
        self.geometry("600x600")
        self.resizable(False, False)
        self.iconbitmap(
            r"C:\Active Coding Projects\Python\Simple_Python_TKinter_Projects\QrCodeApp\Images\Logo\empty.ico")

        # Initialize the Entry field
        self.entry_string = ctk.StringVar()
        # Bind the method create_qr_code to changes in the entry field
        self.entry_string.trace('w', self.create_qr_code)
        # Create an EntryField instance
        EntryField(self, self.entry_string, self.save)

        # Bind the save method to the Return key
        self.bind("<Return>", self.save)

        # Initialize variables for QR Codes
        self.raw_image = None
        self.tk_image = None
        # Create an instance of QRImageGenerator
        self.qr_image = QRImageGenerator(self)

        # Start the main loop of the tkinter application
        self.mainloop()

    def create_qr_code(self, *args):
        current_text = self.entry_string.get()
        # If the text is non-empty, create QR code
        if current_text:
            self.raw_image = qrcode.make(current_text).resize((400, 400))
            self.tk_image = ImageTk.PhotoImage(self.raw_image)
            self.qr_image.update_image(self.tk_image)
        # If the text is empty, clear the QR code
        else:
            self.qr_image.clear()
            self.raw_image = None
            self.tk_image = None

    def save(self, event=""):
        # If raw_image exists, save it to a file
        if self.raw_image:
            file_path = filedialog.asksaveasfilename()
            if file_path:
                self.raw_image.save(file_path + ".jpg")

    def update_title_bar(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00FFFFFF)), sizeof(c_int))
        finally:
            pass


class QRImageGenerator(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background="white", bd=0, highlightthickness=0, relief="ridge")
        self.place(relx=0.5, rely=0.4, width=400, height=400, anchor="center")

    def update_image(self, image_tk):
        self.clear()
        self.create_image(0, 0, image=image_tk, anchor="nw")

    def clear(self):
        self.delete("all")


class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string, save_func):
        super().__init__(master=parent, corner_radius=20, fg_color="#4B0082")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure((0, 1), weight=1, uniform="a")

        # Create a frame inside the EntryField
        self.Frame = ctk.CTkFrame(self, fg_color="transparent")
        self.Frame.columnconfigure(0, weight=1, uniform="b")
        self.Frame.columnconfigure(1, weight=4, uniform="b")
        self.Frame.columnconfigure(2, weight=2, uniform="b")
        self.Frame.columnconfigure(3, weight=1, uniform="b")
        self.Frame.grid(row=0, column=0)

        # Create an entry widget for text input
        entry = ctk.CTkEntry(self.Frame, textvariable=entry_string, fg_color="#380062", border_width=0,
                             text_color="#FFFFFF")
        entry.grid(row=0, column=1, sticky="nsew")

        # Create a save button to save the QR code
        save_button = ctk.CTkButton(self.Frame, text="Save", fg_color="#380062", hover_color="#260041",
                                    command=save_func)
        save_button.grid(row=0, column=2, sticky="nsew", padx=10)


if __name__ == "__main__":
    App()
