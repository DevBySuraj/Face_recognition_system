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

mydata = [] #global variable - data from csv file will come here
class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Attendence Here")
# ===================variables=================
        self.var_atten = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_atten_st = StringVar()

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\smart-attendance.jpg")
        img = img.resize((770,200),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 0, width=770, height=200) # place the label on the root window

        #second image
        img1 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((770,200),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image = self.photoimg1) #create a image label
        f_lbl.place(x = 770, y = 0, width=770, height=200) # place the label on the root window

        #background image
        img3 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\wp2551980.jpg")
        img3 = img3.resize((1540,600),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg3 = ImageTk.PhotoImage(img3)   
        bg_img = Label(self.root, image = self.photoimg3) #create a image label
        bg_img.place(x = 0 , y = 200, width=1540, height=600) # place the label on the root window

        #title
        title_lbl= Label(bg_img,text = "ATTENDENCE MANAGEMENT SYSTEM", font = ("times new roman", 35,"bold"), bg="white",fg= "green")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        #frame
        main_frame = Frame(bg_img, bd = 2,bg = "white")
        main_frame.place(x = 15, y = 50 , width= 1500 , height=540)

        #Left label frame
        Left_frame = LabelFrame(main_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Student Attendence Details") #relif == framestyle
        Left_frame.place(x = 10, y = 10, width= 730, height=520)

        img_left = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image = self.photoimg_left) #create a image label
        f_lbl.place(x = 5, y = 0, width=720, height=130) # place the label on the root window

        #left inside frame
        left_inside_frame = Frame(Left_frame, bd = 2, relief=RIDGE, bg = "white")
        left_inside_frame.place(x = 5, y = 140 , width= 715 , height=350)

        #attendence id
        attendence_id_label = Label(left_inside_frame,text = "Attendence ID:", font = ("times new roman", 12,"bold"),bg = "white")
        attendence_id_label.grid(row=0, column=0,padx=10,pady=10,sticky = W) #stickey fixes the alignment of the label name 
        attendence_id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten,width=20,font = ("times new roman",12,"bold"))
        attendence_id_entry.grid(row=0, column=1,padx=10,pady=10,sticky = W)

        #Roll
        Roll_label = Label(left_inside_frame,text = "Roll No:", font = ("times new roman", 12,"bold"),bg = "white")
        Roll_label.grid(row=0, column=2,padx=30,pady=10,sticky = W) #stickey fixes the alignment of the label name 
        Roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=20,font = ("times new roman",12,"bold"))
        Roll_entry.grid(row=0, column=3,padx=10,pady=10,sticky = W)

        #Name
        Name_label = Label(left_inside_frame,text = "Name:", font = ("times new roman", 12,"bold"),bg = "white")
        Name_label.grid(row=1, column=0,padx=10,pady=10,sticky = W) #stickey fixes the alignment of the label name 
        Name_entry = ttk.Entry(left_inside_frame,textvariable = self.var_name,width=20,font = ("times new roman",12,"bold"))
        Name_entry.grid(row=1, column=1,padx=10,pady=10,sticky = W)

        #Department
        Department_label = Label(left_inside_frame,text = "Department:", font = ("times new roman", 12,"bold"),bg = "white")
        Department_label.grid(row=1, column=2,padx=30,pady=10,sticky = W) #stickey fixes the alignment of the label Department 
        Department_entry = ttk.Entry(left_inside_frame,textvariable = self.var_dept,width=20,font = ("times new roman",12,"bold"))
        Department_entry.grid(row=1, column=3,padx=10,pady=10,sticky = W)

        #Time
        Time_label = Label(left_inside_frame,text = "Time:", font = ("times new roman", 12,"bold"),bg = "white")
        Time_label.grid(row=2, column=0,padx=10,pady=10,sticky = W) #stickey fixes the alignment of the label Time 
        Time_entry = ttk.Entry(left_inside_frame,textvariable = self.var_time,width=20,font = ("times new roman",12,"bold"))
        Time_entry.grid(row=2, column=1,padx=10,pady=10,sticky = W)

        #Date
        Date_label = Label(left_inside_frame,text = "Date:", font = ("times new roman", 12,"bold"),bg = "white")
        Date_label.grid(row=2, column=2,padx=30,pady=10,sticky = W) #stickey fixes the alignment of the label Date 
        Date_entry = ttk.Entry(left_inside_frame,textvariable = self.var_date,width=20,font = ("times new roman",12,"bold"))
        Date_entry.grid(row=2, column=3,padx=10,pady=10,sticky = W)

        #attendence status
        class_label = Label(left_inside_frame,text = "Attendence Status:", font = ("times new roman", 12,"bold"),bg = "white")
        class_label.grid(row=3, column=0,padx=10,pady=10,sticky = W) #stickey fixes the alignment of the label name 

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_st,font = ("times new roman",12,"bold"),state="readonly",width = 18)
        self.atten_status["values"] = ("Status","Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row = 3, column= 1,padx=10,pady=10,sticky = W)

        #button frame
        button_frame = Frame(left_inside_frame,bd = 2, relief=RIDGE,bg = 'white')
        button_frame.place(x = 5, y=270, width= 695, height= 35 )

        import_button = Button(button_frame,command=self.import_csv,text = "Import csv", width= 18,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        import_button.grid(row = 0, column= 0)

        export_button = Button(button_frame,command=self.export_csv,text = "Export csv", width= 18,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        export_button.grid(row = 0, column= 1)

        update_button = Button(button_frame,text = "Update", width= 19,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        update_button.grid(row = 0, column= 2)

        reset_button = Button(button_frame,command=self.reset_data,text = "Reset", width= 19,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        reset_button.grid(row = 0, column= 3)


        #Right label frame
        Right_frame = LabelFrame(main_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Attendence Details")
        Right_frame.place(x = 750, y = 10, width= 730, height=520)

        #Right inside frame
        table_frame = Frame(Right_frame, bd = 2, relief=RIDGE, bg = "white")
        table_frame.place(x = 5, y = 5 , width= 715 , height=480)

        # ============scroll bar table===============
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Attendence_report_table = ttk.Treeview(table_frame, column = ("id", "roll", "name", "dept","time","date", "attendence"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command=self.Attendence_report_table.xview)
        scroll_y.config(command=self.Attendence_report_table.yview)

        self.Attendence_report_table.heading("id",text= "Attendence ID")
        self.Attendence_report_table.heading("roll", text="Roll No")
        self.Attendence_report_table.heading("name", text="Student Name")
        self.Attendence_report_table.heading("dept", text="Department")
        self.Attendence_report_table.heading("time", text="Time")
        self.Attendence_report_table.heading("date", text="Date")
        self.Attendence_report_table.heading("attendence", text="Attendence")
        self.Attendence_report_table["show"] = "headings"

        self.Attendence_report_table.column("id",width= 100)
        self.Attendence_report_table.column("roll", width=100)
        self.Attendence_report_table.column("name", width=100) 
        self.Attendence_report_table.column("dept", width=100)
        self.Attendence_report_table.column("time", width=100)
        self.Attendence_report_table.column("date", width=100)
        self.Attendence_report_table.column("attendence", width=100)

        self.Attendence_report_table.pack(fill=BOTH, expand=1) #pack : to pack the heading of the column name in the table
        self.Attendence_report_table.bind("<ButtonRelease>", self.get_cursor)

        # ===============fetch data==============
    def fetch_data(self, rows):  #fetches the data from the csv and show in the attendence table
        self.Attendence_report_table.delete(*self.Attendence_report_table.get_children())
        for row in rows:
            self.Attendence_report_table.insert("", END, values=row)
    
    #import csv
    def import_csv(self): #ask to open files and select the csv file then read and passes to fetch func which inserts the data in the attendence table
        global mydata
        mydata.clear()
        file_name  = filedialog.askopenfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"),("ALL File", "*.*")),parent=self.root)
        with open (file_name) as myfile: #by default in the read mode
            csvread = csv.reader(myfile,delimiter= ",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #export csv
    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No data found")
                return False
            file_name  = filedialog.asksaveasfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"),("ALL File", "*.*")),parent=self.root)
            with open(file_name, "w", newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for row in mydata:
                    exp_write.writerow(row)
                messagebox.showinfo("Data Export",f"Data exported successfully to {os.path.basename(file_name)}")
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root ) 


    #get cursor
    def get_cursor(self,event = ""):
        cursor_row = self.Attendence_report_table.focus()
        content = self.Attendence_report_table.item(cursor_row)
        rows = content['values']
        self.var_atten.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dept.set(rows[3]) 
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_atten_st.set(rows[6])


    #reset data
    def reset_data(self):
        self.var_atten.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("") 
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten_st.set("Status")

if __name__ == "__main__":
    root = Tk()  #create the main tinker window 
    obj = Attendence(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.  