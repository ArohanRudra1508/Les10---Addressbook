from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = Tk()
root.title("Address Book")
root.geometry("500x500")

lab = Label(root, text = "Address Book", font = ("Arial", 30, "bold"))
lab.grid(row = 0, column = 0, columnspan = 5)

openbut = Button(root, text = "Open")
openbut.grid(row = 1, column = 3, padx = 10, pady = 10)

savebut = Button(root, text = "Save")
savebut.grid(row = 1, column = 4, padx = 10, pady = 10)

editbut = Button(root, text = "Edit")
editbut.grid(row = 7, column = 3, padx = 10, pady = 10)

delbut = Button(root, text = "Delete")
delbut.grid(row = 7, column = 4, padx = 10, pady = 10)

lis = Listbox(root, width = 30, height = 20)
lis.grid(row = 3, column = 0, columnspan = 3, rowspan = 5)

name_lab = Label(root, text = "Name")
name_lab.grid(row = 3, column = 3)

name_ent = Entry(root, width = 10)
name_ent.grid(row = 3, column = 4)

email_lab = Label(root, text = "Email")
email_lab.grid(row = 4, column = 3)

email_ent = Entry(root, width = 10)
email_ent.grid(row = 4, column = 4)

adres_lab = Label(root, text = "Address")
adres_lab.grid(row = 5, column = 3)

adres_ent = Entry(root, width = 10)
adres_ent.grid(row = 5, column = 4)

phone_lab = Label(root, text = "Phone Number")
phone_lab.grid(row = 6, column = 3)

phone_ent = Entry(root, width = 10)
phone_ent.grid(row = 6, column = 4)



root.mainloop()