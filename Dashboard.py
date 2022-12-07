from tkinter import *
'''import pandas as pd
from tkinter import ttk, filedialog'''
from PIL import ImageTk, Image

root = Tk()
root.title("Dashboard")
root.geometry('500x500')
# background set up
root.config(background="#6a9662")

'''my_img = ImageTk.PhotoImage(Image.open("Black-Art-XoX-349.jpg"))
my_lbl = Label(root, image=my_img)
my_lbl.place(x=0, y=0, relwidth=1, relheight=1)'''

my_frame = Frame(root, background="#6a9662")
my_frame.grid(pady=20, padx=10, row=0, column=0)

dashboard = Button(my_frame, text="DASHBOARD", relief='ridge', bd=5, fg="black", bg="dark green")
pm_masters = Button(my_frame, text="PM MASTERS", fg="black", bg="dark green")
work_order = Button(my_frame, text="WORK ORDER", fg="black", bg="dark green")
routes = Button(my_frame, text="ROUTES", fg="black", bg="dark green")
job_plans = Button(my_frame, text="JOB PLANS", fg="black", bg="dark green")
statistics = Button(my_frame, text="STATISTICS", fg="black", bg="dark green")
costs = Button(my_frame, text="COSTS", fg="black", bg="dark green")
reliability_factors = Button(my_frame, text="RELIABILITY FACTORS", fg="black", bg="dark green")

dashboard.grid(row=0, column=0, ipadx=22, pady=10)
pm_masters.grid(row=1, column=0, ipadx=22, pady=10)
work_order.grid(row=2, column=0, ipadx=20, pady=10)
routes.grid(row=3, column=0, ipadx=36, pady=10)
job_plans.grid(row=4, column=0, ipadx=28, pady=10)
statistics.grid(row=5, column=0, ipadx=28, pady=10)
costs.grid(row=6, column=0, ipadx=40, pady=10)
reliability_factors.grid(row=7, column=0, pady=10)

my_logo_frame = Frame(root, background="#6a9662")

my_img = ImageTk.PhotoImage(Image.open("Black-Art-XoX-349.jpg"))
my_lbl = Label(my_logo_frame, image=my_img)
my_lbl.place(x=0, y=0, relwidth=1, relheight=1)
my_lbl.pack()

my_logo_frame.grid(row=0, column=1)

root.mainloop()
