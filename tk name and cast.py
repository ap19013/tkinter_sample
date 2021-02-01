#p4 tk07

import tkinter as tk

def print_txtval():
    val_en1=en1.get()
    val_en2=en2.get()
    print(val_en1,val_en2)

root=tk.Tk()
root.title('get text box')
root.geometry('550x150')

lb1=tk.Label(text='Name')
en1=tk.Entry()
lb2=tk.Label(text='Cast')
en2=tk.Entry()
bt=tk.Button(text='button',command=print_txtval)
#[widget.pack() for widget in [lb,en,bt]]
#[lb.pack(),en.pack(),bt.pack()]
lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
bt.pack()
root.mainloop()