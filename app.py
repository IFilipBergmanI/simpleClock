import os

import tkinter as tk
from clockLabel import ClockLabel


class App:

    def __init__(self):
        self.root = tk.Tk()

        # Give the window a name and an icon
        self.root.title("Clock")
        self.setup_window_icon()

        # Set size, resizability and bg color
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        # Create a clock and include it
        self.clock = ClockLabel(self.root)
        self.clock.pack(expand=True)

    def setup_window_icon(self):
        # Find image path
        basedir = os.path.dirname(__file__)
        path_to_icon = os.path.join(basedir, os.path.join("images", "clock.png"))

        # Set the icon
        img = tk.PhotoImage(file=path_to_icon)
        self.root.iconphoto(False, img)

    def run(self):
        self.root.mainloop()
        



    