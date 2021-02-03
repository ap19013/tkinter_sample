#
"
"
import tkinter as tk
def print_txtval():
    val_id=en1.get()
    val_name=en2.get()
    print('User id:{} Name:{} '.format(val_id,val_name))
root=tk.Tk()
root.geometry('350x150')

lb1=tk.Label(text='User Id')
en1=tk.Entry()
lb2=tk.Label(text='Name')
en2=tk.Entry()

bt=tk.Button(text='Enter Data',command=print_txtval)
lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
bt.pack()
root.mainloop()


root.mainloop()