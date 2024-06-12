from tkinter import ttk, Tk

window = Tk()
style = ttk.Style()
style.configure("TScale", background="#505050")
scale = ttk.Scale(window, from_=0, to=100, value=0, orient="horizontal", style="TScale")
scale.pack()

window.mainloop()