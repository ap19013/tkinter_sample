import tkinter as tk

def action_btn_press():
    print('Button was pressed')

root=tk.Tk()
root.title('Widget creation')
root.geometry('350x150')
lb=tk.Label(text='Label-1')
bt1=tk.Button(text='Button')
bt2=tk.Button(text='Button')
bt=tk.Button(text='ボタン',command=action_btn_press)
lb.pack()
bt1.pack()
bt2.pack()
bt.pack()
root.mainloop()