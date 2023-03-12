import tkinter as tk
from tkinter import ttk
import serial
from time import sleep
# from PIL import ImageTk
from tkinter.filedialog import askopenfilename

TITLEFONT = ("calibri", 30)
CAPTIONFONT = ()
BUTTONFONT = ()

def stopCode():
    exit

class AngklungApp(tk.Tk):
     
    # __init__ function for class AngklungApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (mainMenu, modeManual, modeOtomatis):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(mainMenu)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class mainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        welcomesign = tk.Label(self, text="SELAMAT DATANG", anchor="n", font=TITLEFONT)
        
        modeManual_btn = ttk.Button(self, text ="Mode Manual",
        command = lambda : controller.show_frame(modeManual))

        modeOtomatis_btn = ttk.Button(self, text ="Mode Otomatis",
        command = lambda : controller.show_frame(modeOtomatis))

class modeManual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class modeOtomatis(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


root = AngklungApp()
root.title("Angklung")
root.geometry('1024x600')
root.mainloop()