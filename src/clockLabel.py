import tkinter as tk
from time import localtime, strftime


class ClockLabel(tk.Label):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.text = tk.StringVar()
        self.configure(bg="black", fg="white", textvariable=self.text, font=("Arial", 25))

        # start updating the time, it is only required once as update time schedules itself to be called again
        self.update_time()
        
    def update_time(self):
        # Update time text based on current local time
        self.text.set(strftime("%H:%M:%S", localtime()))

        # Schedule next time update
        self.master.after(100, self.update_time)
        

    
    


