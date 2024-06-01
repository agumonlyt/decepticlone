import tkinter as tk
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import CTkSpinbox
# from bumblebee.spinbox.BumblebeeSpinbox import BBBSpinbox
import customtkinter
from tkinter import Tk, ttk



class Decepticlone(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        # self.geometry("360x300")
        self.geometry("460x320")
        self.title("chrome")
        # titlebar = TitleBar(self, title="DECEPTICLONE")
        # titlebar.pack(fill="both")
        tabview = customtkinter.CTkTabview(master=self, corner_radius=5)
        tabview._outer_spacing=0
        tabview.pack(padx=0, pady=0)        
        self.tab_1 = tabview.add("Controls")
        self.tab_2 = tabview.add("Skills")
        self.tab_3 = tabview.add("Consumables")
        self.tab_4 = tabview.add("Settings")
        self.tab_5 = tabview.add("Modules")
        self.tab_6 = tabview.add("+")
        tabview.set("Consumables")


# d = Decepticlone()
# d.mainloop()

root = Tk()
root.title("Notebook Example")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create frames and labels for two tabs
frame1 = ttk.Frame(root)
label1 = ttk.Label(frame1, text="This is tab 1 content")
label1.pack()

frame2 = ttk.Frame(root)
label2 = ttk.Label(frame2, text="This is tab 2 content")
label2.pack()

# Add tabs to the notebook
notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")

root.mainloop()

