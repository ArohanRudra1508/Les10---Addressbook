from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import tkinter as tk


root = Tk()
root.title("Address Book")
root.geometry("600x600")

adresbook = {}

def clear():
    name_ent.delete(0, END)
    email_ent.delete(0, END)
    adres_ent.delete(0, END)
    phone_ent.delete(0, END)

def reset():
    clear()
    lis.delete(0, END)
    adresbook.clear()
    lab.configure(text = "Adressbook")

def save():
    fout = asksaveasfile(defaultextension = ".txt")
    if fout:
        print(adresbook, file = fout)
        reset()
    else:
        messagebox.showinfo("Warning", "Your adressbook is not saved.")

def open():
    fin = askopenfile(title = "OpenFile")
    if fin:
        adresbook = eval(fin.read())
        for key in adresbook.keys():
            lis.insert(END, key)
        lab.configure(text = os.path.basename(fin.name))
    else:
        messagebox.showinfo("Warning", "File has not been opened.")

def update():
    key = name_ent.get()
    if key == "":
        messagebox.showinfo("Warning", "Name has not been filled.")
    else:
        if key not in adresbook.keys():
            lis.insert(END, key)
        else:
            adresbook[key] = email_ent.get()

def hover(event):
    newwin = Toplevel(root)
    index = lis.curselection()
    contact = ""
    if index:
        key = lis.get(index)
        contact += "NAME:" + key + "\n \n"
        details = adresbook[key]
        contact += "EMAIL:" + details[0] + "\n"
        contact += "ADDRESS:" + details[1] + "\n"
        contact += "PHONE NUMBER:" + details[2] + "\n"

    l = Label(newwin)
    l.grid(row = 0, column = 0)
    l.configure(text = contact)
def edit():
    clear()
    index = lis.curselection()
    if index:
        name_ent.insert(0, lis.get(index))
        details = adresbook[name_ent.get()]
        email_ent.insert(0, details[0])
        adres_ent.insert(0, details[1])
        phone_ent.insert(0, details[2])
    else:
        messagebox.showinfo("Warning", "Please select a name first.")
def delete():
    index = lis.curselection()
    if index:
        del adresbook[lis.get(index)]
        lis.delete(index)
        clear()
    else:
        messagebox.showinfo("Warning", "Please select a name first.")

lab = Label(root, text = "Address Book", font = ("Arial", 30, "bold"))
lab.grid(row = 0, column = 0, columnspan = 5)

openbut = tk.Button(root, text = "Open", fg = "red", bg = "blue", activebackground = "blue", command = open)
openbut.grid(row = 1, column = 3, padx = 10, pady = 10)

savebut = tk.Button(root, text = "Save", fg = "red", bg = "blue", activebackground = "blue", command = save)
savebut.grid(row = 1, column = 4, padx = 10, pady = 10)

editbut = tk.Button(root, text = "Edit", fg = "red", bg = "blue", activebackground = "blue", command = edit)
editbut.grid(row = 8, column = 3, padx = 10, pady = 10)

delbut = tk.Button(root, text = "Delete", fg = "red", bg = "blue", activebackground = "blue", command = delete)
delbut.grid(row = 8, column = 4, padx = 10, pady = 10)

addbut = tk.Button(root, text = "Add", fg = "red", bg = "blue", activebackground = "blue", command = update)
addbut.grid(row = 7, column = 3, padx = 10, pady = 10)

lis = Listbox(root, width = 30, height = 20)
lis.grid(row = 3, column = 0, columnspan = 3, rowspan = 5, padx = 10, pady = 10)
lis.bind('<<ListboxSelect>>', hover)

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
