import tkinter as tk
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import CTkSpinbox
# from bumblebee.spinbox.BumblebeeSpinbox import BBBSpinbox

root = tk.Tk()
# root = tb.Window(themename='darkly')
root.geometry("400x300")

# b1 = tb.Button(root, text="Button 1", bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)
# b2 = tb.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
# b2.pack(side=LEFT, padx=5, pady=10)
# b1 = tb.Button(root, text='primary', bootstyle=PRIMARY)
# b1.pack(side=LEFT, padx=5, pady=5)
# b2 = tb.Button(root, text='secondary', bootstyle=SECONDARY)
# b2.pack(side=LEFT, padx=5, pady=5)
# b3 = tb.Button(root, text='success', bootstyle=SUCCESS)
# b3.pack(side=LEFT, padx=5, pady=5)
# b4 = tb.Button(root, text='info', bootstyle=INFO)
# b4.pack(side=LEFT, padx=5, pady=5)
# b5 = tb.Button(root, text='warning', bootstyle=WARNING)
# b5.pack(side=LEFT, padx=5, pady=5)
# b6 = tb.Button(root, text='danger', bootstyle=DANGER)
# b6.pack(side=LEFT, padx=5, pady=5)
# b7 = tb.Button(root, text='light', bootstyle=LIGHT)
# b7.pack(side=LEFT, padx=5, pady=5)
# b8 = tb.Button(root, text='dark', bootstyle=DARK)
# b8.pack(side=LEFT, padx=5, pady=5)
# b9 = tb.Button(root, text='outline', bootstyle=(SUCCESS,OUTLINE))
# b9.pack(side=LEFT, padx=5, pady=5)
# for color in root.style.colors:
#     b = tb.Button(root, text=color, bootstyle=color)
#     b.pack(side=LEFT, padx=5, pady=5)


spinbox1values=['1800s','900s','300s','150s','60s']
# spinbox1 = CTkSpinbox.CTkSpinbox(root, font=('Helvetica',12), min_value=0, max_value=10,
# state='readonly')
# spinbox1.pack(padx=20, pady=20)
# spinbox2 = tb.Spinbox(root, font=('Helvetica',12), from_=0, to=10, values=spinbox1values, 
# state='readonly')
# spinbox2.pack(padx=20, pady=20)
# spinbox4 = BBBSpinbox(root, width=8)
# spinbox4.pack(padx=20, pady=20)
# spinbox3 = tk.Spinbox(root, from_=0, to=10, width=8, values=spinbox1values, buttonbackground='#2d2d2d', fg='#f1ff21', bg='#2d2d2d',
spinbox3 = tk.Spinbox(root, from_=0, to=10, width=8, values=spinbox1values, buttonbackground='#2d2d2d', fg='#f1ff21', bg='pink',
bd=0, font=('Helvetica',8))
spinbox3.pack(padx=20, pady=20)
spinbox5 = tk.Spinbox(root, from_=0, to=10, width=8, bg='#f1ff21', fg='#a3b9fa', values=spinbox1values, 
buttonbackground='#2ff12f', bd=0, font=('Helvetica',12))
spinbox5.pack(padx=20, pady=20)
spinbox6 = tk.Spinbox(root, font=('Helvetica',14), width=6, from_=0, to=10, values=spinbox1values, 
bd=0, bg='#212121')
# state='readonly', bg='#fcfccf', buttonbackground='#2ff12e', fg='#aa3ffa', bd=0)
spinbox6.pack(padx=20, pady=20)




root.mainloop()