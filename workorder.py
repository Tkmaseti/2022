from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog


work = Tk()
work.configure(background="#6a9662")
work.title("Work Order")
work.geometry("800x500")

'''
frame = Frame(work)
frame.pack(pady=20)

search = Entry(frame)
search.insert(0, "Workorder")
search.grid(row=0, column=0)

go = Button(frame, text="➤")
go.grid(row=0, column=1)
'''
add_frame = Frame(work)
add_frame.pack(pady=20)

'''
# Labels for add frame 
wo = Label(add_frame, text="Work Order", font="Century")
wo.grid(row=0, column=0)

description = Label(add_frame, text="Description", font="Century")
description.grid(row=0, column=1)

mt = Label(add_frame, text="Maintenance Type", font="Century")
mt.grid(row=0, column=2)

state = Label(add_frame, text="Completed or Not", font="Century")
state.grid(row=0, column=3)

date = Label(add_frame, text="Date Assigned", font="Century")
date.grid(row=0, column=4)
'''

# Text box for add frame
wo_box = Entry(add_frame)
wo_box.insert(0, "Work Order")
wo_box.grid(row=1, column=0, ipady=4, ipadx=1)

description_box = Entry(add_frame)
description_box.grid(row=1, column=1, ipady=4, ipadx=2)

mt_box = Entry(add_frame)
mt_box.grid(row=1, column=2, ipady=4, ipadx=2)

state_box = Entry(add_frame)
state_box.grid(row=1, column=3, ipady=4, ipadx=2)

date_box = Entry(add_frame)
date_box.grid(row=1, column=4, ipady=4, ipadx=2)


style = ttk.Style()
style.configure("Treeview",
                background="silver",
                foreground="black",
                rowheight=25,
                fieldbackgroung="silver"
                )

style.theme_use("clam")

style.map("Treeview",
          background=[('selected', 'green')]
          )

my_tree = ttk.Treeview(work)

# Defining  our columns
my_tree['columns'] = ("Work Order", "Description", "Maintenance Type",  "Completed/Not Completed", "Date Assigned")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Work Order", anchor=CENTER, width=120)
my_tree.column("Description", anchor=W, width=120)
my_tree.column("Maintenance Type", anchor=CENTER, width=120)
my_tree.column("Completed/Not Completed", anchor=CENTER, width=155)
my_tree.column("Date Assigned", anchor=W, width=120)

# Creating Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Work Order", text="Work Order", anchor=CENTER)
my_tree.heading("Description", text="Description", anchor=W)
my_tree.heading("Maintenance Type", text="Maintenance Type", anchor=CENTER)
my_tree.heading("Completed/Not Completed", text="Completed/Not Completed", anchor=CENTER)
my_tree.heading("Date Assigned", text="Date Assigned", anchor=W)

# Adding Data
data = [
    ["1", "Install a pump",	"CM",	"completed"],
    ["2", "Replace a bearing", "CM", "completed"],
    ["3", "Paint the workshop", "CM", "completed"],
    ["4", "Fix the Window", "CM", "in progress"],
    ["5", "Service the air con", "PM", "in progress"],
    ["6", "Service the generator", "PM", "in progress"],
    ["7", "Set the limit switch", "CM", "in progress"],
    ["8", "Remove the window", "CM", "in progress"],
    ["9", "Paint the workshop", "PM", "in progress"],
    ["10", "Clean the compressor", "PM", "in progress"]
]
count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]))
    count += 1


'''
my_tree.insert(parent='', index='end', iid=0, text="1", values=("Install a pump",	"CM",	"completed"))
my_tree.insert(parent='', index='end', iid=1, text="2", values=("Replace a bearing", "CM", "completed"))
my_tree.insert(parent='', index='end', iid=2, text="3", values=("Paint the workshop", "CM", "completed"))
my_tree.insert(parent='', index='end', iid=3, text="4", values=("Fix the Window", "CM", "in progress"))
my_tree.insert(parent='', index='end', iid=4, text="5", values=("Service the air con", "PM", "in progress"))
my_tree.insert(parent='', index='end', iid=5, text="6", values=("Service the generator", "PM", "in progress"))
my_tree.insert(parent='', index='end', iid=6, text="7", values=("Set the limit switch", "CM", "in progress"))
my_tree.insert(parent='', index='end', iid=7, text="8", values=("Remove the window", "CM", "in progress"))
my_tree.insert(parent='', index='end', iid=8, text="9", values=("Paint the workshop", "PM", "in progress"))
my_tree.insert(parent='', index='end', iid=9, text="10", values=("Clean the compressor", "PM", "in progress"))
'''
# Add child
my_tree.pack(pady=20)



# New file button
def new_file():
    def file_open():
        filename = filedialog.askopenfilename(
            initialdir="C:/Documents",
            title="Open file",
            filetype=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
        )

        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
            except ValueError:
                label.config(text='File not open')
            except FileNotFoundError:
                label.config(text='File not found')

        clear_tree()

        my_tree["column"] = list(df.columns)
        my_tree["show"] = "headings"
        # Loop
        for column in my_tree["column"]:
            my_tree.heading(column, text=column)

        # putting data
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("", "end", values=row)

        my_tree.pack()

    # add menu
    my_menu = Menu(work)
    work.config(menu=my_menu)

    # menu drop down
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label='Spreadsheet', menu=file_menu)
    file_menu.add_command(label='Open', command=file_open)

    def clear_tree():
        my_tree.delete(*my_tree.get_children())


