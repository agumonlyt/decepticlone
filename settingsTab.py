import customtkinter as ctk

def create_checkbox_row(parent, text):
    """
    Create a row with a checkbox and a label.
    
    Parameters:
    - parent: The parent widget where the row will be placed.
    - text: The text for the label next to the checkbox.
    """
    row_frame = ctk.CTkFrame(parent)
    row_frame.pack(fill='x', pady=5)  # Adjust padding as needed
    
    checkbox = ctk.CTkCheckBox(row_frame, text="")
    checkbox.configure(font=("Arial", 12))
    checkbox.grid(row=0, column=0, padx=(0, 2), sticky='w')  # Minimal padding

    label = ctk.CTkLabel(row_frame, text=text)
    label.configure(font=("Arial", 12))
    label.grid(row=0, column=1, sticky='w')

    return row_frame

# Create the main window
app = ctk.CTk()
app.title("CustomTkinter Example")
app.geometry("600x400")

# Create the main frame
main_frame = ctk.CTkFrame(app, width=560, height=320, corner_radius=6)
main_frame.pack(padx=20, pady=20)
main_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its children

# Create two columns
left_column = ctk.CTkFrame(main_frame)
left_column.pack(side='left', fill='y', expand=True, padx=10, pady=10)

right_column = ctk.CTkFrame(main_frame)
right_column.pack(side='left', fill='y', expand=True, padx=10, pady=10)

# Add rows to the left column
create_checkbox_row(left_column, "Bounty Hunter")
sub_frame = ctk.CTkFrame(left_column)
sub_frame.pack(padx=10, pady=5)
create_checkbox_row(sub_frame, "Polo")
create_checkbox_row(sub_frame, "Especia")
create_checkbox_row(left_column, "Auto HP/MP")
create_checkbox_row(left_column, "Auto CC")
create_checkbox_row(left_column, "Auto TP")

# Add rows to the right column
create_checkbox_row(right_column, "Rune Solver")
create_checkbox_row(right_column, "LD Detection")
create_checkbox_row(right_column, "Auto Unstuck")
create_checkbox_row(right_column, "White Room")
create_checkbox_row(right_column, "Map Change")
create_checkbox_row(right_column, "Chat Reader")
create_checkbox_row(right_column, "Admin NPC Detect")

# Start the application
app.mainloop()
