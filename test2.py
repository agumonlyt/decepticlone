import customtkinter
import asyncio
import tkinter
from tkinter import Frame, Label
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



# Colors
WHITE = "#FFFFFF"
DARK_BLUE = "#031249"
DARK = "#212121"
SECOND_DARK_BLUE = "#142455"

# Custom Title Bar
class TitleBar(Frame):
    def __init__(self, parent, title:str):
        self.root = parent
        self.root.overrideredirect(True) # For Remove Default Title Bar
        super().__init__(parent, bg=DARK)
        self.nav_title = Label(self, text=title, foreground=WHITE, background=DARK)        
        self.nav_title.bind("<ButtonPress-1>", self.oldxyset_label)
        self.nav_title.bind("<B1-Motion>", self.move)        
        self.nav_title.pack(side="left", padx=(10), pady=0)
        
        # self.nav_title.bind("<Map>", self.restore_window)
        # self.nav_title.bind("<Button-3>", self.restore_window2)
        
        customtkinter.CTkButton(self, text='✕', cursor="hand2", corner_radius=5, fg_color=DARK,
                  hover_color=SECOND_DARK_BLUE, width=40, command=self.close_window).pack(side="right",padx=0, pady=0)
        # customtkinter.CTkButton(self, text='——', cursor="hand2", corner_radius=5, fg_color=DARK_BLUE,
        #           hover_color=SECOND_DARK_BLUE, width=40, command=self.minimize_window).pack(side="right")
        self.bind("<ButtonPress-1>", self.oldxyset)
        self.bind("<B1-Motion>", self.move)

    def oldxyset(self, event):
        self.oldx = event.x 
        self.oldy = event.y

    def oldxyset_label(self, event):
        self.oldx = event.x + self.nav_title.winfo_x()
        self.oldy = event.y + self.nav_title.winfo_y()
        
    def move(self, event):
        self.y = event.y_root - self.oldy
        self.x = event.x_root - self.oldx
        self.root.geometry(f"+{self.x}+{self.y}")
    
    def close_window(self):
        self.root.destroy()

    def minimize_window(self):
        # self.root.overrideredirect(0)
        # self.root.iconify()
        self.root.withdraw()

    def restore_window(self,event):
        self.root.overrideredirect(1)

    def restore_window2(self,event):
        self.root.deiconify()
        self.root.overrideredirect(0)








class Decepticlone(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("360x280")
        self.title("chrome")
        titlebar = TitleBar(self, title="DECEPTICLONE")
        titlebar.pack(fill="both")
        tabview = customtkinter.CTkTabview(master=self, corner_radius=5)
        tabview._outer_spacing=0
        tabview.pack(padx=0, pady=0)        
        self.tab_1 = tabview.add("Controls")  # add tab at the end
        self.tab_2 = tabview.add("Skills")  # add tab at the end
        self.tab_3 = tabview.add("Consumables")  # add tab at the end
        self.tab_4 = tabview.add("Settings")  # add tab at the end
        self.tab_5 = tabview.add("Modules")  # add tab at the end
        self.tab_6 = tabview.add("+")  # add tab at the end
        tabview.set("Controls")  # set currently visible tab
        # self.tab_1.grid_columnconfigure(0,weight=1)
        # self.tab_1.grid_columnconfigure(1,weight=1)
        self.setup_tab1()

    def setup_tab1(self):

        frameright2 = customtkinter.CTkFrame(self.tab_1, fg_color='#f231ff', height=110, width=170)
        frameright2.grid_propagate(False)
        # frameright2.rowconfigure(0, weight=1)
        # frameright2.columnconfigure(0, weight=1)
        frameright2.grid(row=1,column=0,padx=(1,1),pady=(0,0))

        frame2image = customtkinter.CTkImage(light_image=Image.open('minimap.png'), dark_image=Image.open('minimap.png'), size=(170,110))
        canvas = tkinter.Canvas(frameright2, borderwidth=0, highlightthickness=0, relief='ridge')
        # canvas.pack(padx=(0,0),pady=(0,0), anchor='nw', fill='both', expand=1)
        canvas.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='nw')
        image = Image.open('minimap.png')
        # imageresized = image.resize((170,110), Image.LANCZOS)
        imagetk = ImageTk.PhotoImage(image)
        canvas.create_image(0,0,image=imagetk, anchor='nw')

        pass


async def main():
    decepticlone = Decepticlone()
    decepticlone.mainloop()


if __name__ == "__main__":
    asyncio.run(main())







