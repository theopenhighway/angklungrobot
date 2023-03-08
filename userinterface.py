import tkinter as tk
import serial
from time import sleep
from PIL import ImageTk
from tkinter.filedialog import askopenfilename



def main():
    ser = serial.Serial('/dev/ttACM0',9600)
    ser.flush()

    # initiallize app
    root = tk.TK()

    # screen dimension
    root.geometry('1024x600')

    #run app
    root.mainloop()  
    
if __name__ == '__main__':
    main()
    