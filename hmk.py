from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Address Book')
root.config(background='lightgreen')

frame = Frame(root, background='white')
frame.pack()

titlelabel = Label(frame, text='My Address Book', fg='black', bg='white', bd=15)
titlelabel.grid(row=0, column=0)

openbutton = Button(frame, text='Open', fg='black', bg='white', bd=10)
openbutton.grid(row=0, column=1)

contactlist = Listbox(frame, width=25, height=12)
contactlist.grid(row=1, column=0, rowspan=6)

namelabel = Label(frame, text='Name:', fg='black', bg='white', bd=10)
namelabel.grid(row=1, column=1)

nameentry = Entry(frame, fg='black', bg='white')
nameentry.grid(row=1, column=2)

addresslabel = Label(frame, text='Address:', fg='black', bg='white', bd=10)
addresslabel.grid(row=2, column=1)

addressentry = Entry(frame, fg='black', bg='white')
addressentry.grid(row=2, column=2)

mobilelabel = Label(frame, text='Mobile:', fg='black', bg='white', bd=10)
mobilelabel.grid(row=3, column=1)

mobileentry = Entry(frame, fg='black', bg='white')
mobileentry.grid(row=3, column=2)

emaillabel = Label(frame, text='Email:', fg='black', bg='white', bd=10)
emaillabel.grid(row=4, column=1)

emailentry = Entry(frame, fg='black', bg='white')
emailentry.grid(row=4, column=2)

birthdaylabel = Label(frame, text='Birthday:', fg='black', bg='white', bd=10)
birthdaylabel.grid(row=5, column=1)

birthdayentry = Entry(frame, fg='black', bg='white')
birthdayentry.grid(row=5, column=2)

editbutton = Button(frame, text='Edit', fg='black', bg='white', bd=10)
editbutton.grid(row=7, column=0)

deletebutton = Button(frame, text='Delete', fg='black', bg='white', bd=10)
deletebutton.grid(row=7, column=1)

updatebutton = Button(frame, text='Update/Add', fg='black', bg='white', bd=10)
updatebutton.grid(row=6, column=2)

savebutton = Button(frame, text='Save', fg='black', bg='white', bd=10, width=25)
savebutton.grid(row=8, column=1)

root.mainloop()