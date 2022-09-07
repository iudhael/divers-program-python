
import tkinter as tk
import time

class Timer():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=('Times New Roman', 40))
        self.label.pack()
        self.updateClock()
        self.root.mainloop()

    def updateClock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text = now)
        self.root.after(1000, self.updateClock)

gui = Timer()


