from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Discount App')
root.config(background='white')

frame = Frame(root, background='white')
frame.pack()

def find_amount_saved():
    price = origpriceentry.get()
    discount = discountentry.get()
    amount_saved = int(price) * (int(discount)/100)
    finalprice = int(price) - int(amount_saved)
    savedtxtbox.config(text = str(amount_saved))
    finalpricetxtbox.config(text = str(finalprice))

origpricelabel = Label(frame, text = 'Original Price: ', fg = 'black', bg = 'white', bd =15)
origpricelabel.grid(row = 0, column = 0)

origpriceentry = Entry(frame, fg = 'black', bg = 'white')
origpriceentry.grid(row = 0, column = 1)

discountlabel = Label(frame, text = 'Discount (%): ', fg = 'black', bg = 'white', bd = 15)
discountlabel.grid(row =1, column = 0)

discountentry = Entry(frame, fg = 'black', bg = 'white')
discountentry.grid(row = 1, column =1)

calcbutton = Button(frame, text = 'Calculate', bg = 'yellow', fg = 'black', bd = 15, command = find_amount_saved)
calcbutton.grid(row = 2, column = 1)

savedlabel = Label(frame, text = 'Amount Saved: ',fg = 'black', bg = 'white', bd = 15)
savedlabel.grid(row = 3, column = 0)

savedtxtbox = Label(frame,text = ' ', fg = 'black', bg = 'white', bd = 15)
savedtxtbox.grid(row = 3, column = 1)

finalpricelabel = Label(frame ,text = 'Final Price: ', fg = 'black', bg ='white', bd =15)
finalpricelabel.grid(row = 4, column = 0)

finalpricetxtbox = Label(frame, text = ' ', fg = 'black', bg = 'white', bd = 15)
finalpricetxtbox.grid(row = 4, column = 1)




root.mainloop()







