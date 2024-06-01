import customtkinter
import asyncio
import tkinter
from tkinter import Frame, Label
from PIL import Image, ImageTk
import cv2
import numpy as np

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
        self.geometry("500x500")
        self.title("chrome")
        
        
        frame1 = customtkinter.CTkFrame(self, fg_color='green', width=170, height=70, corner_radius=5)
        # frame1.grid_propagate(False)
        # frame1.grid_columnconfigure(0,weight=1)
        # frame1.grid_columnconfigure(1,weight=1)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        # # frame2 = customtkinter.CTkFrame(self.tab_2, fg_color='transparent', width=170, height=110, corner_radius=5)
        # frame2 = customtkinter.CTkFrame(self.tab_2, fg_color='lime', width=170, height=110, corner_radius=5)
        # frame2.grid_propagate(False)
        # frame2.grid(row=1,column=0,padx=0,pady=0)
        # frame3 = customtkinter.CTkFrame(self.tab_2, fg_color='khaki', width=170, height=180, corner_radius=5)
        # frame3.grid_propagate(False)
        # frame3.grid(row=0,column=1, rowspan=2, padx=0,pady=0)

        # label1 = customtkinter.CTkLabel(frame1, text='Class Required Skills', font=('Arial', 12, 'bold'), height=20)
        # label1.grid(row=0,column=0, padx=4,pady=0, sticky='w')
        sframe1 = customtkinter.CTkScrollableFrame(frame1, fg_color='purple', width=146, height=30, corner_radius=5)
        sframe1.grid(row=0,column=0,padx=1,pady=0)
        sframe1._scrollbar.configure(height=0)
        # sframe1.grid_rowconfigure(0, weight=1)
        # sframe1.grid_columnconfigure(0, weight=1)
        self.entrylist=[]
        for i in range(10):
            entry1 = customtkinter.CTkEntry(sframe1, width=60)
            entry1.grid(row=i,column=0,padx=1,pady=(1,0))
            self.entrylist.append(entry1)
            entrylabel1 = customtkinter.CTkLabel(sframe1, width=70, text='text')
            entrylabel1.grid(row=i,column=1,padx=1,pady=(1,0))
    



async def main():
    decepticlone = Decepticlone()
    decepticlone.mainloop()
    

if __name__ == "__main__":
    asyncio.run(main())







