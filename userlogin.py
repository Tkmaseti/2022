from tkinter import *
import os
# from PIL import ImageTk,Image



def delete():
    screen4.destroy()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Incorrect password")
    screen4.geometry("150x100")
    Label(screen4, text="Incorrect Password").pack()
    Button(screen4, text="Exit", command=delete).pack()



def user_not_found():
    return


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:


            # login_success()


        else:
            password_not_recognised()
    else:
        user_not_found()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration success")


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter text here").pack(pady=5)
    Label(screen1, text="Username * ").pack(pady=5)
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack(pady=5)
    Button(screen1, text="Register", command=register_user).pack()


def login():

    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")


    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Please login details").pack(pady=5)
    Label(screen2, text="Username * ").pack(pady=5)
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack(pady=5)
    Label(screen2, text="Password * ").pack(pady=5)
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack(pady=10)
    Button(screen2, text="Login", command=login_verify).pack()

# main login screen


def main_screen():
    global screen
    screen = Tk()
    screen.title("Home")
    screen.geometry("500x500")
    screen.configure(background="#6a9662")
    Label(text="Welcome ...", anchor=CENTER).grid(row=0, column=1, ipady=10, ipadx=40, pady=18)
    Button(text="Login", height=2, width=10, command=login, relief='ridge', bd=5, fg="black", bg="#6a9662").grid(row=1, column=0, pady=10, padx=40)
    Button(text="Register", height=2, width=10, command=register, relief='ridge', bd=5, fg="black", bg="#6a9662").grid(row=1, column=2, pady=10, padx=40)
    screen.mainloop()


main_screen()