# add record
def add_records():

    ''' global count

    my_tree.insert(parent='', index='end', iid=count, text='', values=(wo_box.get(), description_box.get(), mt_box.get(), state_box.get(), date_box.get()))
    count += 1

    # Clear txt boxes
    wo_box.delete(0, END)
    description_box.delete(0, END)
    mt_box.delete(0, END)
    state_box.delete(0, END)
    date_box.delete(0, END)
    '''
    add_rec = Tk()
    add_rec.title("Adding Record")
    add_rec.geometry("500x500")

    style = ttk.Style()
    style.configure("Treeview",
                    background="silver",
                    foreground="blue",
                    rowheight=25,
                    fieldbackgroung="silver"
                    )

    style.theme_use("clam")

    style.map("Treeview",
              background=[('selected', 'green')]
              )

    my_tree = ttk.Treeview(add_rec)

    # Defining  our columns
    my_tree['columns'] = ("Work Order", "Description", "Maintenance Type", "Completed/Not Completed", "Date Assigned")

    # Format our columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Work Order", anchor=CENTER, width=120)
    my_tree.column("Description", anchor=W, width=120)
    my_tree.column("Maintenance Type", anchor=CENTER, width=120)
    my_tree.column("Completed/Not Completed", anchor=CENTER, width=155)
    my_tree.column("Date Assigned", anchor=W, width=120)

    # Creating Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Work Order", text="Work Order", anchor=CENTER)
    my_tree.heading("Description", text="Description", anchor=W)
    my_tree.heading("Maintenance Type", text="Maintenance Type", anchor=CENTER)
    my_tree.heading("Completed/Not Completed", text="Completed/Not Completed", anchor=CENTER)
    my_tree.heading("Date Assigned", text="Date Assigned", anchor=W)

    # Adding Data
    data = [
        ["1", "Install a pump", "CM", "completed"],
        ["2", "Replace a bearing", "CM", "completed"],
        ["3", "Paint the workshop", "CM", "completed"],
        ["4", "Fix the Window", "CM", "in progress"],
        ["5", "Service the air con", "PM", "in progress"],
        ["6", "Service the generator", "PM", "in progress"],
        ["7", "Set the limit switch", "CM", "in progress"],
        ["8", "Remove the window", "CM", "in progress"],
        ["9", "Paint the workshop", "PM", "in progress"],
        ["10", "Clean the compressor", "PM", "in progress"]
    ]
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]))
        count += 1

    '''
    my_tree.insert(parent='', index='end', iid=0, text="1", values=("Install a pump",	"CM",	"completed"))
    my_tree.insert(parent='', index='end', iid=1, text="2", values=("Replace a bearing", "CM", "completed"))
    my_tree.insert(parent='', index='end', iid=2, text="3", values=("Paint the workshop", "CM", "completed"))
    my_tree.insert(parent='', index='end', iid=3, text="4", values=("Fix the Window", "CM", "in progress"))
    my_tree.insert(parent='', index='end', iid=4, text="5", values=("Service the air con", "PM", "in progress"))
    my_tree.insert(parent='', index='end', iid=5, text="6", values=("Service the generator", "PM", "in progress"))
    my_tree.insert(parent='', index='end', iid=6, text="7", values=("Set the limit switch", "CM", "in progress"))
    my_tree.insert(parent='', index='end', iid=7, text="8", values=("Remove the window", "CM", "in progress"))
    my_tree.insert(parent='', index='end', iid=8, text="9", values=("Paint the workshop", "PM", "in progress"))
    my_tree.insert(parent='', index='end', iid=9, text="10", values=("Clean the compressor", "PM", "in progress"))
    '''
    # Add child
    my_tree.pack(pady=20)

    add_rec.mainloop()


# Remove record
def removed():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


# Buttons Frame
my_frame = Frame(work, bg='#6a9662')
my_frame.pack(pady=10)

# Buttons

remove_all = Button(my_frame, text="Remove Record", command=removed, relief='ridge', bd=5, fg="black", bg="dark green")
remove_all.grid(pady=5, padx=20, row=0, column=0)

add_record = Button(my_frame, text="Add Record", command=add_records, relief='ridge', bd=5, fg="black", bg="dark green")
add_record.grid(pady=5, padx=30, ipadx=11, row=0, column=1)

new_file_button = Button(my_frame, text="Add file", command=new_file, relief='ridge', bd=5, fg="black", bg="dark green")
new_file_button.grid(pady=5, padx=30, ipadx=21, row=0, column=2)

find_record = Button(my_frame, text="Find Record", relief='ridge', bd=5, fg="black", bg="dark green")
find_record.grid(pady=5, padx=30, ipadx=18, row=0, column=3)

label = Label(work)

work.mainloop()
