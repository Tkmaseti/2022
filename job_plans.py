from tkinter import *

jobs = Tk()
jobs.title("Job Plans")
jobs.geometry("500x500")
jobs.config(background="#6a9662")

job_frame = Frame(jobs)
job_frame.config(background="#6a9662")
job_frame.pack(pady=20)

lbl_work_order = Label(job_frame, text="Work Order").grid(row=0, column=0, padx=15, ipady=4, ipadx=15)
lbl_id = Label(job_frame, text="ID").grid(row=0, column=1, padx=15, ipady=4, ipadx=40)
lbl_job_type_assigned = Label(job_frame, text="Job Type").grid(row=0, column=2, padx=15, ipady=4, ipadx=15)
lbl_employee_assigned = Label(job_frame, text="Employee").grid(row=0, column=3, padx=15, ipady=4, ipadx=15)

job_frame.grid(row=0, column=0, pady=15)

info_frame = Frame(jobs)
info_frame.config(background="#6a9662")

description_lbl = Label(info_frame, text="Description").grid(row=0, column=0, ipadx=28)
description_txt = Entry(info_frame).grid(row=1, column=0)

start_time_btn = Entry(info_frame)
start_time_btn.insert(0, "Start time:")
start_time_btn.grid(row=0, column=1, padx=80)

end_time_btn = Entry(info_frame)
end_time_btn.insert(0, "End Time:")
end_time_btn.grid(row=1, column=1, pady=5)

duration = "Duration: " + "30"

duration_lbl = Label(info_frame, text=duration)
duration_lbl.grid(row=2, column=1, pady=5, ipadx=26)


info_frame.grid(row=1, column=0, pady=30)
add_job_plan = Button(text="Add Job")
add_job_plan.grid(row=4, column=0)


jobs.mainloop()
