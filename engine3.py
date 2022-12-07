from tkinter import *
# import PIL
import sqlite3


root = Tk()
root.title("Home")
root.iconbitmap("Untitled.png")
root.geometry("400x400")

# Database

# Create a database or connect to one
conn = sqlite3.connect('../admin_login.db')

# Create cursor
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE addresses (
#        first_name text,
#        last_name text,
#        address text,
#        city text,
#        state text,
#        zipcode integer
#        )""")


# Create a edit function to update  record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('../admin_login.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE logins SET
        first_name = :first,
        last_name = :last
        mail = :mail,
        city = :city,
        state = :state,
        zipcode = zipcode
        
        WHERE oid = :oid""",
        {
         'first': f_name_editor.get(),
         'last': l_name_editor.get(),
         'mail': mail_editor.get(),
         'city': city_editor.get(),
         'state': state_editor.get(),
         'zipcode': zipcode_editor.get(),
         'oid': record_id
        })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


def edit():
    editor = Tk()
    editor.title("Update A Record")
    editor.iconbitmap("")
    editor.geometry("400x400")

    # Create a database or connect to one
    conn = sqlite3.connect('../admin_login.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM logins WHERE oid = " + record_id)
    records = c.fetchall()

    # Create Global variables for text box names
    global f_name_editor
    global l_name_editor
    global mail_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Creating Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Creating Text Boxes Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    mail_label = Label(editor, text="Mail")
    mail_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        mail_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a save button to save a record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Create a function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('../admin_login.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from logins WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)
    
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('../admin_login.db')
    # Create cursor
    c = conn.cursor()

    # Create into table
    c.execute("INSERT INTO home VALUES (:f_name, :l_name, :mail, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'mail': mail.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clearing The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    mail.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query function


def query():
    # Create a database or connect to one
    conn = sqlite3.connect('../admin_login.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *,oid FROM logins")
    records = c.fetchall()
    # print(records)

    # Loop Through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) +"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Creating Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
mail = Entry(root, width=30)
mail.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Creating Text Boxes Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
mail_label = Label(root, text="Mail")
mail_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_label = Label(root, text="Select ID")
delete_label.grid(row=9, column=0, pady=5)

# Create a Submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Create a Query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
