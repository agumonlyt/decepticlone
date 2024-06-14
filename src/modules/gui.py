import customtkinter
import asyncio
import tkinter
from tkinter import Frame, Label
from PIL import Image, ImageTk
from bumblebee import customtkinter as bumblebeetkinter
from src.common import config
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



WHITE = "#FFFFFF"
DARK_BLUE = "#031249"
DARK = "#212121"
SECOND_DARK_BLUE = "#142455"


class TitleBar(Frame):
    def __init__(self, parent, title:str):
        self.root = parent
        self.root.overrideredirect(True) # For Remove Default Title Bar
        super().__init__(parent, bg=DARK)
        self.nav_title = Label(self, text=title, foreground=WHITE, background=DARK)        
        self.nav_title.bind("<ButtonPress-1>", self.oldxyset_label)
        self.nav_title.bind("<B1-Motion>", self.move)        
        self.nav_title.pack(side="left", padx=(10), pady=0)
                
        customtkinter.CTkButton(self, text='✕', cursor="hand2", corner_radius=5, fg_color=DARK,
                  hover_color=SECOND_DARK_BLUE, width=40, command=self.close_window).pack(side="right",padx=0, pady=0)
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
        self.root.withdraw()

    def restore_window(self,event):
        self.root.overrideredirect(1)

    def restore_window2(self,event):
        self.root.deiconify()
        self.root.overrideredirect(0)

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, mylabeltext2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.title("chrome")
        titlebar = TitleBar(self, title="DECEPTICLONE")
        titlebar.pack(fill="both")

        print(args)
        print(kwargs)
        print(mylabeltext2)

        self.label1 = customtkinter.CTkLabel(self, text="Press any key to bind")
        self.label1.pack(padx=20, pady=20)
        self.label2 = customtkinter.CTkLabel(self, text=f'{mylabeltext2}')
        self.label2.pack(padx=20, pady=20)
        self.label3 = customtkinter.CTkLabel(self, text="Press ESC to cancel.\n\n Waiting ...")
        self.label3.pack(padx=20, pady=20)










