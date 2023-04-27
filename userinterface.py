import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from tkinter import filedialog as fd
# import serial
from time import sleep
from tkinter.filedialog import askopenfilename
import os
# import midireader_man
# import midireader

# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

# fonts
TITLEFONT = ("calibri", 30)
CAPTIONFONT = ("calibri", 15)
BUTTONFONT = ("calibri", 20)

# screen dimension (pixels)
HEIGHT = 9
WIDTH = 9

# color
BACKGROUND = '#cfbdb0'


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
  
            frame = F(container, self,bg=BACKGROUND)
  
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
    def __init__(self, parent, controller, bg=None, fg=None):
        tk.Frame.__init__(self, parent, bg=bg, fg=fg)
        welcomesign = tk.Label(self, text="SELAMAT DATANG", anchor="n", font=TITLEFONT, bg=BACKGROUND)
        welcomesign.grid(row = 0, column = 10, padx = 10, pady = 10)
        
        modeManual_btn = tk.Button(self, text ="Mode Manual",
        command = lambda : controller.show_frame(modeManual), height=5, width=20, font=BUTTONFONT)
        modeManual_btn.grid(row = 400, column = 70, padx = 40, pady = 20, sticky="ew")

        modeOtomatis_btn = tk.Button(self, text ="Mode Otomatis",
        command = lambda : controller.show_frame(modeOtomatis), height= 5, width= 20, font=BUTTONFONT)
        modeOtomatis_btn.grid(row = 400, column = 10,  padx = 40, pady = 20, sticky="ew")

class modeManual(tk.Frame):
    def __init__(self, parent, controller, bg=None, fg=None):
        tk.Frame.__init__(self, parent, bg=bg, fg=fg)

        manualSign = tk.Label(self, text="MODE MANUAL", anchor="n", font=TITLEFONT, bg=BACKGROUND)
        manualSign.grid(row = 200, column = 5, padx = 10, pady = 50, sticky="n")

        # Back to main menu button
        backToMainMenu = tk.Button(self, command = lambda : controller.show_frame(mainMenu), height= 5, width= 5)
        # click_btn= tk.PhotoImage(file='clickme.png')
        backToMainMenu.grid(row = 0, column = 0, padx = 2, pady = 2,sticky="nw")

class modeOtomatis(tk.Frame):
    def __init__(self, parent, controller, bg=None, fg=None):
        tk.Frame.__init__(self, parent, bg=bg, fg=fg)
        otomatisSign = tk.Label(self, text="MODE OTOMATIS", anchor="n", font=TITLEFONT, bg=BACKGROUND)
        otomatisSign.grid(row = 0, column = 5, padx = 200, pady = 50)

        # image assets
        self.backButtonPic = tk.PhotoImage(file = "C:\\Users\\milo\\personal projects\\angklungrobot\\gui_asset\\backButton.png")

        backToMainMenu = tk.Button(self, command = lambda : controller.show_frame(mainMenu), height= 5, width= 5, image=self.backButtonPic)
        # click_btn = tk.PhotoImage(file='clickme.png')
        backToMainMenu.grid(row = 0, column = 0, padx = 300, pady = 30)

        # get list of songs from a designated folder onto a listbox
        dir_path = "C:\\Users\\milo\\personal projects\\angklungrobot\\midi_files\\"
        songList = tk.Listbox(self)
        
        i = 0
        for file in os.listdir(dir_path):
            
            if os.path.isfile(os.path.join(dir_path, file)):
                i = i + 1
                songList.insert(i,file)

        songList.grid(row = 0, column = 0, sticky = "w")
        
        # songList.bind("<<ListboxSelect>>", songList)

        # self.scroll = ttk.Scrollbar(self)
        # self.scroll.grid()

        
        # songList.configure(yscrollcommand=self.scroll.set)
        # self.scroll.configure(command=songList.yview)
        # play button --> run midireader.py

        



root = AngklungApp()
root.title("Angklung")
root.geometry('1024x600')
root.mainloop()
