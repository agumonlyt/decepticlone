import customtkinter
import asyncio
import tkinter
from tkinter import Frame, Label
from PIL import Image, ImageTk
from bumblebee import customtkinter as bumblebeetkinter
# from bumblebee.customtkinter.windows.widgets import CTkCheckBox
# import ttkbootstrap as tb

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



# Colors
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

class ToplevelWindow(customtkinter.CTkToplevel):
    # def __init__(self, mylabeltext, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
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







class Decepticlone(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        # self.geometry("360x300")
        self.geometry("400x320")
        self.title("chrome")
        titlebar = TitleBar(self, title="DECEPTICLONE")
        titlebar.pack(fill="both")
        tabview = customtkinter.CTkTabview(master=self, corner_radius=5, width=400, height=220)
        tabview._outer_spacing=0
        tabview.pack(padx=0, pady=0)        
        self.tab_1 = tabview.add("Controls")
        self.tab_2 = tabview.add("Skills")
        self.tab_3 = tabview.add("Consumables")
        self.tab_4 = tabview.add("Settings")
        self.tab_5 = tabview.add("Modules")
        self.tab_6 = tabview.add("+")
        tabview.set("Consumables")

    def setup_tab3(self):
        frame1 = customtkinter.CTkFrame(self.tab_3, fg_color='transparent', width=170, height=200, corner_radius=5)
        frame1.grid_propagate(False)
        # frame1.grid_columnconfigure(0,weight=1)
        # frame1.grid_columnconfigure(1,weight=1)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        frame2 = customtkinter.CTkFrame(self.tab_3, fg_color='transparent', width=220, height=200, corner_radius=5)
        frame2.grid_propagate(False)
        # frame2.grid_columnconfigure(0, weight=1)
        # frame2.grid_columnconfigure(1, weight=1)
        frame2.grid(row=0,column=1, padx=0,pady=0)


        self.toplevel_window = None

        def create_label(master,button_id,text='Custom Slot'):
            # label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12), width=11, height=11, anchor='w')
            label1 = customtkinter.CTkLabel(master, text=text, text_color="white", font=("Arial", 12), 
            width=100, height=11, anchor='w', bg_color='transparent')
            return label1
        def create_checkbox(master,button_id):
            checkbox1 = bumblebeetkinter.CTkCheckBox(master, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            border_width=0, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            return checkbox1
        def create_button(master,button_id):
            def button_command1():
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(mylabeltext2=f'{button_id}')  # create window if its None or destroyed
                else:
                    self.toplevel_window.focus()  # if window exists focus it
            button1 = customtkinter.CTkButton(master, width=30, height=20, border_width=0, text='', command=lambda: button_command1(),
            font=('Lucida Console', 10), fg_color='#0bbdb3')
            # button1.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            return button1
        # def button1cmd(i):
        #     if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        #         self.toplevel_window = ToplevelWindow(mylabeltext2=f'{i}')  # create window if its None or destroyed
        #     else:
        #         self.toplevel_window.focus()  # if window exists focus it
        self.buttonlist1=[]
        self.entrylist1=[]
        self.checkboxlist1=[]
        for i in range(9):
            # # entry1 = customtkinter.CTkEntry(frame1, width=30, height=20, justify='center', border_width=0, 
            # # font=('Lucida Console', 10), fg_color='#0bbdb3')
            # # entry1.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            # # self.entrylist.append(entry1)
            # button1 = customtkinter.CTkButton(frame1, width=30, height=20, border_width=0, text='', command=lambda: button1cmd(i),
            # font=('Lucida Console', 10), fg_color='#0bbdb3')
            # button1.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            # self.buttonlist1.append(button1)
            button = create_button(frame1,i)            
            button.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            # # checkbox1 = tkinter.Checkbutton(frame1)
            # # # checkbox1 = customtkinter.CTkCheckBox(frame1, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            # checkbox1 = bumblebeetkinter.CTkCheckBox(frame1, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            # border_width=0, corner_radius=0, checkmark_color='#424041', fg_color='#0bbdb3', bg_color='#424041')
            # # text='Union Wealth', font=('Arial Narrow', 12), border_width=0, corner_radius=0, 
            # # text='Union Wealth', font=('Lucida Console', 12), border_width=0, corner_radius=0)
            checkbox1 = create_checkbox(frame1,i)
            checkbox1.grid(row=i,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            # label1 = customtkinter.CTkLabel(frame1, text='Mushroom Buff', text_color="white", font=("Arial", 12), width=11, height=11, anchor='w')
            label1 = create_label(frame1,i)
            label1.grid(row=i,column=2,padx=(5,0),pady=(0,0), sticky='w')
        self.entrylist2=[]
        self.checkboxlist2=[]
        for i in range(4):
            # entry2 = customtkinter.CTkEntry(frame2, width=40, height=20, justify='center')
            # entry2.grid(row=i,column=0,padx=0,pady=(0,0), sticky='w')
            # self.entrylist.append(entry2)
            # checkbox2 = customtkinter.CTkCheckBox(frame2, width=11, height=11, checkbox_width=12, checkbox_height=12, 
            # text='Wealth Acquisition Potion', font=('Arial Narrow', 12), border_width=0, corner_radius=5)
            # checkbox2.grid(row=i,column=1,padx=(2,0),pady=(0,0), sticky='w')
            # self.checkboxlist2.append(checkbox2)
            button = create_button(frame2,i)            
            button.grid(row=i,column=0,padx=0,pady=(2,0), sticky='w')
            checkbox1 = create_checkbox(frame2,i)
            checkbox1.grid(row=i,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame2,i)
            label1.grid(row=i,column=2,padx=(5,0),pady=(0,0), sticky='w')
        framecolor = ['#123456', '#fedcba']
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
        print(f'{usepotionlist=}')
        for i in range(2):
            checkbox1 = create_checkbox(frame2,i)
            checkbox1.grid(row=i+6,column=1,padx=(5,0),pady=(0,0), sticky='w')
            self.checkboxlist1.append(checkbox1)
            label1 = create_label(frame2,i,'Use Pet Food?')
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
        font=('Helvetica', 12), fg_color='#0bbdb3', text_color='black')
        buttonenable.grid(row=0,column=0,padx=(35,5),pady=(0,0), sticky='w')
        def disableall():
            pass
        buttondisable = customtkinter.CTkButton(framebutton, width=80, border_width=0, text='Disable All', command=disableall,
        font=('Helvetica', 12), fg_color='#0bbdb3', text_color='black')
        buttondisable.grid(row=0,column=1,padx=0,pady=(0,0), sticky='w')




    def setup_tab2(self):
        frame1 = customtkinter.CTkFrame(self.tab_2, fg_color='green', width=170, height=70, corner_radius=5)
        # frame1.grid_propagate(False)
        frame1.grid_columnconfigure(0,weight=1)
        frame1.grid_columnconfigure(1,weight=1)
        frame1.grid(row=0,column=0,padx=0,pady=0)
        # # frame2 = customtkinter.CTkFrame(self.tab_2, fg_color='transparent', width=170, height=110, corner_radius=5)
        frame2 = customtkinter.CTkFrame(self.tab_2, fg_color='lime', width=170, height=130, corner_radius=5)
        frame2.grid_propagate(False)
        frame2.grid(row=1,column=0,padx=0,pady=0)
        frame3 = customtkinter.CTkFrame(self.tab_2, fg_color='khaki', width=170, height=200, corner_radius=5)
        frame3.grid_propagate(False)
        frame3.grid_columnconfigure(0, weight=1)
        frame3.grid_columnconfigure(1, weight=1)
        frame3.grid(row=0,column=1, rowspan=2, padx=0,pady=0)

        label1 = customtkinter.CTkLabel(frame1, text='Class Required Skills', font=('Arial', 12, 'bold'), height=18)
        label1.grid(row=0,column=0, padx=4,pady=0, sticky='w')
        sframe1 = customtkinter.CTkScrollableFrame(frame1, fg_color='purple', width=146, height=40, corner_radius=5, border_width=0)
        sframe1.grid(row=1,column=0,padx=1,pady=0)
        sframe1._scrollbar.configure(height=0)
        # sframe1.grid_rowconfigure(0, weight=1)
        # sframe1.grid_columnconfigure(0, weight=1)
        # sframe1.grid_columnconfigure(1, weight=1)
        # sframe1.grid_columnconfigure(2, weight=1)
        self.entrylist=[]
        for i in range(20):
            entry1 = customtkinter.CTkEntry(sframe1, width=40, height=20, justify='center')
            entry1.grid(row=i,column=0,padx=0,pady=(0,0), sticky='nw')
            self.entrylist.append(entry1)
            entrylabel1 = customtkinter.CTkLabel(sframe1, width=100, height=20, text=f'{i}', fg_color='black', anchor='w')
            entrylabel1.grid(row=i,column=1,padx=2,pady=(1,0), sticky='nw')

        label2 = customtkinter.CTkLabel(frame2, text='Class Skills', font=('Arial', 12, 'bold'), height=18, text_color='#0e8783')
        label2.grid(row=0,column=0, padx=4,pady=0, sticky='w')
        sframe2 = customtkinter.CTkScrollableFrame(frame2, fg_color='purple', width=146, height=100, corner_radius=5, border_width=0)
        sframe2.grid(row=1,column=0,padx=1,pady=0)
        sframe2._scrollbar.configure(height=0)
        self.entrylist2=[]
        for i in range(20):
            entry2 = customtkinter.CTkEntry(sframe2, width=40, height=20, justify='center')
            entry2.grid(row=i,column=0,padx=0,pady=(0,0), sticky='nw')
            self.entrylist2.append(entry2)
            entrylabel2 = customtkinter.CTkLabel(sframe2, width=100, height=20, text=f'{i}', fg_color='black', anchor='w')
            entrylabel2.grid(row=i,column=1,padx=2,pady=(1,0), sticky='nw')

        label3 = customtkinter.CTkLabel(frame3, text='Optional Skills', font=('Arial', 12, 'bold'), height=18, text_color='#0e8783', fg_color='black')
        label3.grid(row=0,column=0, padx=(1,0),pady=0, sticky='w')
        button3 = customtkinter.CTkButton(frame3, text='Skill Editor', font=('Arial', 12, 'bold'), width=60, height=18, text_color='#0e8783', fg_color='black')
        button3.grid(row=0,column=1, padx=1,pady=0, sticky='e')
        sframe3 = customtkinter.CTkScrollableFrame(frame3, fg_color='purple', width=146, height=168, corner_radius=5, border_width=0)
        sframe3.grid(row=1,column=0,columnspan=2,padx=1,pady=0)
        sframe3._scrollbar.configure(height=0)
        self.entrylist3=[]
        for i in range(20):
            entry3 = customtkinter.CTkEntry(sframe3, width=40, height=20, justify='center')
            entry3.grid(row=i,column=0,padx=0,pady=(0,0), sticky='nw')
            self.entrylist3.append(entry2)
            entrylabel3 = customtkinter.CTkLabel(sframe3, width=100, height=20, text=f'{i}', fg_color='black', anchor='w')
            entrylabel3.grid(row=i,column=1,padx=2,pady=(1,0), sticky='nw')


        pass
        # self.mainloop()

    def setup_tab1(self):
        # frameleft = customtkinter.CTkFrame(self.tab_1, width=180, height=210, fg_color='transparent')
        # frameleft = customtkinter.CTkFrame(self.tab_1, fg_color='green', width=173, height=180, corner_radius=5)
        frameleft = customtkinter.CTkFrame(self.tab_1, fg_color='transparent', width=173, height=180, corner_radius=5)
        frameleft.grid_propagate(False)
        frameleft.rowconfigure(0,weight=1)
        frameleft.rowconfigure(1,weight=1)
        frameleft.grid(row=0,column=0,padx=0,pady=0)
        # frameright = customtkinter.CTkFrame(self.tab_1, fg_color='teal', width=173, height=180, corner_radius=5)
        frameright = customtkinter.CTkFrame(self.tab_1, fg_color='transparent', width=173, height=180, corner_radius=5)
        frameright.grid(row=0,column=1,padx=0,pady=0,sticky='nsew')

        # frame1 = customtkinter.CTkFrame(frameleft, fg_color='transparent', width=10, height=10)
        # frame1 = customtkinter.CTkFrame(frameleft, fg_color='blue', height=125, width=173)
        frame1 = customtkinter.CTkFrame(frameleft, fg_color='transparent', height=125, width=173)
        frame1.grid_propagate(False)
        frame1.grid(row=0,column=0,padx=0,pady=0, sticky='nsew')

        def startcmd():
            pass
        button1 = customtkinter.CTkButton(frame1, text='Start', width=75, height=20, font=('Helvetica',11), corner_radius=10, command=startcmd)
        button1.grid(row=0,column=0,padx=(3,3),pady=(4,2))
        def resetcmd():
            pass
        button2 = customtkinter.CTkButton(frame1, text='Reset', width=75, height=20, font=('Helvetica',11), corner_radius=10, command=resetcmd)
        button2.grid(row=0,column=1,padx=(3,3),pady=(4,2))
        button3 = customtkinter.CTkButton(frame1, text='Pause', width=75, height=20, font=('Helvetica',11), corner_radius=10)
        button3.grid(row=1,column=0,padx=(3,3),pady=(2,4))
        button4 = customtkinter.CTkButton(frame1, text='Town', width=75, height=20, font=('Helvetica',11), corner_radius=10)
        button4.grid(row=1,column=1,padx=(3,3),pady=(2,4))

        # frame2 = customtkinter.CTkFrame(frameleft, width=180, fg_color='transparent')
        # frame2 = customtkinter.CTkFrame(frameleft, fg_color='purple', width=173)
        frame2 = customtkinter.CTkFrame(frameleft, fg_color='transparent', width=173)
        frame2.grid_propagate(False)
        frame2.columnconfigure(1,weight=1)
        
        frame2.grid(row=1,column=0,padx=0,pady=0, sticky='nsew')
        label1 = customtkinter.CTkLabel(frame2, text='Map Controls', height=20, fg_color='transparent', font=('Helvetica',11, 'bold'), text_color='white', anchor='w')
        label1.grid(row=0,column=0,padx=(3,3),pady=(0,0), sticky='W', columnspan=2)
        label2 = customtkinter.CTkLabel(frame2, text='Bounds', height=20, fg_color='transparent', font=('Helvetica',11), text_color='white', anchor='w')
        label2.grid(row=1,column=0,padx=(3,3),pady=(0,0), sticky='W')
        label3 = customtkinter.CTkLabel(frame2, text='Offset', height=20, fg_color='transparent', font=('Helvetica',11), text_color='white', anchor='w')
        label3.grid(row=2,column=0,padx=(3,3),pady=(0,0), sticky='W')
        label4 = customtkinter.CTkLabel(frame2, text='Height', height=20, fg_color='transparent', font=('Helvetica',11), text_color='white', anchor='w')
        label4.grid(row=3,column=0,padx=(3,3),pady=(0,0), sticky='W')
        label5 = customtkinter.CTkLabel(frame2, text='Floor', height=20, fg_color='transparent', font=('Helvetica',11), text_color='white', anchor='w')
        label5.grid(row=4,column=0,padx=(3,3),pady=(0,0), sticky='W')
        label6 = customtkinter.CTkLabel(frame2, text='Pickup Cycles', height=20, fg_color='transparent', font=('Helvetica',11), text_color='white', anchor='w')
        label6.grid(row=5,column=0,padx=(3,3),pady=(0,0), sticky='W', columnspan=2)

        # frame3 = customtkinter.CTkFrame(frame2, fg_color='magenta', height=20, width=80)
        frame3 = customtkinter.CTkFrame(frame2, fg_color='transparent', height=20, width=80)
        frame3.grid_propagate(False)
        frame3.rowconfigure(0, weight=1)
        frame3.columnconfigure(0, weight=1)
        frame3.grid(row=0,column=2,padx=(0,5),pady=(0,0), sticky='E')        
        button5 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button5.grid(row=0,column=1,padx=(2,0),pady=(0,0))
        button6 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button6.grid(row=0,column=2,padx=(2,0),pady=(0,0))
        button7 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button7.grid(row=0,column=3,padx=(2,0),pady=(0,0))
        button8 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button8.grid(row=0,column=4,padx=(2,0),pady=(0,0))
        button9 = customtkinter.CTkButton(frame3, text='', width=10, height=10, corner_radius=10, fg_color='#acbbbb')
        button9.grid(row=0,column=5,padx=(2,4),pady=(0,0))

        self.bounds=40
        self.offset=50
        def sliding(value):
            self.imagesrefleft.pop()
            self.imagesleft.pop()
            self.imagesrefright.pop()
            self.imagesright.pop()
            value=int(value)
            self.bounds=value
            leftend=80-self.bounds+self.offset-50
            if leftend<=1:
                leftend=1
            rightstart=90+self.bounds+self.offset-50
            if rightstart>=169:
                rightstart=169
            create_rectangle_left(0, 0, leftend, 110, fill='lightgreen', alpha=.3)
            create_rectangle_right(rightstart, 0, 170, 110, fill='red', alpha=.3)
        slider1 = customtkinter.CTkSlider(frame2,from_=0,to=80,command=sliding,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider1.grid(row=1,column=1,padx=(1,5),pady=(1,1), columnspan=2)
        def sliding2(value):
            self.imagesrefleft.pop()
            self.imagesleft.pop()
            self.imagesrefright.pop()
            self.imagesright.pop()
            value=int(value)
            self.offset=value
            leftend=80-self.bounds+value-50
            if leftend<=1:
                leftend=1
            rightstart=90+self.bounds+value-50
            if rightstart>=169:
                rightstart=169
            create_rectangle_left(0, 0, leftend, 110, fill='lightgreen', alpha=.3)
            create_rectangle_right(rightstart, 0, 170, 110, fill='red', alpha=.3)
        slider2 = customtkinter.CTkSlider(frame2,from_=0,to=100,command=sliding2,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider2.grid(row=2,column=1,padx=(1,5),pady=(1,1), columnspan=2)
        def sliding3(value):     
            self.imagesreftop.pop()
            self.imagestop.pop()
            value=int(value)
            if value>=100:
                value=99
            valueB = value+10
            if valueB >= 110:
                valueB=109
            create_rectangle_top(0, value, 170, valueB, fill='#00ffff', alpha=.3)
        slider3 = customtkinter.CTkSlider(frame2,from_=0,to=110,command=sliding3,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider3.grid(row=3,column=1,padx=(1,5),pady=(1,1), columnspan=2)
        slider3.set(10)

        def sliding4(value):
            self.imagesrefbtm.pop()
            self.imagesbtm.pop()
            value=int(value)
            create_rectangle_btm(0, value, 170, 110, fill='maroon', alpha=.7)
        slider4 = customtkinter.CTkSlider(frame2,from_=0,to=110,command=sliding4,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider4.grid(row=4,column=1,padx=(1,5),pady=(1,1), columnspan=2)
        slider4.set(100)

        # spinbox1 = tkinter.Spinbox(frame2, from_=0, to=10, width=10, bg='#142455', fg='white')
        # spinbox1 = tkinter.Spinbox(frame2, from_=0, to=10, width=10, bg='#11aaaa')
        # spinbox1 = tkinter.Spinbox(frame2, from_=0, to=10, width=10, bg='transparent')
        spinbox1 = tkinter.Spinbox(frame2, from_=0, to=10, width=10, bg='#212121', fg='white', buttonbackground='#212121', bd=0)
        spinbox1.grid(row=5,column=2,padx=(1,5),pady=(1,1))

        # frameright1 = customtkinter.CTkFrame(frameright, fg_color='#123fff', height=47, width=170)
        frameright1 = customtkinter.CTkFrame(frameright, fg_color='transparent', height=47, width=170)
        frameright1.grid_propagate(False)
        frameright1.grid(row=0,column=0,padx=(1,1),pady=(0,0))
        # frameright2 = customtkinter.CTkFrame(frameright, fg_color='#f231ff', height=110, width=170)
        frameright2 = customtkinter.CTkFrame(frameright, fg_color='transparent', height=110, width=170)
        frameright2.grid_propagate(False)
        frameright2.grid(row=1,column=0,padx=(1,1),pady=(0,0))
        # frameright3 = customtkinter.CTkFrame(frameright, fg_color='#12ff1f', height=20, width=170)
        frameright3 = customtkinter.CTkFrame(frameright, fg_color='transparent', height=20, width=170)
        frameright3.grid_propagate(False)
        frameright3.grid_rowconfigure(0, weight=1)
        frameright3.grid_columnconfigure(0, weight=1)
        frameright3.grid(row=2,column=0,padx=(1,1),pady=(0,0))

        framerightlabel1 = customtkinter.CTkLabel(frameright1, text='Mobbing Algorithm', fg_color='transparent', font=('Helvetica',11, 'bold'), text_color='white', anchor='w', height=20)
        framerightlabel1.grid(row=0,column=0,padx=(5,0),pady=(0,0), sticky='W')
        def combobox1function(value):
            print(f'comboboxfunction')
        comboboxvalue=['Clockwise', 'Anticlockwise']
        combobox1 = customtkinter.CTkComboBox(frameright1, values=comboboxvalue, command=combobox1function, height=25, width=130)
        combobox1.grid(row=1,column=0,padx=(2,0),pady=(0,0), sticky='W')

        canvas = tkinter.Canvas(frameright2, borderwidth=0, highlightthickness=0, relief='ridge')
        canvas.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='nw')
        image = Image.open('minimap.png')
        imageresized = image.resize((170,110), Image.LANCZOS)
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

        leftend=80-self.bounds+self.offset-50
        if leftend<=1:
            leftend=1
        rightstart=90+self.bounds+self.offset-50
        if rightstart>=169:
            rightstart=169
        create_rectangle_left(0, 0, leftend, 110, fill='lightgreen', alpha=.3)
        create_rectangle_right(rightstart, 0, 170, 110, fill='red', alpha=.3)
        create_rectangle_top(0, 10, 170, 25, fill='#00ffff', alpha=.3)
        create_rectangle_btm(0, 110-10, 170, 110, fill='maroon', alpha=.7)

        frameright3label1 = customtkinter.CTkLabel(frameright3, text='PAUSED Cycle 2', fg_color='transparent', font=('Helvetica',11, 'bold'), text_color='green', anchor='center')
        frameright3label1.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='nsew')
        


async def main():
    decepticlone = Decepticlone()
    decepticlone.setup_tab1()
    decepticlone.setup_tab2()
    decepticlone.setup_tab3()
    # decepticlone.after(3,decepticlone.mainloop())
    decepticlone.mainloop()


if __name__ == "__main__":
    asyncio.run(main())







