from turtle import*
from tkinter import*
def Kruznica():
    circle(100)
    return
def Kvadrat():
    for i in range(4):
        fd(100)
        lt(90)
    return
t=Tk()
t.title('Proba')
t.config(bg='blue', width=200, height=200, cursor='plus')
g=Button(t, text='Crtaj', font=('Arial',14,'bold'), command=Kruznica)
g.place(x=50, y=100, width=100, height=30)
g1=Button(t, text='Kvadrat', font=('Arial',14,'bold'), command=Kvadrat)
g1.place(x=50, y=150, width=100, height=30)
t.mainloop()
