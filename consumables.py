import customtkinter as ctk
import tkinter as tk

# Create the main application window
app = ctk.CTk()
app.geometry("560x320")
app.title("Decepticlone for Agumon")

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main frame to hold all elements
main_frame = ctk.CTkFrame(
    app, width=360, height=280, corner_radius=6, fg_color="#2D2D2D"
)
main_frame.pack(padx=10, pady=10)

# First column frame
column1_frame = ctk.CTkFrame(main_frame)
column1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Second column frame
column2_frame = ctk.CTkFrame(main_frame)
column2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


def create_button_row(
    parent, button1_text, button2_text, button1_command, button2_command
):
    """
    Create a row with two buttons side by side.

    Parameters:
    - parent: The parent widget where the buttons will be placed.
    - button1_text: Text for the first button.
    - button2_text: Text for the second button.
    - button1_command: Command to be executed when the first button is pressed.
    - button2_command: Command to be executed when the second button is pressed.
    """

    # Create a frame to hold the buttons
    button_frame = ctk.CTkFrame(parent)
    button_frame.pack(pady=10)  # Adjust padding as needed

    # Create the first button
    button1 = ctk.CTkButton(button_frame, text=button1_text, command=button1_command)
    button1.grid(row=0, column=0, padx=5)  # Adjust padding as needed

    # Create the second button
    button2 = ctk.CTkButton(button_frame, text=button2_text, command=button2_command)
    button2.grid(row=0, column=1, padx=5)  # Adjust padding as needed

    return button_frame
def on_button1_click():
    print("Button 1 clicked")

def on_button2_click():
    print("Button 2 clicked")

# Define the function to create a row with a button, checkbox, and label
def create_row(parent, button_text, label_text):
    row_frame = ctk.CTkFrame(parent)
    row_frame.pack(fill="x", pady=2)

    button = ctk.CTkButton(
        row_frame,
        text=button_text,
        width=28,
        height=24,
        corner_radius=6,
        fg_color="#02BBB9",
        font=("Arial", 12),
    )
    button.pack(side="left", padx=2)

    checkbox = ctk.CTkCheckBox(row_frame, text="")
    checkbox.pack(side="left", padx=2)

    label = ctk.CTkLabel(
        row_frame, text=label_text, text_color="white", font=("Arial", 12)
    )
    label.pack(side="left", padx=2)


# Add rows to the first column
create_row(column1_frame, "F2", "Union Wealth")
create_row(column1_frame, "F2", "Union EXP")
create_row(column1_frame, "F3", "Mushroom Buff")
create_row(column1_frame, "F4", "MVP 50% EXP")
create_row(column1_frame, "F5", "Yellow Potion")
create_row(column1_frame, "F6", "2X EXP (30m)")
create_row(column1_frame, "F7", "2X EXP (15m)")
create_row(column1_frame, "F8", "EB BOX")
create_row(column1_frame, "F9", "Ignition Ring")

# Add a row to the second column
create_row(column2_frame, "", "Wealth Acquisition Potion")
create_row(column2_frame, "", "EXP Accumulation Potion")
create_row(column2_frame, "", "Noblesse Skill 1 (1h)")
create_row(column2_frame, "", "Noblesse Skill 2 (1h)")
create_row(column2_frame, "", "Custom Slot")
create_row(column2_frame, "", "Use Potion?")
create_row(column2_frame, "", "Use Pet Food?")
create_button_row(column2_frame, "Enable All", "Disable All", on_button1_click, on_button2_click)


# Start the main event loop
app.mainloop()
