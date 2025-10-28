from tkinter import*
from tkinter import ttk   #GUI library
from PIL import Image,ImageTk #image manipulation library
from student import Student
from train import Train
from face_recognition import Face_recognition
import os
from attendence import Attendence
from developer import Developer
from helpdesk import Helpdesk
import tkinter  #for the exit function
from time import strftime
from datetime import datetime 
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\CHANDIGARH-UNIVERSITY-CU-Mohali-Punjab.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 0, width=500, height=130) # place the label on the root window

        #second image
        img1 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\facialrecognition.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image = self.photoimg1) #create a image label
        f_lbl.place(x = 500, y = 0, width=500, height=130) # place the label on the root window

        #third image
        img2 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\images.jpeg")
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image = self.photoimg2) #create a image label
        f_lbl.place(x = 1000, y = 0, width=550, height=130) # place the label on the root window

        #background image
        img3 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\wp2551980.jpg")
        img3 = img3.resize((1530,710),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg3 = ImageTk.PhotoImage(img3)   
        bg_img = Label(self.root, image = self.photoimg3) #create a image label
        bg_img.place(x = 0 , y = 130, width=1530, height=710) # place the label on the root window

        #title
        title_lbl= Label(bg_img,text = "FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font = ("times new roman", 35,"bold"), bg="white",fg= "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #function for time call
        def time():
            string = strftime('%H:%M:%S %p')
            dt_lbl.config(text = string)
            dt_lbl.after(1000,time)

        #time label
        dt_lbl= Label(title_lbl, font = ("times new roman", 13,"bold"), bg="white",fg= "blue")
        dt_lbl.place(x=0,y=0,width=110,height=45)
        time()
        

        # student button
        img4 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\gettyimages-1022573162.jpg")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg4 = ImageTk.PhotoImage(img4) 

        b1 = Button(bg_img, image = self.photoimg4,command=self.student_details,cursor='hand2')  
        b1.place(x = 200, y = 100, width=220,height=220)

        b1_1 = Button(bg_img, text="Student Details",cursor='hand2',command=self.student_details,font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 200, y = 300, width=220,height=40)

        # detect face button
        img5 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\face_detector1.jpg")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg5 = ImageTk.PhotoImage(img5) 

        b1 = Button(bg_img,command=self.face_recogn, image = self.photoimg5,cursor='hand2')  
        b1.place(x = 500, y = 100, width=220,height=220)

        b1_1 = Button(bg_img,command=self.face_recogn, text="Face Detector",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 500, y = 300, width=220,height=40)

        # Attendence button
        img6 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\report.jpg")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg6 = ImageTk.PhotoImage(img6) 

        b1 = Button(bg_img,command=self.attendence_system, image = self.photoimg6,cursor='hand2')  
        b1.place(x = 800, y = 100, width=220,height=220)

        b1_1 = Button(bg_img,command=self.attendence_system, text="Attendence",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 800, y = 300, width=220,height=40)

        # help button
        img7 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg7 = ImageTk.PhotoImage(img7) 

        b1 = Button(bg_img,command=self.help_page, image = self.photoimg7,cursor='hand2')  
        b1.place(x = 1100, y = 100, width=220,height=220)

        b1_1 = Button(bg_img,command=self.help_page, text="Help Desk",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 1100, y = 300, width=220,height=40)

        # Train data button
        img8 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\Train.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg8 = ImageTk.PhotoImage(img8) 

        b1 = Button(bg_img,command=self.Train_data_set, image = self.photoimg8,cursor='hand2')  
        b1.place(x = 200, y = 360, width=220,height=220)

        b1_1 = Button(bg_img,command=self.Train_data_set, text="Train Data",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 200, y = 560, width=220,height=40)

        # Photos button
        img9 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg9 = ImageTk.PhotoImage(img9) 

        b1 = Button(bg_img,command=self.open_img_dataset, image = self.photoimg9,cursor='hand2')  
        b1.place(x = 500, y = 360, width=220,height=220)

        b1_1 = Button(bg_img,command=self.open_img_dataset, text="Photos",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 500, y = 560, width=220,height=40)

        # Developer button
        img10 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg10 = ImageTk.PhotoImage(img10) 

        b1 = Button(bg_img,command=self.developer_page, image = self.photoimg10,cursor='hand2')  
        b1.place(x = 800, y = 360, width=220,height=220)

        b1_1 = Button(bg_img,command=self.developer_page, text="Developer",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 800, y = 560, width=220,height=40)

        # Exit button
        img11 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\exit.jpg")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg11 = ImageTk.PhotoImage(img11) 

        b1 = Button(bg_img,command=self.iExit, image = self.photoimg11,cursor='hand2')  
        b1.place(x = 1100, y = 360, width=220,height=220)

        b1_1 = Button(bg_img,command=self.iExit, text="Exit",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 1100, y = 560, width=220,height=40)


    def open_img_dataset(self):
        os.startfile("data")
    
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition System", "Are you sure to exit this project", parent = self.root)
        if self.iExit :
            self.root.destroy()
        else:
            return

        # ------------------ button function-----------------------#
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def Train_data_set(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recogn(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
        
    def attendence_system(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def developer_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpdesk(self.new_window)

if __name__ == "__main__":
    root = Tk()  #create the main tinker window
    obj = Face_Recognition_System(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.