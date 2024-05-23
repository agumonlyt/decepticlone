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
        # self.app = customtkinter.CTk()
        self.geometry("360x280")
        # self.app.title("chrome")
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
        # canvas = tkinter.Canvas(self.app, bg='white')
        # canvas.pack(padx=(0,0),pady=(0,0))
        # image = Image.open('minimap.png')
        # imagetk = ImageTk.PhotoImage(image)
        # canvas.create_image(0,0,image=imagetk)


    def setup_tab1(self):
        # frameleft = customtkinter.CTkFrame(self.tab_1, width=180, height=210, fg_color='transparent')
        frameleft = customtkinter.CTkFrame(self.tab_1, fg_color='green', width=173, height=180, corner_radius=5)
        frameleft.grid_propagate(False)
        frameleft.rowconfigure(0,weight=1)
        frameleft.rowconfigure(1,weight=1)
        frameleft.grid(row=0,column=0,padx=0,pady=0)
        # frameleft.grid(row=0,column=0,padx=0,pady=0,sticky='nsew')
        # frameright = customtkinter.CTkFrame(self.tab_1, width=180, height=210, fg_color='transparent')
        frameright = customtkinter.CTkFrame(self.tab_1, fg_color='teal', width=173, height=180, corner_radius=5)
        # frameright.grid_propagate(False)
        # frameright.grid(row=0,column=1,padx=0,pady=0)
        # frameright.pack(padx=0,pady=0)
        frameright.grid(row=0,column=1,padx=0,pady=0,sticky='nsew')

        # frame1 = customtkinter.CTkFrame(frameleft, fg_color='transparent', width=10, height=10)
        frame1 = customtkinter.CTkFrame(frameleft, fg_color='blue', height=125, width=173)
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
        frame2 = customtkinter.CTkFrame(frameleft, fg_color='purple', width=173)
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

        frame3 = customtkinter.CTkFrame(frame2, fg_color='magenta', height=20, width=80)
        # frame3 = customtkinter.CTkFrame(frame2, fg_color='red', height=20, width=80)
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
            print(f'{value=} deleting {imagesrefleft[-1]=}')
            # canvas.delete(imagesrefleft[-1])
            # imagesrefleft.pop()
            # imagesleft.pop()
            # print(imagesrefleft, len(imagesrefleft))
            # create_rectangle_left(0, 0, int(value), 110, fill='lightgreen', alpha=.3)
            imagesrefleft.pop()
            imagesleft.pop()
            imagesrefright.pop()
            imagesright.pop()
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
            print(f'{value=}  deleting {imagesrefright[-1]=}')       
            # canvas.delete(imagesrefright[-1])
            # imagesrefright.pop()
            # imagesright.pop()
            # print(imagesrefright, len(imagesrefright))
            # create_rectangle_right(int(value), 0, 170, 110, fill='red', alpha=.3)
            imagesrefleft.pop()
            imagesleft.pop()
            imagesrefright.pop()
            imagesright.pop()
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
            print(f'{value=}  deleting {imagesrefright[-1]=}')      
            imagesreftop.pop()
            imagestop.pop()
            value=int(value)
            if value>=100:
                value=99
            valueB = value+10
            if valueB >= 110:
                valueB=109
            # self.offset=value
            # leftend=80-self.bounds+value-50
            # if leftend<=1:
            #     leftend=1
            # rightstart=90+self.bounds+value-50
            # if rightstart>=169:
            #     rightstart=169
            # create_rectangle_left(0, 0, leftend, 110, fill='lightgreen', alpha=.3)
            # create_rectangle_right(rightstart, 0, 170, 110, fill='red', alpha=.3)
            create_rectangle_top(0, value, 170, valueB, fill='#00ffff', alpha=.3)
        slider3 = customtkinter.CTkSlider(frame2,from_=0,to=110,command=sliding3,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider3.grid(row=3,column=1,padx=(1,5),pady=(1,1), columnspan=2)
        slider3.set(10)

        def sliding4(value):
            print(f'{value=}  deleting {imagesrefright[-1]=}')      
            imagesrefbtm.pop()
            imagesbtm.pop()
            value=int(value)
            # self.offset=value
            # leftend=80-self.bounds+value-50
            # if leftend<=1:
            #     leftend=1
            # rightstart=90+self.bounds+value-50
            # if rightstart>=169:
            #     rightstart=169
            # create_rectangle_left(0, 0, leftend, 110, fill='lightgreen', alpha=.3)
            # create_rectangle_right(rightstart, 0, 170, 110, fill='red', alpha=.3)
            create_rectangle_btm(0, value, 170, 110, fill='maroon', alpha=.7)
        slider4 = customtkinter.CTkSlider(frame2,from_=0,to=110,command=sliding4,number_of_steps=100,width=150,height=10,fg_color='#11aaaa',progress_color='green',button_color='yellow',button_hover_color='orange')
        slider4.grid(row=4,column=1,padx=(1,5),pady=(1,1), columnspan=2)
        slider4.set(100)

        spinbox1 = tkinter.Spinbox(frame2, from_=0, to=10, width=10, bg='#11aaaa')
        spinbox1.grid(row=5,column=2,padx=(1,5),pady=(1,1))

        frameright1 = customtkinter.CTkFrame(frameright, fg_color='#123fff', height=47, width=170)
        frameright1.grid_propagate(False)
        # frameright1.grid_rowconfigure(0, weight=2)
        # frameright1.grid_rowconfigure(1, weight=3)
        frameright1.grid(row=0,column=0,padx=(1,1),pady=(0,0))
        frameright2 = customtkinter.CTkFrame(frameright, fg_color='#f231ff', height=110, width=170)
        frameright2.grid_propagate(False)
        # # frameright2.rowconfigure(0, weight=1)
        # # frameright2.columnconfigure(0, weight=1)
        # frameright2.grid_rowconfigure(0, weight=1)
        # frameright2.grid_columnconfigure(0, weight=1)
        # frameright2.pack(padx=(1,1),pady=(0,0))
        frameright2.grid(row=1,column=0,padx=(1,1),pady=(0,0))
        frameright3 = customtkinter.CTkFrame(frameright, fg_color='#12ff1f', height=20, width=170)
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

        # frame2image = customtkinter.CTkImage(light_image=Image.open('minimap.png'), dark_image=Image.open('minimap.png'), size=(170,110))
        canvas = tkinter.Canvas(frameright2, borderwidth=0, highlightthickness=0, relief='ridge')
        # canvas.pack(padx=(0,0),pady=(0,0), anchor='nw', fill='both', expand=1)
        canvas.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='nw')
        image = Image.open('minimap.png')
        imageresized = image.resize((170,110), Image.LANCZOS)
        imagetk = ImageTk.PhotoImage(imageresized)
        # canvas.create_image(0,0,image=imagetk)
        canvas.create_image(0,0,image=imagetk, anchor='nw')
        # frame2label = customtkinter.CTkLabel(frameright2, text='', image=frame2image)
        # frame2label.grid(row=1,column=0,padx=(0,0),pady=(0,0), sticky='W')
        
        # def transparent():
        #     alpha = int(.5 * 255)
        #     fill = self.winfo_rgb('green') + (alpha,)
        #     image = Image.new('RGBA', (100-10, 200-10), fill)
        #     images=[]
        #     images.append(ImageTk.PhotoImage(image))
        #     canvas.create_image(10, 100, image=images[-1], anchor='nw')
        #     canvas.create_rectangle(10, 10, 100, 200)
            
        images=[] # prevent garbage collected because PYTHON!!!!!
        imagesleft=[] # prevent garbage collected because PYTHON!!!!!
        imagesright=[] # prevent garbage collected because PYTHON!!!!!
        imagesref=[]
        imagesrefleft=[]
        imagesrefright=[]
        ## https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent
        def create_rectangle_left(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                imagesleft.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                imagesrefleft.append(imageref)
                print(imagesrefleft, len(imagesrefleft))
        def create_rectangle_right(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                imagesright.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                imagesrefright.append(imageref)
                print(imagesrefright, len(imagesrefright))
                
        imagestop=[] # prevent garbage collected because PYTHON!!!!!
        imagesbtm=[] # prevent garbage collected because PYTHON!!!!!
        imagesreftop=[]
        imagesrefbtm=[]
        def create_rectangle_top(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')
                fill = self.winfo_rgb(fill) + (alpha,)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                imagestop.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                imagesreftop.append(imageref)
        def create_rectangle_btm(x1, y1, x2, y2, **kwargs):
            if 'alpha' in kwargs:
                alpha = int(kwargs.pop('alpha') * 255)
                fill = kwargs.pop('fill')                
                winforgb = self.winfo_rgb(fill)
                fill = self.winfo_rgb(fill) + (alpha,)
                # fill = (63325, 52535, 47568)+(179,)
                # print(winforgb, fill)
                image = Image.new('RGBA', (x2-x1, y2-y1), fill)
                image = ImageTk.PhotoImage(image)
                imagesbtm.append(image)
                imageref = canvas.create_image(x1, y1, image=image, anchor='nw')
                imagesrefbtm.append(imageref)

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
        # create_rectangle_btm(0, 100-10, 170, 110, fill='purple', alpha=.6)
        # create_rectangle_btm(0, 100-10, 170, 110, fill='goldenrod', alpha=.8)
        # create_rectangle_btm(0, 100-10, 170, 110, fill='gold', alpha=.5)
        # # create_rectangle(50, 50, 250, 150, fill='green', alpha=.5)
        # # create_rectangle(80, 80, 150, 120, fill='#800000', alpha=.8)
        # # create_rectangle(10, 10, 100, 100, fill='#89abcd', alpha=.9)
        # create_rectangle_left(0, 0, 50, 110, fill='lightgreen', alpha=.3)
        # create_rectangle_right(120, 0, 170, 110, fill='red', alpha=.3)

        frameright3label1 = customtkinter.CTkLabel(frameright3, text='PAUSED Cycle 2', fg_color='transparent', font=('Helvetica',11, 'bold'), text_color='green', anchor='center')
        frameright3label1.grid(row=0,column=0,padx=(0,0),pady=(0,0), sticky='nsew')
        
        self.mainloop()



async def main():
    decepticlone = Decepticlone()


if __name__ == "__main__":
    asyncio.run(main())







