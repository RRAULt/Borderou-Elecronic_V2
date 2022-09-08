from tkinter import *
from database import Database



import tkinter as tk

database = Database("borderou_electronic.db")

 
def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index) 
    
    nume_entry.delete(0,END)
    nume_entry.insert(END, selected_tuple[1])
    domiciliu_entry.delete(0,END)
    domiciliu_entry.insert(END, selected_tuple[2])
    denumirea_speciei_entry.delete(0,END)
    denumirea_speciei_entry.insert(END, selected_tuple[3])
    cantitate_entry.delete(0,END)
    cantitate_entry.insert(END, selected_tuple[4])
    pret_entry.delete(0,END)
    pret_entry.insert(END, selected_tuple[5])



def view_command():
    list_box.delete(0, END) 
    for row in database.view_all():
        list_box.insert(END,row) 


def search_command():
    list_box.delete(0, END)
    
    for row in database.search(nume_value.get(),domiciliu_value.get(),denumirea_speciei_value.get(),cantitate_value.get(),pret_value.get()):
        list_box.insert(END,row)


def insert_command():
    database.insert(nume_value.get(),domiciliu_value.get(),denumirea_speciei_value.get(),cantitate_value.get(),pret_value.get())
    
    list_box.delete(0, END)
    
    list_box.insert(END,(nume_value.get(),domiciliu_value.get(),denumirea_speciei_value.get(),cantitate_value.get(),pret_value.get()))

def delete_command():
    database.delete(selected_tuple[0]) 

def update_command():
    database.update(selected_tuple[0],nume_value.get(),domiciliu_value.get(),denumirea_speciei_value.get(),cantitate_value.get(),pret_value.get()) 

def clear_widgets():
    nume_entry.delete(0,END)   
    domiciliu_entry.delete(0,END)  
    denumirea_speciei_entry.delete(0,END)   
    cantitate_entry.delete(0,END)   
    pret_entry.delete(0,END)  


window= tk.Tk()
window.geometry("1000x720")
window["bg"] = "#FFA500"

window.title("Borderou Electronic")

name_label = Label(
    window,
    text="Nume complet",
    fg="blue",
    width=14,
    height=1,
    font=('arial Bold', 13)
    )
name_label.grid(padx = 5, pady = 5, row = 1, column = 1) 

nume_value=StringVar()  
nume_entry = Entry(window,textvariable = nume_value, width = 30, font = "TNR" "bold") 
nume_entry.grid(row=1,column=2)                             

domiciliu_label = Label(
    window,
    text="Domiciliu",
    fg="blue",
    width=10,
    height=1,
    font=('arial Bold', 13)
    )
domiciliu_label.grid(row=1,column=3)

domiciliu_value=StringVar()
domiciliu_entry = Entry(window, textvariable = domiciliu_value, width=30, font = "TNR" "bold")
domiciliu_entry.grid(row=1, column=4, columnspan = 3)

denumirea_speciei_label = Label(
    window,
    text="Denumirea speciei",
    fg="blue",
    width = 14,
    height = 1,
    font=('arial Bold', 13)
    )
denumirea_speciei_label.grid( padx = 5, pady = 5, row = 2,column = 1)

denumirea_speciei_value=StringVar()
denumirea_speciei_entry = Entry(window, textvariable = denumirea_speciei_value, width = 30, font = "TNR" "bold")
denumirea_speciei_entry.grid(row = 2, column = 2)

cantitate_label = Label(
    window,
    text="Cantitate",
    fg="blue",
    width=10,
    height=1,
    font=('arial Bold', 13)
    )
cantitate_label.grid( row = 2,column = 3)

cantitate_value=StringVar()
cantitate_entry = Entry(window, textvariable = cantitate_value, width=30, font = "TNR" "bold")
cantitate_entry.grid(row = 2, column = 4, columnspan = 3)

pret_label = Label(
    window,
    text="Pret",
    fg="blue",
    width=10,
    height=1,
    font=('arial Bold', 13)
    )
pret_label.grid(padx = 5, pady = 5, row = 3,column = 1)

pret_value=StringVar()
pret_entry = Entry(window, textvariable = pret_value, width = 30, font = "TNR" "bold")
pret_entry.grid(row = 3,column = 2)



list_box = Listbox(window, height = 10, width = 60)
list_box.grid(row = 5, column = 1, rowspan = 5,columnspan = 5)


list_box.configure( width = 100, height = 25, background ="LightYellow",font = ("TNR" "bold")) 
list_box.bind("<<ListboxSelect>>", get_selected_row)


view = Button(
    window,
    text = "View  all records",
    width = 15,
    bg="blue violet",
    fg="black",
    font=('arial Bold', 15),
    command = view_command)
view.grid(padx = 5, pady = 5, row = 12,column = 1)

search = Button(
    window,
    text="Search Entry",
    width=15, 
    bg="azure4",
    fg="red",
    font=('arial Bold', 15),
    command = search_command)
search.grid(padx = 5, pady = 5, row = 12,column = 2)

insert = Button(
    window,
    text="Add Entry",
    width=15, 
    bg="green",
    fg="black",
    font=('arial Bold', 15),
    relief = RAISED,
    command = insert_command)
insert.grid(padx = 5, pady = 1, row = 12 ,column = 3)

update = Button(
    window,
    text="Update Selected",
    width=15, 
    bg="blue",
    fg="black",
    font=('arial Bold', 15),
    command = update_command)
update.grid(padx = 5, pady = 5, row = 13 ,column = 1)

delete = Button(
    window,
    text="Delete Selected",
    width=15,
    bg="blue",
    fg="black",
    font=('arial Bold', 15), 
    command = delete_command)
delete.grid(padx = 5, pady = 5, row = 13,column = 2)

refresh = Button(
    window,
    text="Refresh",
    width=15, 
    bg="blue",
    fg="black",
    font=('arial Bold', 15),
    command = clear_widgets)
refresh.grid(padx = 5, pady = 5, row = 13,column = 3)

quit = Button(
    window,
    text="Quit",
    width=25,
    bg="red",
    fg="yellow",
    font=('arial Bold', 15),
    relief = SUNKEN,
    command = window.destroy
    )
quit.grid(row = 12, column = 4)


window.mainloop()