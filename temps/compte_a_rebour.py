"""
import time


def countdown(num_of_sec):
    while num_of_sec:
        m, s = divmod(num_of_sec, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        time.sleep(1)
        num_of_sec -= 1
    print('countdwon finished.')


temps = input("Input number of seconds to countdown: ")
temps = int(temps)
countdown(temps)

"""
import time as t
import tkinter as tk


def decompte(count=180):
    m, s = divmod(count, 60)

    lab.config(text='{:02d}:{:02d}'.format(m, s))
    if count > 0:
        fen1.after(1000, decompte, count - 1)


fen1 = tk.Tk()

lab = tk.Label(fen1, text='{:02d}:{:02d}'.format(3, 0))
lab.pack()

btn = tk.Button(fen1, text="go", command=decompte)
btn.pack()

btn2 = tk.Button(fen1, text="quit", command=fen1.destroy)
btn2.pack()

fen1.mainloop()

















