_from tkinter import *
from tkinter import ttk

root = Tk()
root.title('TK')

# Add style
style = ttk.Style()

style.theme_use("clam")

style.configure("Treeview",
                background="Aqua",
                foreground="black",
                rowheight=25,
                fieldbackgroung="silver"
                )
style.map("Treeview",
          background=[('Selected', 'green')])

my_tree = ttk.Treeview(root)

# Define columns
my_tree['columns'] = ("Name", "ID", "Favourite Pizza")

# Format columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favourite Pizza", anchor=W, width=140)

# create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Pizza", text="Favourite Pizza", anchor=W)

# Add data
data = [
    ["John", 1, "Peperoni"],
    ["Zoe", 2, "Onion"],
    ["Sam", 3, "Salami"],
    ["Luke", 4, "Olive"],
    ["Dan", 5, "Meat"]
]

global count
count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
    count += 1


'''
my_tree.insert(parent='', index='end', iid=0, text='', values=("John", 1, "Peperoni"))
my_tree.insert(parent='', index='end', iid=1, text='', values=("Zoe", 2, "Onion"))
my_tree.insert(parent='', index='end', iid=2, text='', values=("Sam", 3, "Salami"))
my_tree.insert(parent='', index='end', iid=3, text='', values=("Luke", 4, "Olive"))
my_tree.insert(parent='', index='end', iid=4, text='', values=("Dan", 5, "Meat"))
'''

my_tree.pack(pady=20)
add_frame = Frame(root)
add_frame.pack(pady=20)

# Labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

# Text box
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)


# add record
def add_records():
    global count

    my_tree.insert(parent='', index='end', iid=count, text='', values=(name_box.get(), id_box.get(), topping_box.get()))
    count += 1

    # Clear txt boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


# Buttons
add_record = Button(root, text="Add Record", command=add_records)
add_record.pack(pady=20)


# Remove all
def removed():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


remove_all = Button(root, text="Remove Record", command=removed)
remove_all.pack(pady=10)


root.mainloop()
