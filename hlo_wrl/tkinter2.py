from tkinter import *
window=Tk()
window.geometry("300x200")
window.title("Welcom to Python Class")
lbl=Label(window,text="Hello ")
lbl.grid(row=0,column=0)
txt=Entry(window,width=10)
txt.grid(column=0,row=1)
def click():
    lbl.configure(text="Button was clicked!!")
button=Button(window,text="Click Me",command=click).grid(column=0,row=2)    
window.mainloop()

