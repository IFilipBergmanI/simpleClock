import tkinter as tk
from time import localtime, strftime


class ClockLabel(tk.Label):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.text = tk.StringVar()
        self.configure(bg="black", fg="white", textvariable=self.text)
        self.update_time()
        
    def update_time(self):
        self.text.set(strftime("%H:%M:%S", localtime()))
        self.master.after(100, self.update_time)
        

    
    


