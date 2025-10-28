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

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Developer")

        #title
        title_lbl= Label(self.root,text = "Developer", font = ("times new roman", 35,"bold"),bg= "white" ,fg= "blue")
        title_lbl.place(x=0,y=0,width=1540,height=60)

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\dev.jpg")
        img = img.resize((1540,720),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 60, width=1540, height=720) # place the label on the root window

        #frame
        main_frame = Frame(f_lbl, bd = 2,bg = "white")
        main_frame.place(x = 1000, y = 10 , width= 510 , height=690)

        #second image
        img1 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\20250903_1617_Cyberpunk Teen Silhouette_simple_compose_01k47jzkxqee89es89k19181gw.png")
        img1 = img1.resize((200,300),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(main_frame, image = self.photoimg1) #create a image label
        f_lbl.place(x = 290, y = 15, width=200, height=300) # place the label on the root window

        #background image
        img3 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img3 = img3.resize((510,315),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg3 = ImageTk.PhotoImage(img3)   
        bg_img = Label(main_frame, image = self.photoimg3) #create a image label
        bg_img.place(x = 0 , y = 315, width=510, height=375) # place the label on the root window

        #text developer info
        text_lbl= Label(main_frame,text = "Hello I'm Suraj", font = ("times new roman", 15,"bold"),bg= "white" ,fg= "blue")
        text_lbl.place(x=10,y=30,width=270,height=30)

        text_lbl1= Label(main_frame,text = "This is the python project", font = ("times new roman", 15,"bold"),bg= "white" ,fg= "blue")
        text_lbl1.place(x=10,y=90,width=270,height=30)

        text_lbl2= Label(main_frame,text = "for the 3rd semester", font = ("times new roman", 15,"bold"),bg= "white" ,fg= "blue")
        text_lbl2.place(x=10,y=150,width=270,height=30)
if __name__ == "__main__":
    root = Tk()  #create the main tinker window 
    obj = Developer(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.x 