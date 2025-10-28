from tkinter import*
from tkinter import ttk   #GUI library
from PIL import Image,ImageTk #image manipulation library
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Train Dataset")

        #title
        title_lbl= Label(self.root,text = "Photo Sample Training", font = ("times new roman", 35,"bold"),bg= "white" ,fg= "red")
        title_lbl.place(x=0,y=0,width=1540,height=60)

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\facialrecognition.png")
        img = img.resize((1540,320),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 60, width=1540, height=320) # place the label on the root window

        #train data button
        b1_1 = Button(self.root,command=self.train_data, text="Train Data",cursor='hand2',font = ("times new roman", 30,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 0, y = 380, width=1540,height=50)

        #second image
        img1 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\opencv_face_reco_more_data.jpg")
        img1 = img1.resize((1540,370),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image = self.photoimg1) #create a image label
        f_lbl.place(x = 0, y = 430, width=1540, height=370) # place the label on the root window

    #train data function
    def train_data(self):
        data_dir = "data"
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)] # to get a list of complete path of all files or dataset
            
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L") #for gray scale conversion
            imageNP = np.array(img,'uint8') #converting to numpy array of images
            id = int(os.path.split(image)[1].split('.')[1])
            #print(id)

# solved conufion
# Parameter passed: image → a full path string, e.g., "data/User.1.jpg".
# Purpose: Splits a file path into (directory, file_name) using the last path separator (/ or \).
# Returns: a tuple (head, tail) → (directory, file_name)
 
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training", imageNP) #shows the current image with title of window Training
            cv2.waitKey(1) == 13 #enter to stop or close the window or process 

        ids = np.array(ids) #converting the ids to numpy array

# ================Train the classifier and save============= using the local binary pattern classifier algorithm in cv2
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml") #here writing in the file from the dataset later will be read to recognize face but here we are doing face detection not recongnition
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset trained successfully",parent=self.root)

if __name__ == "__main__":
    root = Tk()  #create the main tinker window 
    obj = Train(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.