import tkinter as tk
from clockLabel import ClockLabel

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)

        self.frame.configure(background="black", width=200, height=200)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.clock = ClockLabel(self.frame)
        self.clock.pack()

    def run(self):
        self.root.mainloop()
        



    