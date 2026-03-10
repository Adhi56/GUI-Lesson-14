from tkinter import *

root =Tk()
root.geometry('500x700')
root.title('Test Marks')
root.config(background='white')

frame = Frame(root, background='white')
frame.pack()

def totalscore():
    mathscore = int(mathsentry.get())
    englishscore = int(englishentry.get())
    sciencescore = int(scienceentry.get())
    artscore = int(artentry.get())
    computingscore = int(computingentry.get())
    totalscore = mathscore+englishscore+sciencescore+artscore+computingscore
    totalscorelabel.config(text = 'Total Score: '+ str(totalscore))

def meanscore():
    mathscore = int(mathsentry.get())
    englishscore = int(englishentry.get())
    sciencescore = int(scienceentry.get())
    artscore = int(artentry.get())
    computingscore = int(computingentry.get())
    totalscore = mathscore+englishscore+sciencescore+artscore+computingscore
    meanscore = totalscore/5
    meanscorelabel.config(text = 'Mean Score:'+ str(meanscore))

mathslabel = Label(frame ,text = 'Maths: ', fg = 'black', bg = 'white', bd = 15)
mathslabel.grid(row = 0, column = 0)

mathsentry = Entry(frame, fg = 'black', bg = 'white')
mathsentry.grid(row = 0, column = 1)

englishlabel = Label(frame, text = 'English: ',fg  = 'black', bg= 'white', bd = 15)
englishlabel.grid(row = 1, column = 0)

englishentry =Entry(frame, fg = 'black', bg = 'white')
englishentry.grid(row = 1, column =1)

sciencelabel = Label(frame, text = 'Science:', fg = 'black', bg= 'white', bd = 15)
sciencelabel.grid(row = 2, column  =0)

scienceentry = Entry(frame, fg = 'black', bg = 'white')
scienceentry.grid(row = 2, column = 1)

computinglabel = Label(frame, text = 'Computing: ', fg = 'black', bg= 'white', bd = 15)
computinglabel.grid(row = 3, column = 0)

computingentry = Entry(frame, fg = 'black', bg = 'white')
computingentry.grid(row = 3, column = 1)

artlabel = Label(frame, text = 'Art: ', fg = 'black', bg = 'white', bd =15)
artlabel.grid(row = 4, column = 0)

artentry = Entry(frame, fg = 'black', bg = 'white')
artentry.grid(row = 4, column= 1)

totalscorebutton = Button(frame, text = 'Total', fg ='black', bg = 'white', bd = 15, command=totalscore)
totalscorebutton.grid(row = 5, column = 0)

meanscorebutton = Button(frame, text = 'Mean Score', fg = 'black', bg = 'white', bd = 15, command = meanscore)
meanscorebutton.grid(row = 5, column = 1)

totalscorelabel = Label(frame, text = 'Total Score: ', fg = 'black', bg ='white', bd = 15)
totalscorelabel.grid(row = 6, column = 0)

meanscorelabel  = Label(frame, text = 'Mean Score: ', fg = 'black', bg = 'white', bd = 15)
meanscorelabel.grid(row = 6,column = 1)

root.mainloop()
