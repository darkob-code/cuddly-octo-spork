from tkinter import*
def zbroji():
    zbroj=int(b1.get())+int(b2.get())
    a3=Label(t, text=str(zbroj))
    a3.place(x=120,y=150)
    return
def oduzmi():
    razlika=int(b1.get())-int(b2.get())
    a4=Label(t, text=str(razlika))
    a4.place(x=120,y=150)
    return
def podijeli():
    kolicnik=int(b1.get())//int(b2.get())
    a5=Label(t, text=str(kolicnik))
    a5.place(x=120,y=150)
def pomnozi():
    produkt=int(b1.get())*int(b2.get())
    a6=Label(t, text=str(produkt))
    a6.place(x=120,y=150)
    return
## napravi prozor
t=Tk()
t.config(width=300, height=200)
## napravi prvi tekstni okvir
a1=Label(t, text='Unesi prvi broj:')
a1.place(x=0,y=0)
## napravi prvo polje za unos tekstualnog sadrÅ¾aja
b1=Entry(t)
b1.place(x=120, y=0)
## napravi drugi tekstni okvir
a2=Label(t, text='Unesi drugi broj:')
a2.place(x=0,y=50)
##napravi drugo polje za unos tekstualnog sadrÅ¾aja
b2=Entry(t)
b2.place(x=120,y=50)
## napravi gumb Zbroji; klikom na gumb izvedi funkciju zbroji()
g=Button(t, text='Zbroji', command=zbroji)
g.place(x=0,y=100)
## napravi gumb Oduzmi; klikom na gumb izvedi funkciju oduzmi()
g=Button(t, text='Oduzmi', command=oduzmi)
g.place(x=50,y=100)
## napravi gumb Podijeli; klikom na gumb izvedi funkciju podijeli()
g=Button(t, text='Podijeli', command=podijeli)
g.place(x=110,y=100)
## napravi gumb Pomnozi; klikom na gumb izvedi funkciju pomnozi()
g=Button(t, text='Pomnozi', command=pomnozi)
g.place(x=170,y=100)