class GUI(customtkinter.CTk):

    def __init__(self):
        config.gui = self
        super().__init__()
        self.geometry("400x320")
        self.title("chrome")
        titlebar = TitleBar(self, title="DECEPTICLONE")
        titlebar.pack(fill="both")
        tabview = customtkinter.CTkTabview(master=self, width=400, height=180, corner_radius=5, border_width=0)
        tabview._outer_spacing=0
        tabview.pack(padx=0, pady=0)
        self.tab_1 = tabview.add("Controls")
        self.tab_2 = tabview.add("Skills")
        self.tab_3 = tabview.add("Consumables")
        self.tab_4 = tabview.add("Settings")
        self.tab_5 = tabview.add("Modules")
        self.tab_6 = tabview.add("+")
        tabview.set("Controls")
        
    def setup_tab6(self):
        frame1 = customtkinter.CTkFrame(self.tab_6, fg_color='transparent', width=180, height=216, corner_radius=5)
        frame1.grid_propagate(False)
        frame1.grid_columnconfigure(0,weight=1)
        frame1.grid_columnconfigure(1,weight=1)
        frame1.grid_columnconfigure(2,weight=1)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        frame2 = customtkinter.CTkFrame(self.tab_6, fg_color='transparent', width=210, height=216, corner_radius=5)
        frame2.grid_propagate(False)
        frame2.grid_columnconfigure(0,weight=1)
        frame2.grid_columnconfigure(1,weight=1)
        frame2.grid_columnconfigure(2,weight=1)
        frame2.grid(row=0,column=1, padx=0,pady=0)



        def create_label(master,button_id,text='Custom Slot',width=30,anchor='w'):
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12),
            height=11, anchor=anchor, bg_color='transparent',width=width)
            return label1
        def create_checkbox(master,button_id,bd_width=0,bd_color='#3a8b83'):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=bd_width, border_color=bd_color, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id,width=40,text=None):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                    button1.configure(text=f'{button_id}')
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=width, height=20, border_width=0, text=text, command=lambda: button_command1(),
            font=('Arial', 11), fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
            return button1
        def create_slider(master):            
            def sliding(value):
                value=int(value)
                print(value)
            slider1 = customtkinter.CTkSlider(master,from_=0,to=80,command=sliding,number_of_steps=100,width=95,height=10,
            fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
            return slider1

        label1 = create_label(frame1,button_id=0,text='Volume Controls',anchor='center')
        label1.grid(row=0,column=0,columnspan=3,padx=(0,0),pady=(4,4), sticky='ew')
        label2 = create_label(frame2,button_id=0,text='Tools',anchor='center')
        label2.grid(row=0,column=0,columnspan=3,padx=(0,0),pady=(4,4), sticky='ew')

        labellist1=['LD/GM','Player','Presence']
        for i in range(3):
            label3 = create_label(frame1,0,text=labellist1[i], width=30)
            label3.grid(row=i+1,column=0,padx=(5,0),pady=(4,0), sticky='w')
            checkbox1 = create_checkbox(frame1,0,bd_width=1)
            checkbox1.grid(row=i+1,column=1,padx=(2,2),pady=(4,0), sticky='w')
            slider1=create_slider(frame1)
            slider1.grid(row=i+1,column=2,padx=(0,0),pady=(4,0), sticky='w')

        label4 = create_label(frame1,0,text='PRO', width=30)
        label4.grid(row=5,column=0,padx=(5,0),pady=(4,0), sticky='w')

        button = create_button(frame1,i,text='Monster Life',width=75)
        button.grid(row=6,column=0,columnspan=3,padx=(4,0),pady=(2,0), sticky='w')
        button1 = create_button(frame1,i,text='Harvesting',width=75)
        button1.grid(row=7,column=0,columnspan=3,padx=(4,0),pady=(2,0), sticky='w')

        frame2a = customtkinter.CTkFrame(frame2, fg_color='transparent', width=209, height=25, corner_radius=0)
        frame2a.grid_propagate(False)
        frame2a.grid(row=1,column=0,columnspan=3,padx=0,pady=0)
        button2 = create_button(frame2a,i,text='LD Reset',width=75)
        button2.grid(row=0,column=0,padx=(1,0),pady=(2,0), sticky='w')
        button3 = create_button(frame2a,i,text='Manage Sub',width=75)
        button3.grid(row=0,column=1,padx=(1,0),pady=(2,0), sticky='w')

        for i in range(1):
            checkbox1 = create_checkbox(frame2,0,bd_width=1)
            checkbox1.grid(row=2,column=0,padx=(2,0),pady=(4,0), sticky='w')
            label3 = create_label(frame2,0,text='Auto Reply', width=80)
            label3.grid(row=2,column=1,padx=(2,0),pady=(4,0), sticky='w')
        spinbox1values=['60min','120min','150min','300min','600min','900min','1800min']
        labellist2=['Scheduled CC','Scheduled Town','Scheduled Status']
        for i in range(3):
            checkbox1 = create_checkbox(frame2,0,bd_width=1)
            checkbox1.grid(row=i+3,column=0,padx=(2,0),pady=(4,0), sticky='w')
            label3 = create_label(frame2,0,text=labellist2[i], width=30)
            label3.grid(row=i+3,column=1,padx=(2,0),pady=(4,0), sticky='w')
            spinbox1_var = tkinter.StringVar(frame2)
            spinbox1 = tkinter.Spinbox(frame2, font=('Helvetica',10), width=7, from_=0, to=10, values=spinbox1values, textvariable=spinbox1_var, 
            state='readonly', bd=0, buttonbackground='#212121', fg='#fffeee', bg='#212121', readonlybackground='#212121')
            spinbox1.grid(row=i+3,column=2,padx=(1,5),pady=(1,1))
            spinbox1_var.set('60min')
        labellist3=['Mute Non-Important Messages','Old Rune Behaviour']
        for i in range(2):
            checkbox1 = create_checkbox(frame2,0,bd_width=1)
            checkbox1.grid(row=6+i,column=0,padx=(2,0),pady=(4,0), sticky='w')
            label3 = create_label(frame2,0,text=labellist3[i], width=190)
            label3.grid(row=6+i,column=1,columnspan=2,padx=(2,0),pady=(4,0), sticky='w')

    def setup_tab5(self):
        frame1 = customtkinter.CTkFrame(self.tab_5, fg_color='transparent', width=127, height=216, corner_radius=5)
        frame1.grid_propagate(False)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        frame2 = customtkinter.CTkFrame(self.tab_5, fg_color='transparent', width=127, height=216, corner_radius=5)
        frame2.grid_propagate(False)
        frame2.grid(row=0,column=1, padx=0,pady=0)
        frame3 = customtkinter.CTkFrame(self.tab_5, fg_color='transparent', width=136, height=216, corner_radius=5)
        frame3.grid_propagate(False)
        frame3.grid(row=0,column=2, padx=0,pady=0)

        frame1a = customtkinter.CTkFrame(frame1, fg_color='transparent', width=123, height=40, corner_radius=5)
        frame1a.grid_propagate(False)
        frame1a.grid(row=0,column=0,padx=(2,0),pady=(2,0))
        frame2a = customtkinter.CTkFrame(frame2, fg_color='transparent', width=123, height=40, corner_radius=5)
        frame2a.grid_propagate(False)
        frame2a.grid(row=0,column=0, padx=(2,0),pady=(2,0))
        frame3a = customtkinter.CTkFrame(frame3, fg_color='transparent', width=132, height=40, corner_radius=5)
        frame3a.grid_propagate(False)
        frame3a.grid(row=0,column=0, padx=(2,0),pady=(2,0))

        frame1b = customtkinter.CTkFrame(frame1, fg_color='transparent', width=126, height=175, corner_radius=5)
        frame1b.grid_propagate(False)
        frame1b.grid(row=1,column=0,padx=0,pady=0)
        frame2b = customtkinter.CTkFrame(frame2, fg_color='transparent', width=126, height=175, corner_radius=5)
        frame2b.grid_propagate(False)
        frame2b.grid(row=1,column=0, padx=0,pady=0)
        frame3b = customtkinter.CTkFrame(frame3, fg_color='transparent', width=135, height=175, corner_radius=5)
        frame3b.grid_propagate(False)
        frame3b.grid(row=1,column=0, padx=0,pady=0)



        def create_label(master,button_id,text='Custom Slot',width=30):
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12), 
            height=11, anchor='w', bg_color='transparent',width=width)
            return label1
        def create_checkbox(master,button_id,bd_width=0,bd_color='#3a8b83'):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=bd_width, border_color=bd_color, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id,width=40):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                    button1.configure(text=f'{button_id}')
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=width, height=20, border_width=0, text='', command=lambda: button_command1(),
            font=('Lucida Console', 10), fg_color='#0bbdb3')
            return button1

        
        
        label1 = create_label(frame1a,button_id=0,text='PRO')
        label1.grid(row=0,column=0,padx=(10,0),pady=(10,0), sticky='nsew')
        label2 = create_label(frame2a,button_id=0,text='PLUS')
        label2.grid(row=0,column=0,padx=(10,0),pady=(10,0), sticky='nsew')
        label3 = create_label(frame3a,button_id=0,text='CORE')
        label3.grid(row=0,column=0,padx=(10,0),pady=(10,0), sticky='nsew')


        checkbox1 = create_checkbox(frame1b,0,bd_width=1)
        checkbox1.grid(row=0,column=0,padx=(5,0),pady=(4,0), sticky='w')
        label1 = create_label(frame1b,0,text='Bounty Hunter', width=110)
        label1.grid(row=0,column=1,padx=(5,0),pady=(4,0), sticky='w')
        
        frame1b1 = customtkinter.CTkFrame(frame1b, fg_color='transparent', width=103, height=38, corner_radius=5)
        frame1b1.grid_propagate(False)
        frame1b1.grid(row=1,column=0,columnspan=2, padx=(10,0),pady=0,sticky='w')

        checkbox2 = create_checkbox(frame1b1,0,bd_width=1)
        checkbox2.grid(row=0,column=0,padx=(5,0),pady=(4,0), sticky='w')
        label2 = create_label(frame1b1,0,text='Polo', width=60)
        label2.grid(row=0,column=1,padx=(5,0),pady=(4,0), sticky='w')
        checkbox3 = create_checkbox(frame1b1,0,bd_width=1)
        checkbox3.grid(row=1,column=0,padx=(5,0),pady=(4,0), sticky='w')
        label3 = create_label(frame1b1,0,text='Especia', width=60)
        label3.grid(row=1,column=1,padx=(5,0),pady=(4,0), sticky='w')

        labellist1=['Auto HP/MP', 'Auto CC', 'Auto TP']
        for i in range(3):
            checkbox1 = create_checkbox(frame1b,0,bd_width=1)
            checkbox1.grid(row=i+3,column=0,padx=(5,0),pady=(4,0), sticky='w')
            label1 = create_label(frame1b,0,text=labellist1[i], width=60)
            label1.grid(row=i+3,column=1,padx=(5,0),pady=(4,0), sticky='w')

        for i in range(1):
            checkbox4 = create_checkbox(frame2b,0,bd_width=1)
            checkbox4.grid(row=i,column=0,padx=(5,0),pady=(4,0), sticky='w')
            label4 = create_label(frame2b,0,text="Rune Solver", width=60)
            label4.grid(row=i,column=1,padx=(5,0),pady=(4,0), sticky='w')

        labellist2=['LD Detection', 'Auto Unstuck', 'White Room', 'Map Change', 'Chat Reader', 'Admin NPC Detect']
        for i in range(6):
            checkbox4 = create_checkbox(frame3b,0,bd_width=1)
            checkbox4.grid(row=i,column=0,padx=(5,0),pady=(4,0), sticky='w')
            label4 = create_label(frame3b,0,text=labellist2[i], width=60)
            label4.grid(row=i,column=1,padx=(5,0),pady=(4,0), sticky='w')
        





    def setup_tab4(self):
        frame = customtkinter.CTkScrollableFrame(self.tab_4, fg_color='transparent', width=370, height=190, corner_radius=5)
        frame._scrollbar.configure(height=0)
        frame.grid(row=0,column=0,padx=0,pady=0)
        frame1 = customtkinter.CTkFrame(frame, fg_color='transparent', width=200, height=256, corner_radius=5)
        frame1.grid_propagate(False)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        frame1a = customtkinter.CTkFrame(frame1, fg_color='transparent', width=200, height=135, corner_radius=5)
        frame1a.grid_propagate(False)
        frame1a.grid(row=0,column=0,padx=0,pady=0)
        frame1b = customtkinter.CTkFrame(frame1, fg_color='transparent', width=200, height=120, corner_radius=5)
        frame1b.grid_propagate(False)
        frame1b.grid(row=1,column=0,padx=0,pady=0)
        frame2 = customtkinter.CTkFrame(frame, fg_color='transparent', width=170, height=256, corner_radius=5)
        frame2.grid_propagate(False)
        # frame2.grid_columnconfigure(2,weight=1)
        frame2.grid(row=0,column=1, padx=0,pady=0)
        frame2a = customtkinter.CTkFrame(frame2, fg_color='transparent', width=170, height=135, corner_radius=5)
        frame2a.grid_propagate(False)
        frame2a.grid(row=0,column=0, padx=0,pady=0)
        frame2b = customtkinter.CTkFrame(frame2, fg_color='transparent', width=170, height=120, corner_radius=5)
        frame2b.grid_propagate(False)
        frame2b.grid(row=1,column=0, padx=0,pady=0)

        def create_label(master,button_id,text='Custom Slot',width=30):
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12), 
            height=11, anchor='w', bg_color='transparent',width=width)
            return label1
        def create_checkbox(master,button_id,bd_width=0,bd_color='#3a8b83'):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=bd_width, border_color=bd_color, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id,width=40):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                    button1.configure(text=f'{button_id}')
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=width, height=20, border_width=0, text='', command=lambda: button_command1(),
            font=('Arial', 11), fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
            return button1

        frame_ = customtkinter.CTkFrame(frame1a, fg_color='transparent', width=40, height=20, corner_radius=5)
        frame_.grid_propagate(False)
        frame_.grid(row=0,column=0, padx=0,pady=0)
        button = create_button(frame_,button_id=0,width=19)            
        button.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='w')
        button2 = create_button(frame_,button_id=0,width=20)
        button2.grid(row=0,column=1,padx=0,pady=(0,0), sticky='w')
        label1 = create_label(frame1a,button_id=0,text='Keyboard/Mouse ID')
        label1.grid(row=0,column=1,padx=(5,0),pady=(0,0), sticky='w')
        labellisttxt1 = ['NPC Key*', 'Teleport', 'Rope Connect', 'World Map*', 'Nearest Town Scroll']
        for i in range(5):
            button = create_button(frame1a,i)
            button.grid(row=i+1,column=0,padx=0,pady=(1,0), sticky='w')
            label1 = create_label(frame1a,i,text=labellisttxt1[i])
            label1.grid(row=i+1,column=1,padx=(5,0),pady=(0,0), sticky='w')
        labellisttxt2 = ['Panic Mode', 'CD Reduction', 'Player notification', 'Player Count', 'Buff Duration', 'HP/MP Threshold']
        spinbox1values=['60s','120s','150s','300s','600s','900s','1800s']
        for i in range(6):
            checkbox1 = create_checkbox(frame1b,i,bd_width=1)
            checkbox1.grid(row=i+6,column=0,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame1b,i,text=labellisttxt2[i], width=110)
            label1.grid(row=i+6,column=1,padx=(5,0),pady=(0,0), sticky='w')
            spinbox1_var = tkinter.StringVar(frame1b)
            spinbox1 = tkinter.Spinbox(frame1b, font=('Helvetica',10), width=7, from_=0, to=10, values=spinbox1values, textvariable=spinbox1_var, 
            state='readonly', bd=0, buttonbackground='#212121', fg='#fffeee', bg='#212121', readonlybackground='#212121')
            spinbox1.grid(row=i+6,column=2,padx=(1,5),pady=(1,1))
            spinbox1_var.set('1800s')

        labellisttxt3 = ['Profession Key*', 'Potion Key*', 'Pet Food Key*', 'Jump Key*', 'Safety Charm Key', 'Cash Shop Key']
        for i in range(6):
            button = create_button(frame2a,i)            
            button.grid(row=i,column=0,padx=0,pady=(1,0), sticky='w')
            label1 = create_label(frame2a,i,text=labellisttxt3[i])
            label1.grid(row=i,column=1,padx=(5,0),pady=(0,0), sticky='w')
        labellisttxt4 = ['Have Battleroid?', 'Use Rope for farming?', 'Use combat up jump', 'Death notification', 'Face Outwards?', 
        'Dynamic Rope Connect', 'Ignore Elite Boss?']
        for i in range(7):
            checkbox1 = create_checkbox(frame2b,i,bd_width=1)
            checkbox1.grid(row=i+6,column=0,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame2b,i,text=labellisttxt4[i], width=120)
            label1.grid(row=i+6,column=1,padx=(5,0),pady=(0,2), sticky='w')



    def setup_tab3(self):
        frame1 = customtkinter.CTkFrame(self.tab_3, fg_color='transparent', width=170, height=200, corner_radius=5)
        frame1.grid_propagate(False)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        frame2 = customtkinter.CTkFrame(self.tab_3, fg_color='transparent', width=220, height=200, corner_radius=5)
        frame2.grid_propagate(False)
        frame2.grid_columnconfigure(2,weight=1)
        frame2.grid(row=0,column=1, padx=0,pady=0)


        self.toplevel_window = None

        def create_label(master,button_id,text='Custom Slot'):
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12), 
            height=11, anchor='w', bg_color='transparent')
            return label1
        def create_checkbox(master,button_id):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=0, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                    button1.configure(text=f'{button_id}')
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=30, height=20, border_width=0, text='', command=lambda: button_command1(),
            font=('Arial', 11), fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
            return button1
        self.buttonlist1=[]
        self.entrylist1=[]
        self.checkboxlist1=[]
        labellisttxt = ['Union Wealth', 'Union EXP', 'Mushroom Buff', 'MVP 50% EXP', 'Yellow Potion', '2X EXP (30m)', '2X EXP (15m)', 
        'EB Box', 'Ignition Ring']
        for i in range(9):
            button = create_button(frame1,i)            
            button.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            checkbox1 = create_checkbox(frame1,i)
            checkbox1.grid(row=i,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame1,i,text=labellisttxt[i])
            label1.grid(row=i,column=2,padx=(5,0),pady=(0,0), sticky='w')
        self.entrylist2=[]
        self.checkboxlist2=[]
        labellisttxt2 = ['Wealth Acquisition Potion', 'EXP Accumulation Potion', 'Nobless Skill 1 (1h)', 'Nobless Skill 2 (1h)']
        for i in range(4):
            button = create_button(frame2,i)            
            button.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            checkbox1 = create_checkbox(frame2,i)
            checkbox1.grid(row=i,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame2,i,text=labellisttxt2[i])
            label1.grid(row=i,column=2,columnspan=2,padx=(5,0),pady=(0,0), sticky='w')
        spinbox1values=['60s','120s','150s','300s','600s','900s','1800s']
        for i in range(2):
            button = create_button(frame2,i)            
            button.grid(row=i+4,column=0,padx=0,pady=(2,0), sticky='w')
            checkbox1 = create_checkbox(frame2,i)
            checkbox1.grid(row=i+4,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame2,i,'Custom Slot')
            label1.grid(row=i+4,column=2,padx=(5,0),pady=(0,0), sticky='w')
            spinbox1_var = tkinter.StringVar(frame2)
            spinbox1 = tkinter.Spinbox(frame2, font=('Helvetica',10), width=6, from_=0, to=10, values=spinbox1values, textvariable=spinbox1_var, 
            state='readonly', bd=0, buttonbackground='#212121', fg='#fffeee', bg='#212121', readonlybackground='#212121')
            spinbox1.grid(row=i+4,column=3,padx=(1,5),pady=(1,1))
            spinbox1_var.set('1800s')
        usepotionlist = [f"{i}s" for i in range(10, 301, 10)]
        labellisttxt3 = ['Use Potion?', 'Use Pet Food?']
        for i in range(2):
            checkbox1 = create_checkbox(frame2,i)
            checkbox1.grid(row=i+6,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame2,i,text=labellisttxt3[i])
            label1.grid(row=i+6,column=2,padx=(5,0),pady=(0,0), sticky='w')
            spinbox1_var = tkinter.StringVar(frame2)
            spinbox1 = tkinter.Spinbox(frame2, font=('Helvetica',10), width=6, from_=0, to=10, values=usepotionlist, textvariable=spinbox1_var, 
            state='readonly', bd=0, buttonbackground='#212121', fg='#fffeee', bg='#212121', readonlybackground='#212121')
            spinbox1.grid(row=i+6,column=3,padx=(1,5),pady=(1,1))
            spinbox1_var.set('300s')
        framebutton = customtkinter.CTkFrame(frame2, fg_color='transparent', width=219, corner_radius=5)
        framebutton.grid_propagate(False)
        framebutton.grid_columnconfigure(0,weight=1)
        framebutton.grid_columnconfigure(1,weight=1)
        framebutton.grid(row=9,column=0, columnspan=4, padx=0,pady=0, sticky='w')
        def enableall():
            pass
        buttonenable = customtkinter.CTkButton(framebutton, width=80, border_width=0, text='Enable All', command=enableall,
        font=('Helvetica', 12), fg_color='#0bbdb3', text_color='black', height=20)
        buttonenable.grid(row=0,column=0,padx=(35,5),pady=(5,0), sticky='w')
        def disableall():
            pass
        buttondisable = customtkinter.CTkButton(framebutton, width=80, border_width=0, text='Disable All', command=disableall,
        font=('Helvetica', 12), fg_color='#0bbdb3', text_color='black', height=20)
        buttondisable.grid(row=0,column=1,padx=0,pady=(5,0), sticky='w')




    def setup_tab2(self):
        frame1 = customtkinter.CTkFrame(self.tab_2, fg_color='transparent', width=195, height=70, corner_radius=5)
        frame1.grid_propagate(False)
        frame1.grid_columnconfigure(0,weight=1)
        frame1.grid_columnconfigure(1,weight=1)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        frame2 = customtkinter.CTkFrame(self.tab_2, fg_color='transparent', width=195, height=130, corner_radius=5)
        frame2.grid_propagate(False)
        frame2.grid(row=1,column=0,padx=0,pady=0)
        frame3 = customtkinter.CTkFrame(self.tab_2, fg_color='transparent', width=195, height=200, corner_radius=5)
        frame3.grid_propagate(False)
        frame3.grid_columnconfigure(0, weight=1)
        frame3.grid_columnconfigure(1, weight=1)
        frame3.grid(row=0,column=1, rowspan=2, padx=0,pady=0)

        
        def create_label(master,button_id,text='Custom Slot',width=30,anchor='w'):
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12),
            height=11, anchor=anchor, bg_color='transparent',width=width)
            return label1
        def create_checkbox(master,button_id,bd_width=0,bd_color='#3a8b83'):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=bd_width, border_color=bd_color, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id,width=40,text=None):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                    button1.configure(text=f'{button_id}')
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=width, height=20, border_width=0, text=text, command=lambda: button_command1(),
            font=('Arial', 11), fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
            return button1
        def create_slider(master):            
            def sliding(value):
                value=int(value)
                print(value)
            slider1 = customtkinter.CTkSlider(master,from_=0,to=80,command=sliding,number_of_steps=100,width=95,height=10,
            fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
            return slider1


        label1 = customtkinter.CTkLabel(frame1, text='Class Required Skills', font=('Arial', 12, 'bold'), height=18,text_color='#0e8783')
        label1.grid(row=0,column=0, padx=4,pady=(0,2), sticky='w')
        sframe1 = customtkinter.CTkScrollableFrame(frame1, fg_color='transparent', width=173, height=43, corner_radius=5, border_width=0)
        sframe1.grid(row=1,column=0,padx=0,pady=0)
        sframe1._scrollbar.configure(height=0)
        labellist1=['Mobbing','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion']
        self.entrylist=[]
        for i in range(len(labellist1)):
            button = create_button(sframe1,i,text='',width=40)
            button.grid(row=i,column=0,padx=(0,4),pady=(0,2), sticky='nw')
            entrylabel1 = customtkinter.CTkLabel(sframe1, width=100, height=20, text=f'{i}', fg_color='black', anchor='w')
            entrylabel1.grid(row=i,column=1,padx=2,pady=(1,0), sticky='nw')

        label2 = customtkinter.CTkLabel(frame2, text='Class Skills', font=('Arial', 12, 'bold'), height=18, text_color='#0e8783')
        label2.grid(row=0,column=0, padx=4,pady=0, sticky='w')
        sframe2 = customtkinter.CTkScrollableFrame(frame2, fg_color='transparent', width=173, height=102, corner_radius=5, border_width=0)
        sframe2.grid(row=1,column=0,padx=0,pady=0)
        sframe2._scrollbar.configure(height=0)
        labellist2=['Mobbing','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion',
        'Mobbing','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion']
        self.entrylist2=[]
        for i in range(len(labellist2)):
            button = create_button(sframe2,i,text='',width=40)
            button.grid(row=i,column=0,padx=(0,4),pady=(0,2), sticky='nw')
            entrylabel2 = customtkinter.CTkLabel(sframe2, width=100, height=20, text=f'{i}', fg_color='black', anchor='w')
            entrylabel2.grid(row=i,column=1,padx=2,pady=(1,0), sticky='nw')

        label3 = customtkinter.CTkLabel(frame3, text='Optional Skills', font=('Arial', 12, 'bold'), height=18, 
        text_color='#0e8783', fg_color='transparent')
        label3.grid(row=0,column=0, padx=(1,0),pady=0, sticky='nw')
        button3 = customtkinter.CTkButton(frame3, text='Skill Editor', font=('Arial', 11, 'bold'), width=60, 
        height=12, text_color='#0e8783', fg_color='black')
        button3.grid(row=0,column=1, padx=(0,3),pady=0, sticky='e')
        sframe3 = customtkinter.CTkScrollableFrame(frame3, fg_color='transparent', width=173, height=170, corner_radius=5, border_width=0)
        sframe3.grid(row=1,column=0,columnspan=2,padx=0,pady=0)
        sframe3._scrollbar.configure(height=0)
        labellist3=['Mobbing','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion',
        'Mobbing','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion','Meso Explosion']
        self.entrylist3=[]
        for i in range(len(labellist2)):
            button = create_button(sframe3,i,text='',width=40)
            button.grid(row=i,column=0,padx=(0,4),pady=(0,2), sticky='nw')
            entrylabel3 = customtkinter.CTkLabel(sframe3, width=100, height=20, text=f'{i}', fg_color='black', anchor='w')
            entrylabel3.grid(row=i,column=1,padx=2,pady=(1,0), sticky='nw')


    def setup_tab1(self):
        frameleft = customtkinter.CTkFrame(self.tab_1, fg_color='transparent', width=195, height=200, corner_radius=5)
        frameleft.grid_propagate(False)
        frameleft.rowconfigure(0,weight=1)
        frameleft.rowconfigure(1,weight=1)
        frameleft.grid(row=0,column=0,padx=0,pady=0,sticky='nsew')
        frameright = customtkinter.CTkFrame(self.tab_1, fg_color='transparent', width=195, height=200, corner_radius=5)
        frameright.grid(row=0,column=1,padx=0,pady=0,sticky='nsew')

        frame1 = customtkinter.CTkFrame(frameleft, fg_color='transparent', width=194, height=65)
        frame1.grid_propagate(False)
        frame1.grid(row=0,column=0,padx=0,pady=0, sticky='n')

        def create_label(master,button_id,text='Custom Slot',width=30,anchor='w'):
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12),
            # height=11, anchor=anchor, bg_color='#fabcd3',width=width)
            height=11, anchor=anchor, bg_color='transparent',width=width)
            return label1
        def create_checkbox(master,button_id,bd_width=0,bd_color='#3a8b83'):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=bd_width, border_color=bd_color, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id,width=40,text=None):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                    button1.configure(text=f'{button_id}')
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=width, height=20, border_width=0, text=text, command=lambda: button_command1(),
            font=('Arial', 11), fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
            return button1
        def create_slider(master):            
            def sliding(value):
                value=int(value)
                print(value)
            slider1 = customtkinter.CTkSlider(master,from_=0,to=80,command=sliding,number_of_steps=100,width=95,height=10,
            fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
            return slider1
            
        def startcmd():
            pass
        def resetcmd():
            pass
        button1 = customtkinter.CTkButton(frame1, text='Start', width=87, height=27, font=('Arial',11), 
        fg_color='#0bbdb3', text_color='#010101', corner_radius=6, command=startcmd)
        button1.grid(row=0,column=0,padx=(2,10),pady=(5,0))
        button2 = customtkinter.CTkButton(frame1, text='Reset', width=87, height=27, font=('Arial',11),
        fg_color='#0bbdb3', text_color='#010101', corner_radius=6,command=resetcmd)
        button2.grid(row=0,column=1,padx=(0,3),pady=(5,0))
        button3 = customtkinter.CTkButton(frame1, text='Pause', width=87, height=27, font=('Arial',11), 
        fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
        button3.grid(row=1,column=0,padx=(2,10),pady=(5,0))
        button4 = customtkinter.CTkButton(frame1, text='Town', width=87, height=27, font=('Arial',11), 
        fg_color='#0bbdb3', text_color='#010101', corner_radius=6)
        button4.grid(row=1,column=1,padx=(0,3),pady=(5,0))

        frame2 = customtkinter.CTkFrame(frameleft, fg_color='transparent', width=195, height=135)
        frame2.grid_propagate(False)
        frame2.columnconfigure(1,weight=1)
        frame2.grid(row=1,column=0,columnspan=2,padx=0,pady=0)
        
        label1 = customtkinter.CTkLabel(frame2, text='Map Controls', height=11, fg_color='transparent', font=("Arial", 12, 'bold'), 
        text_color='white', anchor='w',bg_color='transparent',width=30)
        label1.grid(row=0,column=0,padx=(3,3),pady=(7,0), sticky='W', columnspan=2)
        label2 = customtkinter.CTkLabel(frame2, text='Bounds', height=11, fg_color='transparent', font=("Arial", 12), 
        text_color='white', anchor='w',bg_color='transparent',width=30)
        label2.grid(row=1,column=0,padx=(3,3),pady=(7,0), sticky='W')
        label3 = customtkinter.CTkLabel(frame2, text='Offset', height=11, fg_color='transparent', font=("Arial", 12), 
        text_color='white', anchor='w',bg_color='transparent',width=30)
        label3.grid(row=2,column=0,padx=(3,3),pady=(7,0), sticky='W')
        label4 = customtkinter.CTkLabel(frame2, text='Height', height=11, fg_color='transparent', font=("Arial", 12), 
        text_color='white', anchor='w',bg_color='transparent',width=30)
        label4.grid(row=3,column=0,padx=(3,3),pady=(7,0), sticky='W')
        label5 = customtkinter.CTkLabel(frame2, text='Floor', height=11, fg_color='transparent', font=("Arial", 12), 
        text_color='white', anchor='w',bg_color='transparent',width=30)
        label5.grid(row=4,column=0,padx=(3,3),pady=(7,0), sticky='W')
        label6 = customtkinter.CTkLabel(frame2, text='Pickup Cycles', height=11, fg_color='transparent', font=("Arial", 12), 
        text_color='white', anchor='w',bg_color='transparent',width=30)
        label6.grid(row=5,column=0,padx=(3,3),pady=(7,0), sticky='W', columnspan=2)

        frame3 = customtkinter.CTkFrame(frame2, fg_color='transparent', height=20, width=80)
        frame3.grid_propagate(False)
        frame3.rowconfigure(0, weight=1)
        frame3.columnconfigure(0, weight=1)
        frame3.grid(row=0,column=2,padx=(0,5),pady=(0,0), sticky='E')        
        button5 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button5.grid(row=0,column=1,padx=(2,0),pady=(6,0))
        button6 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button6.grid(row=0,column=2,padx=(2,0),pady=(6,0))
        button7 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button7.grid(row=0,column=3,padx=(2,0),pady=(6,0))
        button8 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button8.grid(row=0,column=4,padx=(2,0),pady=(6,0))
        button9 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button9.grid(row=0,column=5,padx=(2,4),pady=(6,0))

        self.bounds=40
        self.offset=50
        def sliding(value):
            self.imagesrefleft.pop()
            self.imagesleft.pop()
            self.imagesrefright.pop()
            self.imagesright.pop()
            value=int(value)
            self.bounds=value
            leftend=91-self.bounds+self.offset-50
            if leftend<=1:
                leftend=1
            rightstart=101+self.bounds+self.offset-50
            if rightstart>=193:
                rightstart=193
            create_rectangle_left(0, 0, leftend, 130, fill='lightgreen', alpha=.3)
            create_rectangle_right(rightstart, 0, 193, 130, fill='red', alpha=.3)
        slider1 = customtkinter.CTkSlider(frame2,from_=0,to=80,command=sliding,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider1.grid(row=1,column=1,padx=(1,5),pady=(9,0), columnspan=2)
        def sliding2(value):
            self.imagesrefleft.pop()
            self.imagesleft.pop()
            self.imagesrefright.pop()
            self.imagesright.pop()
            value=int(value)
            self.offset=value
            leftend=91-self.bounds+value-50
            if leftend<=1:
                leftend=1
            rightstart=101+self.bounds+value-50
            if rightstart>=193:
                rightstart=193
            create_rectangle_left(0, 0, leftend, 130, fill='lightgreen', alpha=.3)
            create_rectangle_right(rightstart, 0, 193, 130, fill='red', alpha=.3)
        slider2 = customtkinter.CTkSlider(frame2,from_=0,to=100,command=sliding2,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider2.grid(row=2,column=1,padx=(1,5),pady=(9,0), columnspan=2)
        def sliding3(value):     
            self.imagesreftop.pop()
            self.imagestop.pop()
            value=int(value)
            if value>=100:
                value=99
            valueB = value+10
            if valueB >= 130:
                valueB=129
            create_rectangle_top(0, value, 193, valueB, fill='#00ffff', alpha=.3)
        slider3 = customtkinter.CTkSlider(frame2,from_=0,to=130,command=sliding3,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider3.grid(row=3,column=1,padx=(1,5),pady=(9,0), columnspan=2)
        slider3.set(10)

        def sliding4(value):
            self.imagesrefbtm.pop()
            self.imagesbtm.pop()
            value=int(value)
            create_rectangle_btm(0, value, 193, 130, fill='maroon', alpha=.7)
        slider4 = customtkinter.CTkSlider(frame2,from_=0,to=130,command=sliding4,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider4.grid(row=4,column=1,padx=(1,5),pady=(9,0), columnspan=2)
        slider4.set(100)

        spinbox1 = tkinter.Spinbox(frame2, from_=0, to=10, width=10, bg='#212121', fg='white', buttonbackground='#212121', bd=0)
        spinbox1.grid(row=5,column=2,padx=(1,5),pady=(9,0))

        frameright1 = customtkinter.CTkFrame(frameright, fg_color='transparent', height=50, width=194)
        frameright1.grid_propagate(False)
        frameright1.grid(row=0,column=0,padx=(0,0),pady=(0,0))
        frameright2 = customtkinter.CTkFrame(frameright, fg_color='transparent', height=130, width=194)
        frameright2.grid_propagate(False)
        frameright2.grid(row=1,column=0,padx=(0,0),pady=(0,0))
        frameright3 = customtkinter.CTkFrame(frameright, fg_color='transparent', height=20, width=194)
        frameright3.grid_propagate(False)
        frameright3.grid_rowconfigure(0, weight=1)
        frameright3.grid_columnconfigure(0, weight=1)
        frameright3.grid(row=2,column=0,padx=(0,0),pady=(0,0))




        framerightlabel1 = customtkinter.CTkLabel(frameright1, text='Mobbing Algorithm', fg_color='transparent', font=('Helvetica',11, 'bold'), 
        text_color='white', anchor='w', height=20)
        framerightlabel1.grid(row=0,column=0,padx=(5,0),pady=(0,0), sticky='W')
        def combobox1function(value):
            print(f'comboboxfunction')
        comboboxvalue=['Clockwise', 'Anticlockwise']
        combobox1 = customtkinter.CTkComboBox(frameright1, values=comboboxvalue, command=combobox1function, height=25, width=130)
        combobox1.grid(row=1,column=0,padx=(2,0),pady=(0,0), sticky='W')

        canvas = tkinter.Canvas(frameright2, borderwidth=0, highlightthickness=0, relief='ridge')
        canvas.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='nw')
        image = Image.open('minimap.png')
        imageresized = image.resize((194,130), Image.LANCZOS)
        self.imagetk = ImageTk.PhotoImage(imageresized)
        canvas.create_image(0,0,image=self.imagetk, anchor='nw')

        self.imagesleft=[] # prevent garbage collected because PYTHON!!!!!
        self.imagesright=[] # prevent garbage collected because PYTHON!!!!!
        self.imagesrefleft=[]
        self.imagesrefright=[]
        ## https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent
        def create_rectangle_left(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                self.imagesleft.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                self.imagesrefleft.append(imageref)
        def create_rectangle_right(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                self.imagesright.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                self.imagesrefright.append(imageref)
                
        self.imagestop=[] # prevent garbage collected because PYTHON!!!!!
        self.imagesbtm=[] # prevent garbage collected because PYTHON!!!!!
        self.imagesreftop=[]
        self.imagesrefbtm=[]
        def create_rectangle_top(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                self.imagestop.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                self.imagesreftop.append(imageref)
        def create_rectangle_btm(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                self.imagesbtm.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                self.imagesrefbtm.append(imageref)

        leftend=91-self.bounds+self.offset-50
        if leftend<=1:
            leftend=1
        rightstart=101+self.bounds+self.offset-50
        if rightstart>=193:
            rightstart=193
        create_rectangle_left(0, 0, leftend, 130, fill='lightgreen', alpha=.3)
        create_rectangle_right(rightstart, 0, 194, 130, fill='red', alpha=.3)
        create_rectangle_top(0, 10, 194, 25, fill='#00ffff', alpha=.3)
        create_rectangle_btm(0, 130-10, 194, 130, fill='maroon', alpha=.7)

        frameright3label1 = customtkinter.CTkLabel(frameright3, text='PAUSED Cycle 2', fg_color='transparent', font=('Helvetica',11, 'bold'), text_color='green', anchor='center')
        frameright3label1.grid(row=0,column=0,padx=(0,0),pady=(7,0), sticky='nsew')
        
    def start(self):
        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()
        self.setup_tab4()
        self.setup_tab5()
        self.setup_tab6()
        self.mainloop()

    
if __name__ == '__main__':
    gui = GUI()
    gui.start()
