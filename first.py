from tkinter import *
root = Tk()
root.title("Free Fire")

lbl = Label(root, text = "Are you a Begniner Or Profesional?")
lbl.grid()
def clicked():
    lbl.configure(text = "Headshot")
 
# button widget with red color 
# inside
btn = Button(root, text = "Fire Button" ,fg = "red", command=clicked)
             
# set Button grid
btn.grid(column=1, row=0)
root.geometry('2000x2000')
root.mainloop()