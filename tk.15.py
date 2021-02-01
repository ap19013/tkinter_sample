import tkinter as tk
root=tk.Tk()
root.geometry('250x250')
ms_dict={}

for bw_int in range(1,6):
    bw_str =str(bw_int)
    ms_dict[bw_str]=tk.Message(text='borderwidge='+bw_str,relief='ridge',width=150,bd=bw_int)
    ms_dict[bw_str].pack()

root.mainloop()