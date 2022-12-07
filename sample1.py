from tkinter import *
import sqlite3

root = Tk()
root.title("Sample")
root.iconbitmap("")
root.geometry("400x400")

conn = sqlite3.connect("records_book.db")

c = conn.cursor()


def submit():
    conn = sqlite3.connect("records_book.db")

    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:pm_masters, : job_plans, :routes, :locations, :charts)",
              {
                  'pm_masters': pm_masters.get(),
                  'job_plans': job_plans.get(),
                  'routes': routes.get(),
                  'locations': locations.get(),
                  'charts': charts.get()
              })

    conn.commit()
    conn.close()

    pm_masters.delete(0, END)
    job_plans.delete(0, END)
    routes.delete(0, END)
    locations.delete(0, END)
    charts.delete(0, END)


def query():
    conn = sqlite3.connect("records_book.db")

    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    conn.commit()
    conn.close()


pm_masters = Entry(root, width=30)
pm_masters.grid(row=0, column=1, padx=20)

job_plans = Entry(root, width=30)
job_plans.grid(row=1, column=1)

routes = Entry(root, width=30)
routes.grid(row=2, column=1)

locations = Entry(root, width=30)
locations.grid(row=3, column=1)

charts = Entry(root, width=30)
charts.grid(row=4, column=1)

# Labels
pm_masters_label = Label(root, text="PM Masters")
pm_masters_label.grid(row=0, column=0)

job_plans_label = Label(root, text="Job Plans")
job_plans_label.grid(row=1, column=0)

routes_label = Label(root, text="Routes")
routes_label.grid(row=2, column=0)

locations_label = Label(root, text="Locations")
locations_label.grid(row=3, column=0)

charts_label = Label(root, text="Charts")
charts_label.grid(row=4, column=0)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=6, column=1, padx=10)

query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=1, padx=15)

conn.commit()
conn.close()
root.mainloop()

