from tkinter import*
from tkinter import ttk   #GUI library
from PIL import Image,ImageTk #image manipulation library
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime 

class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition")

        #title
        title_lbl= Label(self.root,text = "FACE RECOGNITION", font = ("times new roman", 35,"bold"),bg= "white" ,fg= "dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\face_detector1.jpg")
        img = img.resize((610,690),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 60, width=610, height=690) # place the label on the root window
    
        #second image
        img1 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img1 = img1.resize((930,690),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image = self.photoimg1) #create a image label
        f_lbl.place(x = 610, y = 60, width=930, height=690) # place the label on the root window

        #face detection button
        b1_1 = Button(f_lbl,command=self.recognition,text="Face Detection",cursor='hand2',font = ("times new roman", 15,"bold"), bg="darkblue",fg= "white")  
        b1_1.place(x = 360, y = 610, width=200,height=40)

        #bottom label
        title_lbl= Label(self.root,text = "Frontal Face Detector", font = ("times new roman", 20,"bold"),bg= "white" ,fg= "dark blue")
        title_lbl.place(x=0,y=730 ,width=1540,height=60)


        #==============mark attendence============



    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry = line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (r not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H: %M: %S") 
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")    

        #==============face recognition============
    def recognition(self):
        def draw_boundary(img, classifier,scaleFactor, minNeighbour, color, text, clf ):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            coord = []

            for (x,y,h,w) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict= clf.predict(gray_image[y:y+h, x:x+h]) # id cuz we train the data on faces and ids so it will predict this  clf.train(faces,ids)
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = "localhost", username = "root", password = "cyberhunter", database = "face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute(f"select Name from student where Student_Id={str(id)}")       
                n = my_cursor.fetchone()   #return a single row or record 
                # n = n[0]
                n = "+".join(n) 

                my_cursor.execute(f"select Roll from student where Student_Id={str(id)}")       
                r = my_cursor.fetchone()   #return a single row or record 
                # r = r[0]
                r = "+".join(r)

                my_cursor.execute(f"select Dep from student where Student_Id={str(id)}")       
                d = my_cursor.fetchone()   #return a single row or record 
                # d = d[0]
                d = "+".join(d)

                my_cursor.execute(f"select Student_Id from student where Student_Id={str(id)}")    #student id is intger    
                i = my_cursor.fetchone()   #return a single row or record 
                # i = i[0]
                i = str(i[0])
                # i = "+".join(i)

                if confidence > 75:
                    cv2.putText(img,f"Student ID: {i}",(x, y-80), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  # x and y are rectangle's starting origin coordinates and we want roll above rectangle that's why y- 55
                    cv2.putText(img,f"Roll: {r}",(x, y-55), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  # x and y are rectangle's starting origin coordinates and we want roll above rectangle that's why y- 55
                    cv2.putText(img,f"Name: {n}",(x, y-30), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept: {d}",(x, y-5), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x, y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord = [x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img  
        
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")    # here reading the file made from datasets in the train.py   

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face_cascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()  #create the main tinker window 
    obj = Face_recognition(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.