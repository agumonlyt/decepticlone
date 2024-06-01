from CTkSpinbox import CTkSpinbox
from customtkinter import CTkFrame, CTkLabel
import customtkinter
import tkinter
from bumblebee.spinbox.BumblebeeSpinbox import BBBSpinbox
import ttkbootstrap as tb

# Create the main window
root = customtkinter.CTk()
root.geometry("400x400")  # Set window size (optional)
root.title("CTkSpinbox Example")

# Create a frame
frame = CTkFrame(master=root)
frame.pack(fill="both", expand=True)  # Fill and expand the frame

# Create a label
label = CTkLabel(master=frame, text="Value:")
label.pack(pady=5)

# Create a spinbox
spinbox = CTkSpinbox(
    master=frame,
    start_value=10,
    min_value=0,
    max_value=20,
    scroll_value=2,  # Increment/decrement by 2
    variable=tkinter.IntVar(),  # Use a CTk or Tk variable
    command=lambda value: print(f"Selected value: {value}"),  # Optional command
)
spinbox.pack(pady=5)

spinbox_1 = BBBSpinbox(root, width=150, step_size=3)
spinbox_1.pack(padx=20, pady=20)

spinbox_1.set(35)
print(spinbox_1.get())

spinbox1values=['1800s','900s','300s','150s','60s']
spinbox1 = tb.Spinbox(root, font=('Helvetica',18), from_=0, to=10, values=spinbox1values, state='readonly')
spinbox1.pack(padx=20, pady=20)

# Start the main event loop
root.mainloop()



