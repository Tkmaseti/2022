from tkinter import *

root = Tk()
root.title("Work Order rough copy1")
root.iconbitmap("Untitled.png")
root.geometry("400x400")

# Creating Text Boxes
pm_masters = Entry(root, width=30)
pm_masters.grid(row=1, column=0)
job_plans = Entry(root, width=30)
job_plans.grid(row=1, column=1)
routes = Entry(root, width=30)
routes.grid(row=1, column=2)
location = Entry(root, width=30)
location.grid(row=1, column=3)
charts = Entry(root, width=30)
charts.grid(row=1, column=4)

# Creating Text Boxes label = Label(root, text="First Name")
pm_masters_label = Label(root, text="Pm Masters")
pm_masters_label.grid(row=0, column=0)
job_plans_label = Label(root, text="Job Plans")
job_plans_label.grid(row=0, column=1)
routes_label = Label(root, text="Routes")
routes_label.grid(row=0, column=2)
location_label = Label(root, text="Location")
location_label.grid(row=0, column=3)
charts_label = Label(root, text="Charts")
charts_label.grid(row=0, column=4)

column_1 = Label(root, text="""
WORK ORDER

1\n
2\n
3\n
4\n
5\n
6\n
7\n
8\n
9\n
10

""", bg='white')
column_1.grid(row=2, column=0, pady=15)

column_2 = Label(root, text="""
DESCRIPTION

Install a pump9\n
Replace a bearing9\n
Paint the workshop9\n
Fix the Window\n
Service the air con\n
Service the generator9\n
Set the limit switch9\n
Remove the window9\n
Paint the workshop9\n
Clean the compressor

""", bg='white')
column_2.grid(row=2, column=1, pady=15)

column_3 = Label(root, text="""
MAINTENANCE TYPE

CM\n
CM\n
CM\n
CM\n
PM\n
PM\n
CM\n
CM\n
PM\n
PM

""", bg='white')
column_3.grid(row=2, column=2, pady=15)

column_4 = Label(root, text="""
Completed/Not completed

completed\n
completed\n
completed\n
in progress\n
in progress\n
in progress\n
in progress\n
in progress\n
in progress\n
in progress

""", bg='white')
column_4.grid(row=2, column=3, pady=15)

next = Button(root, text="NEXT")
next.grid(row=3, column=4, ipadx=35)

root.mainloop()
