from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog
import os

root = Tk()
root.geometry("400x400")

frame_1 = Frame(root, background="#f216ff")

label = Label(frame_1, text="hello")
label.pack()

frame_1.grid(row=0, column=0)

frame_2 = Frame(root, background="#6a9662")

label = Label(frame_2, text="world")
label.pack()

frame_2.grid(row=0, column=1)

root.mainloop()
