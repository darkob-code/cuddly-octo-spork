#button

from tkinter import *

count = 0
def click():
    global count
    count+=1
    label.config(text=count)
    
window = Tk()
button = Button(window, text='Click Me')
button.config(command=click)

label = Label(window, text=count)
label.config(font=('Forte',50))
label.pack()
button.pack()
window.mainloop()
