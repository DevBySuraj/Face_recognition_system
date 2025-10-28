from tkinter import*
from tkinter import ttk   #GUI library
from PIL import Image,ImageTk #image manipulation library
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog

class Helpdesk:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Helpdesk")

        #title
        title_lbl= Label(self.root,text = "Helpdesk", font = ("times new roman", 35,"bold"),bg= "white" ,fg= "blue")
        title_lbl.place(x=0,y=0,width=1540,height=60)

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img = img.resize((1540,720),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 60, width=1540, height=720) # place the label on the root window

        #help info
        text_lbl= Label(f_lbl,text = "Email : 24BCS11025@cuchd.in", font = ("times new roman", 15,"bold"),bg= "white" ,fg= "blue")
        text_lbl.place(x=630,y=230,width=270,height=30)
if __name__ == "__main__":
    root = Tk()  #create the main tinker window 
    obj = Helpdesk(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.x 