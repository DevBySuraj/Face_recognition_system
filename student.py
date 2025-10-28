from tkinter import*
from tkinter import ttk   #GUI library
from PIL import Image,ImageTk #image manipulation library
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # ============variables===============
        self.var_dep = StringVar()        
        self.var_course = StringVar()        
        self.var_year = StringVar()        
        self.var_semester = StringVar()        
        self.var_id = StringVar()        
        self.var_name = StringVar()        
        self.var_div = StringVar()        
        self.var_roll = StringVar()        
        self.var_gender = StringVar()        
        self.var_dob = StringVar()        
        self.var_email = StringVar()        
        self.var_phone = StringVar()        
        self.var_address = StringVar()        
        self.var_teacher = StringVar()        

        #first image
        img = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\smart-attendance.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg) #create a image label
        f_lbl.place(x = 0, y = 0, width=500, height=130) # place the label on the root window

        #second image
        img1 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image = self.photoimg1) #create a image label
        f_lbl.place(x = 500, y = 0, width=500, height=130) # place the label on the root window

        #third image
        img2 = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\images (1).jpeg")
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
        title_lbl= Label(bg_img,text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 35,"bold"), bg="white",fg= "dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
 
        #frame
        main_frame = Frame(bg_img, bd = 2,bg = "white")
        main_frame.place(x = 15, y = 50 , width= 1495 , height=605)

        #Left label frame
        Left_frame = LabelFrame(main_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Student Details") #relif == framestyle
        Left_frame.place(x = 10, y = 10, width= 730, height=580)

        img_left = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image = self.photoimg_left) #create a image label
        f_lbl.place(x = 5, y = 0, width=720, height=130) # place the label on the root window
        
        #current course frame
        current_course_frame = LabelFrame(Left_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Current course info")
        current_course_frame.place(x = 10, y = 135, width= 710, height=110)

        #label 1,combo 1
        dep_label = Label(current_course_frame,text = "Departement", font = ("times new roman", 12,"bold"),bg = "white")
        dep_label.grid(row=0, column=0,padx=10,sticky = W) #stickey fixes the alignment of the label name 
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font = ("times new roman",12,"bold"),state="readonly",width = 20)
        dep_combo["values"] = ("Select department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column= 1,padx=2,pady=10,sticky=W)# 

        #label 2, combo 2
        course_label = Label(current_course_frame,text = "Course", font = ("times new roman", 12,"bold"),bg = "white")
        course_label.grid(row=0, column=2,padx=10,sticky = W)#
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font = ("times new roman",12,"bold"),state="readonly",width = 20)
        course_combo["values"] = ("Select course", "FE", "TE", "CS", "BE")
        course_combo.current(0)
        course_combo.grid(row = 0, column= 3,padx=2,pady=10,sticky = W)#

        #label 3, combo 3
        year_label = Label(current_course_frame,text = "Year", font = ("times new roman", 12,"bold"),bg = "white")
        year_label.grid(row=1, column=0,padx=10,sticky = W)#
        year_combo = ttk.Combobox(current_course_frame,textvariable = self.var_year,font = ("times new roman",12,"bold"),state="readonly",width = 20)
        year_combo["values"] = ("Select year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0) 
        year_combo.grid(row = 1, column= 1,padx=2,pady=10,sticky = W)# 

        #label 4, combo 4
        sem_label = Label(current_course_frame,text = "Semester", font = ("times new roman", 12,"bold"),bg = "white")
        sem_label.grid(row=1, column=2,padx=10,sticky = W)#
        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font = ("times new roman",12,"bold"),state="readonly",width = 20)
        sem_combo["values"] = ("Select semester", "1st", "2nd", "3rd", "4th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row = 1, column= 3,padx=2,pady=10,sticky = W)#

        #class student information frame
        class_student_frame = LabelFrame(Left_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Class Student Information")
        class_student_frame.place(x = 10, y = 250, width= 710, height=300)
        
        #student id
        student_id_label = Label(class_student_frame,text = "Student ID:", font = ("times new roman", 12,"bold"),bg = "white")
        student_id_label.grid(row=0, column=0,padx=10,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font = ("times new roman",12,"bold"))
        student_id_entry.grid(row=0, column=1,padx=10,pady=5,sticky = W)

        #student name
        student_name_label = Label(class_student_frame,text = "Student Name:", font = ("times new roman", 12,"bold"),bg = "white")
        student_name_label.grid(row=0, column=2,padx=20,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font = ("times new roman",12,"bold"))
        student_name_entry.grid(row=0, column=3,padx=20,pady=5,sticky = W)

        #Class Division
        class_label = Label(class_student_frame,text = "Class Division:", font = ("times new roman", 12,"bold"),bg = "white")
        class_label.grid(row=1, column=0,padx=10,pady=5,sticky = W) #stickey fixes the alignment of the label name 

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font = ("times new roman",12,"bold"),state="readonly",width = 18)
        div_combo["values"] = ("Select Divison","A", "B", "C","D")
        div_combo.current(0)
        div_combo.grid(row = 1, column= 1,padx=10,pady=5,sticky = W)#

        #Roll no
        Rollno_label = Label(class_student_frame,text = "Roll No:", font = ("times new roman", 12,"bold"),bg = "white")
        Rollno_label.grid(row=1, column=2,padx=20,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        Rollno_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font = ("times new roman",12,"bold"))
        Rollno_entry.grid(row=1, column=3,padx=20,pady=5,sticky = W)
        
        #Gender
        gender_label = Label(class_student_frame,text = "Gender:", font = ("times new roman", 12,"bold"),bg = "white")
        gender_label.grid(row=2, column=0,padx=10,pady=5,sticky = W) #stickey fixes the alignment of the label name 

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font = ("times new roman",12,"bold"),state="readonly",width = 18)
        gender_combo["values"] = ("Select Gender","Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row = 2, column= 1,padx=10,pady=5,sticky = W)#

        #DOB
        dob_label = Label(class_student_frame,text = "DOB:", font = ("times new roman", 12,"bold"),bg = "white")
        dob_label.grid(row=2, column=2,padx=20,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font = ("times new roman",12,"bold"))
        dob_entry.grid(row=2, column=3,padx=20,pady=5,sticky = W)

        #Email
        email_label = Label(class_student_frame,text = "Email:", font = ("times new roman", 12,"bold"),bg = "white")
        email_label.grid(row=3, column=0,padx=10,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font = ("times new roman",12,"bold"))
        email_entry.grid(row=3, column=1,padx=10,pady=5,sticky = W)

        #Phone no
        phone_label = Label(class_student_frame,text = "Phone no:", font = ("times new roman", 12,"bold"),bg = "white")
        phone_label.grid(row=3, column=2,padx=20,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font = ("times new roman",12,"bold"))
        phone_entry.grid(row=3, column=3,padx=20,pady=5,sticky = W)

        #Adress  
        Adress_label = Label(class_student_frame,text = "Address:", font = ("times new roman", 12,"bold"),bg = "white")
        Adress_label.grid(row=4, column=0,padx=10,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        Adress_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font = ("times new roman",12,"bold"))
        Adress_entry.grid(row=4, column=1,padx=10,pady=5,sticky = W)

        #Teacher
        Teacher_label = Label(class_student_frame,text = "Teacher Name:", font = ("times new roman", 12,"bold"),bg = "white")
        Teacher_label.grid(row=4, column=2,padx=20,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        Teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font = ("times new roman",12,"bold"))
        Teacher_entry.grid(row=4, column=3,padx=20,pady=5,sticky = W)


        #radio button
        self.var_rad1 = StringVar()
        radio_btn1 = ttk.Radiobutton(class_student_frame,variable=self.var_rad1,text = "Take Photo Sample", value = "Yes")
        radio_btn1.grid(row = 6, column= 0,padx= 12)

        radio_btn2 = ttk.Radiobutton(class_student_frame,variable=self.var_rad1,text = "No Photo Sample", value = "No")
        radio_btn2.grid(row = 6, column= 1,padx=5)

        #button frame
        button_frame = Frame(class_student_frame,bd = 2, relief=RIDGE,bg = 'white')
        button_frame.place(x = 5, y=200, width= 695, height= 70  )
        #class_student_frame.place(x = 10, y = 250, width= 710, height=300)

        save_button = Button(button_frame,command=self.add_data,text = "Save", width= 18,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        save_button.grid(row = 0, column= 0)

        update_button = Button(button_frame,command=self.update_data,text = "Update", width= 18,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        update_button.grid(row = 0, column= 1)

        delete_button = Button(button_frame,command=self.delete_data,text = "Delete", width= 19,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        delete_button.grid(row = 0, column= 2)

        reset_button = Button(button_frame,command=self.reset_data,text = "Reset", width= 19,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        reset_button.grid(row = 0, column= 3)

        #button frame 1
        button_frame1 = Frame(class_student_frame,bd = 2, relief=RIDGE,bg = 'white')
        button_frame1.place(x = 5, y=235, width= 695, height= 35  )

        take_photo_btn  = Button(button_frame1,command=self.generate_dataset,text= "Take Photo sample",width= 38,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white' )
        update_photo_btn  = Button(button_frame1,text= "Update Photo sample",width= 38,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white' )
        take_photo_btn.grid(row=0, column=0)
        update_photo_btn.grid(row=0, column=1)

       #---------------------------------------------------------------#

        #Right label frame
        Right_frame = LabelFrame(main_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Student Details")
        Right_frame.place(x = 750, y = 10, width= 730, height=580)

        img_right = Image.open(r"C:\Users\Suraj\Desktop\Projects\college_images\gettyimages-1022573162.jpg")
        img_right = img_right.resize((720,130),Image.Resampling.LANCZOS)  #ANTIALIAS is depreciated in pillow new version use lanczos instead
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame, image = self.photoimg_right) #create a image label
        f_lbl.place(x = 5, y = 0, width=720, height=130) # place the label on the root window

        #Search frame
        Search_frame = LabelFrame(Right_frame,bd = 2,bg = "white", relief=RIDGE ,font = ("times new roman",12,"bold"), text="Search System")
        Search_frame.place(x = 10, y = 135, width= 710, height=70)

        search_label = Label(Search_frame, text = "Search By:", font = ("times new roman", 12,"bold"),bg = "red",fg = "white")
        search_label.grid(row=0, column=0,padx=10,pady=5,sticky = W) #stickey fixes the alignment of the label name 
        search_combo = ttk.Combobox(Search_frame,font = ("times new roman",12,"bold"),state="readonly",width = 15)
        search_combo["values"] = ("Select", "Name", "Roll no", "Phone no")
        search_combo.current(0)
        search_combo.grid(row = 0, column= 1,padx=2,pady=10,sticky = W)#  

        search_entry = ttk.Entry(Search_frame,width=15,font = ("times new roman",12,"bold"))
        search_entry.grid(row=0, column=2,padx=10,pady=5,sticky = W) 

        search_button = Button(Search_frame,text = "Search", width= 15,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        search_button.grid(row = 0, column= 3,padx = 4,pady= 4)

        showa_all_button = Button(Search_frame,text = "Show All", width= 15,font = ("times new roman",12,"bold"),bg = "darkblue", fg = 'white')
        showa_all_button.grid(row = 0, column= 4,padx = 4,pady= 4)


        #table frame
        table_frame = Frame(Right_frame, bd = 2, relief=RIDGE,bg = "white")
        table_frame.place(x= 10, y = 210, width= 710, height= 350)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course","year", "sem", "id", "name", "divison", "roll no", "gender", "DOB", "email","phone", "address", "teacher name","photo" ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) #fill the scroll bar in x
        scroll_y.pack(side=RIGHT,fill=Y) #fill the scroll bar in y
        scroll_x.config(command=self.student_table.xview) #help to move in x axis in the student table
        scroll_y.config(command=self.student_table.yview) #help to move in y axis in the student table


        #giving name to the headings
        self.student_table.heading("dep", text = "Department") #name of the column 
        self.student_table.heading("course", text = "Course")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("sem", text = "Semester")
        self.student_table.heading("id", text = "Student ID")
        self.student_table.heading("name", text = "Student Name")
        self.student_table.heading("divison", text = "Division")
        self.student_table.heading("roll no", text = "Roll no")
        self.student_table.heading("gender", text = "Gender")
        self.student_table.heading("DOB", text = "DOB")
        self.student_table.heading("email", text = "Email ID")
        self.student_table.heading("phone", text = "Phone no")
        self.student_table.heading("address", text = "Address")
        self.student_table.heading("teacher name", text = "Teacher name")
        self.student_table.heading("photo", text = "Photo Sample Status")
        self.student_table["show"] = "headings"
        
        #setting the the width
        self.student_table.column("dep", width = 100 ) #name of the column 
        self.student_table.column("course", width =100)
        self.student_table.column("year", width= 100)
        self.student_table.column("sem", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("name", width = 150)
        self.student_table.column("divison", width = 100)
        self.student_table.column("roll no", width =100 )
        self.student_table.column("gender", width =100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("email", width = 200)
        self.student_table.column("phone", width = 150)
        self.student_table.column("address", width = 300)
        self.student_table.column("teacher name", width = 150)
        self.student_table.column("photo", width = 150)

        self.student_table.pack(fill=BOTH, expand = 1) #displays on the table or pack on the table
        self.student_table.bind("<ButtonRelease>",self.get_cursor)   #here only give get_cursor not call like this get_cursor(). works if button is clicked/released on the table
        self.fetch_data() #fetch data directly after table , live change

#===============function declaration =================
    def add_data(self): #called by save button (given in the command of save button)
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "": #get helps to get the data from the entry field or combo text variables
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "cyberhunter", database = "face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( #inserting all these data of the entry field to the table created in the mysql one by one after each save in 1 row
                                                                                                                self.var_dep.get(),         
                                                                                                                self.var_course.get(),         
                                                                                                                self.var_year.get(),         
                                                                                                                self.var_semester.get(),         
                                                                                                                self.var_id.get(),         
                                                                                                                self.var_name.get(),         
                                                                                                                self.var_div.get(),         
                                                                                                                self.var_roll.get(),         
                                                                                                                self.var_gender.get(),         
                                                                                                                self.var_dob.get(),         
                                                                                                                self.var_email.get(),         
                                                                                                                self.var_phone.get(),         
                                                                                                                self.var_address.get(),         
                                                                                                                self.var_teacher.get(), 
                                                                                                                self.var_rad1.get() #photo sample variable 
                                                                                                                ))

                conn.commit()
                self.fetch_data() #fetch data into the student table frame from workbench after inserting to the workbench, live change
                conn.close()
                messagebox.showinfo("Success", "Student details has been added succesfully", parent = self.root)
            except Exception as es: #if duplicate entry
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root ) #shows error of the primary key
# ===============fetch data from mysql workbench to the table in student_details===========================
    
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "cyberhunter", database = "face_recognition_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()        
        self.student_table.delete(*self.student_table.get_children())
        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data: #data will be a list of tuples, where each tuple represents a record (row) in the table.
                self.student_table.insert("", END, values= i)
            #conn.commit() #committing after one row in inserted, commit to ensure addition
        # else:
        #         self.student_table.insert("", END, values= "")
        #         conn.commit()

        conn.close()
             

# ===============get_cursor================== # to show the data in the field when clicked on the data on the table to update
    def get_cursor(self,event = ""):
        cursor_focus = self.student_table.focus() #shows the foucused data or where the cursor is on the student table(on which row)
        content = self.student_table.item(cursor_focus) #clicked cursor row(item or data)
        data = content["values"]

        self.var_dep.set(data[0])         
        self.var_course.set(data[1])         
        self.var_year.set(data[2])         
        self.var_semester.set(data[3])         
        self.var_id.set(data[4])         
        self.var_name.set(data[5])         
        self.var_div.set(data[6])         
        self.var_roll.set(data[7])         
        self.var_gender.set(data[8])         
        self.var_dob.set(data[9])         
        self.var_email.set(data[10])         
        self.var_phone.set(data[11])         
        self.var_address.set(data[12])         
        self.var_teacher.set(data[13])   
        self.var_rad1.set(data[14])           

# ==============update_data==================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "": #get helps to get the data from the entry field or combo text variables
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update the student details")
                if update > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "cyberhunter", database = "face_recognition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep = %s, course = %s, year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_id = %s",(
                                                                                                                                                                                                                                                                    self.var_dep.get(),         
                                                                                                                                                                                                                                                                    self.var_course.get(),         
                                                                                                                                                                                                                                                                    self.var_year.get(),         
                                                                                                                                                                                                                                                                    self.var_semester.get(),         
                                                                                                                                                                                                                                                                    self.var_name.get(),         
                                                                                                                                                                                                                                                                    self.var_div.get(),         
                                                                                                                                                                                                                                                                    self.var_roll.get(),         
                                                                                                                                                                                                                                                                    self.var_gender.get(),         
                                                                                                                                                                                                                                                                    self.var_dob.get(),         
                                                                                                                                                                                                                                                                    self.var_email.get(),         
                                                                                                                                                                                                                                                                    self.var_phone.get(),         
                                                                                                                                                                                                                                                                    self.var_address.get(),         
                                                                                                                                                                                                                                                                    self.var_teacher.get(), 
                                                                                                                                                                                                                                                                    self.var_rad1.get(), #photo sample variable 
                                                                                                                                                                                                                                                                    self.var_id.get()        
                                                                                                                                                                                                                                                                    ))
                    
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details has been updated succesfully", parent = self.root)
                conn.commit()
                self.fetch_data() #whenever fetch is called it will insert all date from start to end in the student table from tha database
                conn.close()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root ) #shows error of the primary key

    # ==================delete the student details =================
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error","Student Id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Details Delete Page", "Do you want to want to delete this student details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "cyberhunter", database = "face_recognition_system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id = %s"
                    value = (self.var_id.get(),) #, to make it tuple cuz single value in it
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete", "Student details has been deleted succesfully", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root ) #shows error of the primary key

    def reset_data(self):
        self.var_dep.set("Select department")         
        self.var_course.set("Select course")         
        self.var_year.set("Select year")         
        self.var_semester.set("Select semester")         
        self.var_id.set("")         
        self.var_name.set("")         
        self.var_div.set("Select Division")         
        self.var_roll.set("")         
        self.var_gender.set("Select Gender")         
        self.var_dob.set("")         
        self.var_email.set("")         
        self.var_phone.set("")         
        self.var_address.set("")         
        self.var_teacher.set("")   
        self.var_rad1.set("") 


    # ==================Generate data set or take sample============
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "": #get helps to get the data from the entry field or combo text variables
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else: 
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "cyberhunter", database = "face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0 
                for x in my_result:
                    id+= 1         #giving a specific id to each record/row
                my_cursor.execute("update student set Dep = %s, course = %s, year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_id = %s",(
                                                                                                                                                                                                                                                                    self.var_dep.get(),         
                                                                                                                                                                                                                                                                    self.var_course.get(),         
                                                                                                                                                                                                                                                                    self.var_year.get(),         
                                                                                                                                                                                                                                                                    self.var_semester.get(),         
                                                                                                                                                                                                                                                                    self.var_name.get(),         
                                                                                                                                                                                                                                                                    self.var_div.get(),         
                                                                                                                                                                                                                                                                    self.var_roll.get(),         
                                                                                                                                                                                                                                                                    self.var_gender.get(),         
                                                                                                                                                                                                                                                                    self.var_dob.get(),         
                                                                                                                                                                                                                                                                    self.var_email.get(),         
                                                                                                                                                                                                                                                                    self.var_phone.get(),         
                                                                                                                                                                                                                                                                    self.var_address.get(),         
                                                                                                                                                                                                                                                                    self.var_teacher.get(), 
                                                                                                                                                                                                                                                                    self.var_rad1.get(), #photo sample variable 
                                                                                                                                                                                                                                                                    self.var_id.get()==id+1
                                                                                                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data() #whenever fetch is called it will insert all date from start to end in the student table from tha database
                #self.reset_data()
                conn.close()

                # ==================loads predefined data on face frontals from open cv===========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                 
                def face_cropped(img): #cropping the image, make a rectangle and return the image
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #converting the image to grayscale
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour = 5

                    for (x,y,w,h) in faces:  #x,y and w - > width and h-> height of the images, x,y,w,h to make a rectangle on the face
                        face_cropped = img[y: y+h, x: x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0) #to open the camera
                img_id = 0
                while True: 
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame),(450,450)) #resize it 
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)   #then change to grayscale
                        file_name_path = f"data/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255)) #put formated text, font, color, thickness parameter on the face image
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100: # loop breaks when 100 sample are collected or when pressed enter
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully")

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root ) #shows error of the primary key


if __name__ == "__main__":
    root = Tk()  #create the main tinker window 
    obj = Student(root)
    root.mainloop() #Starts the tkinter event loop, which keeps the window open and responsive until you close it.