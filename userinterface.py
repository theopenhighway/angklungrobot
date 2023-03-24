import tkinter as tk
from tkinter import ttk
import serial
from time import sleep
# from PIL import ImageTk
from tkinter.filedialog import askopenfilename

# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

# fonts
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
        welcomesign.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        modeManual_btn = tk.Button(self, text ="Mode Manual",
        command = lambda : controller.show_frame(modeManual), height=15, width=30, font=BUTTONFONT)
        modeManual_btn.grid()

        modeOtomatis_btn = tk.Button(self, text ="Mode Otomatis",
        command = lambda : controller.show_frame(modeOtomatis), height= 15, width= 30, font=BUTTONFONT)
        modeOtomatis_btn.grid()

class modeManual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        manualSign = tk.Label(self, text="MODE MANUAL", anchor="n", font=TITLEFONT)
        manualSign.grid(row = 0, column = 4, padx = 10, pady = 10)

        # Back to main menu button
        backToMainMenu = tk.Button(self, command = lambda : controller.show_frame(mainMenu), height= 5, width= 5)
        # click_btn= tk.PhotoImage(file='clickme.png')
        backToMainMenu.grid()
        

        
class modeOtomatis(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        otomatisSign = tk.Label(self, text="MODE OTOMATIS", anchor="n", font=TITLEFONT)
        otomatisSign.grid(row = 0, column = 4, padx = 10, pady = 10)
        backToMainMenu = tk.Button(self, command = lambda : controller.show_frame(mainMenu), height= 5, width= 5)
        # click_btn = tk.PhotoImage(file='clickme.png')
        backToMainMenu.grid()
        


root = AngklungApp()
root.title("Angklung")
root.geometry('1024x600')
root.mainloop()