import tkinter as tk

class ClockLabel(tk.Label):

    def __init__(self, master):
        super().__init__(master)
        self.text = tk.StringVar()
        self.configure(bg="black", fg="white", textvariable=self.text)
        self.text.set("test")
        
    
    


