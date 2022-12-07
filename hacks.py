import phonenumbers
# from hacking.numbers import number
from phonenumbers import carrier
from phonenumbers import geocoder
''' from tkinter import *

root = Tk()
root.title("Trackers")


def hack():
    ch_num = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_num, "en"))

    serv_num = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(serv_num, "en"))


btn = Button(root, text="Find ME!", command=hack)
lbl = Label(root, text="Which number would you like to track ")
txt = Entry(root)

lbl.pack()
txt.pack()
btn.pack()


root.mainloop()'''

phn = input("Enter your phone number: ")

number = phonenumbers.parse(phn)
print(geocoder.description_for_number(number, "en"))

print(carrier.name_for_number(number, "en"))
