from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from sql_credentials import SQL_HOST,SQL_PASS,SQL_USER,SQL_DB1,SQL_DB2
class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0") 
        self.root.title("Student Details")

        #variables---
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_rollno = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_mentor = StringVar()

        #adding images
        img1 = Image.open(r"images\network3.png")
        img1 = img1.resize((800,150),Image.ANTIALIAS) #antialias to reduce jaggedness to make it smoother 
        self.photoimg1 = ImageTk.PhotoImage(img1)
        flabel = Label(self.root,image=self.photoimg1)
        flabel.place(x=0,y=0,width=800,height=150)

        img2 = Image.open(r"images\network2.png")
        img2 = img2.resize((800,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        flabel = Label(self.root,image=self.photoimg2)
        flabel.place(x=800,y=0,width=800,height=150)
        
        #background_image
        img4 = Image.open(r"images\bgcolor.png")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1600,height=900)

        #title bar
        title_label = Label(bg_img,text="Student Management",font=("time new roman",22,"bold"),bg="#EB455F",fg="black")
        title_label.place(x=0,y=0,width=1600,height=30)

        #main_frame
        main_frame = Frame(bg_img,bd=3)         #setting farme over background image
        main_frame.place(x=15,y=40,width=1505,height=590)

        #left frame -----------------------------------------
        left_frame = LabelFrame(main_frame,bg="#EAFDFC",bd=3,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=800,height=570)

        img_left = Image.open(r"images\books.png")
        img_left = img_left.resize((800,150),Image.ANTIALIAS) #antialias to reduce jaggedness to make it smoother 
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        flabel = Label(left_frame,image=self.photoimg_left)
        flabel.place(x=5,y=0,width=785,height=150)

        #course frame
        course_frame = LabelFrame(left_frame,bg="#EAFDFC",bd=3,relief=RIDGE,text="Course Details",font=("times new roman",12,"bold"))
        course_frame.place(x=10,y=150,width=775,height=110)

        #department options
        department_label = Label(course_frame,text='Department:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        department_label.grid(row=0,column=0,padx=45,sticky=W)  #grid location 
        department_combo = ttk.Combobox(course_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),width=18,state="readonly")  #read only to not be able to edit content
        department_combo["values"] = ("Select Department","CSE","IT","Electronics","Mechanical","Civil","ECS","ETC")
        department_combo.current(0)     #setting default value in combobox
        department_combo.grid(row=0,column=1,padx=3)    #padx - padding along x axis

        #course options
        course_label = Label(course_frame,text='Course:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        course_label.grid(row=0,column=2,padx=45,sticky=W)  #grid location 
        course_combo = ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=18,state="readonly")  #read only to not be able to edit content
        course_combo["values"] = ("Select Course","B.Tech","M.Tech","Data Analytics","Machine Design")
        course_combo.current(0)     #setting default value in combobox
        course_combo.grid(row=0,column=3,padx=2)    #padx - padding along x axis

        #year options
        year_label = Label(course_frame,text='Year:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        year_label.grid(row=1,column=0,padx=45,pady=15,sticky=W)  #grid location 
        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=18,state="readonly")  #read only to not be able to edit content
        year_combo["values"] = ("Select Year","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)     #setting default value in combobox
        year_combo.grid(row=1,column=1,padx=3)    #padx - padding along x axis

        #semester options
        semester_label = Label(course_frame,text='Semester:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        semester_label.grid(row=1,column=2,padx=45,pady=15,sticky=W)  #grid location 
        semester_combo = ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=18,state="readonly")  #read only to not be able to edit content
        semester_combo["values"] = ("Select Semester","Semester - I","Semester - II")
        semester_combo.current(0)     #setting default value in combobox
        semester_combo.grid(row=1,column=3,padx=3)    #padx - padding along x axis

        #class information frame
        class_info_frame = LabelFrame(left_frame,bg="#EAFDFC",bd=3,relief=RIDGE,text="Class Information",font=("times new roman",12,"bold"))
        class_info_frame.place(x=10,y=260,width=775,height=280)

        #student ID
        studentid_label = Label(class_info_frame,text='Student ID:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        studentid_label.grid(row=0,column=0,padx=40,pady=2,sticky=W)  #grid location 
        studentid_entry = ttk.Entry(class_info_frame,textvariable=self.var_student_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=3)

        #student Name
        student_name_label = Label(class_info_frame,text='Student Name:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        student_name_label.grid(row=0,column=2,padx=40,pady=2,sticky=W)  #grid location 
        student_name_entry = ttk.Entry(class_info_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=3)

        #Section Number
        section_label = Label(class_info_frame,text='Section:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        section_label.grid(row=1,column=0,padx=40,pady=2,sticky=W)  #grid location 
        section_entry = ttk.Entry(class_info_frame,textvariable=self.var_section,width=20,font=("times new roman",12,"bold"))
        section_entry.grid(row=1,column=1,padx=3)

        #Rolll Number
        roll_num_label = Label(class_info_frame,text='Roll No:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        roll_num_label.grid(row=1,column=2,padx=40,pady=2,sticky=W)  #grid location 
        roll_num_entry = ttk.Entry(class_info_frame,textvariable=self.var_rollno,width=20,font=("times new roman",12,"bold"))
        roll_num_entry.grid(row=1,column=3,padx=3)

        #Date Of Birth
        dob_label = Label(class_info_frame,text='DOB:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        dob_label.grid(row=2,column=0,padx=40,pady=2,sticky=W)  #grid location 
        dob_entry = ttk.Entry(class_info_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=3)

        #Gender
        gender_label = Label(class_info_frame,text='Gender:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        gender_label.grid(row=2,column=2,padx=40,pady=2,sticky=W)  #grid location 
        gender_entry = ttk.Combobox(class_info_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_entry["values"] = ("Select Gender","Male","Female","Other")
        gender_entry.current(0)
        gender_entry.grid(row=2,column=3,padx=3)

        #Email
        email_label = Label(class_info_frame,text='Email:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        email_label.grid(row=3,column=0,padx=40,pady=2,sticky=W)  #grid location 
        email_entry = ttk.Entry(class_info_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=3)

        #Phone Number
        phone_num_label = Label(class_info_frame,text='Phone No:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        phone_num_label.grid(row=3,column=2,padx=40,pady=2,sticky=W)  #grid location 
        phone_num_entry = ttk.Entry(class_info_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_num_entry.grid(row=3,column=3,padx=3)

        #Address
        address_label = Label(class_info_frame,text='Address:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        address_label.grid(row=4,column=0,padx=40,pady=2,sticky=W)  #grid location 
        address_entry = ttk.Entry(class_info_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=3)

        #Mentor Name
        mentor_label = Label(class_info_frame,text='Mentor Name:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        mentor_label.grid(row=4,column=2,padx=40,pady=2,sticky=W)  #grid location 
        mentor_entry = ttk.Entry(class_info_frame,textvariable=self.var_mentor,width=20,font=("times new roman",12,"bold"))
        mentor_entry.grid(row=4,column=3,padx=3)

        #radio button style
        s = ttk.Style()
        s.configure('Wild.TRadiobutton',background='#EAFDFC',foreground='black',font = ("times new roman", 12, "bold"))   

        #radio buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(class_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes", style = 'Wild.TRadiobutton')
        radio1.grid(row=5,column=0,padx=15,pady=2)

        radio2 = ttk.Radiobutton(class_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No", style = 'Wild.TRadiobutton')
        radio2.grid(row=5,column=1,padx=15,pady=2)

        #button frame
        button_frame = Frame(class_info_frame,bd=2,relief=RIDGE,bg="#EAFDFC")
        button_frame.place(x=10,y=170,width=750,height=85)

        #buttons
        save_button = Button(button_frame,command=self.add_data,width=15,text="Save",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        save_button.grid(row=0,column=0,pady=5,padx=20)

        update_button = Button(button_frame,command=self.update_data,width=15,text="Update",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        update_button.grid(row=0,column=1,pady=5,padx=20)

        delete_button = Button(button_frame,command=self.delete_data,width=15,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        delete_button.grid(row=0,column=2,pady=5,padx=20)

        reset_button = Button(button_frame,command=self.reset_data,width=15,text="Reset",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        reset_button.grid(row=0,column=3,pady=5,padx=20)

        take_photo_button = Button(button_frame,command=self.generate_data,width=15,text="Take Photo",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        take_photo_button.grid(row=1,column=0,pady=5,padx=20)

        update_photo_button = Button(button_frame,width=15,text="Update Photo",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        update_photo_button.grid(row=1,column=1,pady=5,padx=20)

        #right frame ------------------------------------
        right_frame = LabelFrame(main_frame,bg="#EAFDFC",bd=3,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=820,y=10,width=670,height=570)

        img_right = Image.open(r"images\books.png")
        img_right = img_left.resize((800,150),Image.ANTIALIAS) #antialias to reduce jaggedness to make it smoother 
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        flabel = Label(right_frame,image=self.photoimg_right)
        flabel.place(x=7,y=0,width=650,height=150)

        #TABLE FRAME-----

        table_frame = Frame(right_frame,bg="#EAFDFC",bd=3,relief=RIDGE)
        table_frame.place(x=10,y=150,width=650,height=385)

        #scrollbar for table

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Student ID",
                                                               "Name","Section","Roll No","DOB","Gender","Email",
                                                               "Phone No","Address","Mentor Name"),
                                                               xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student ID",text="Student ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Mentor Name",text="Mentor Name")
        self.student_table["show"] = "headings"
        
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Mentor Name",width=100)
    
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)  #adding get_cursor to fill fields with selected row
        self.fetch_data()   #fetch and add data to tree view
    #function add data to MySql
    def add_data(self):
        if self.var_email.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error","All Fields need to be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host=SQL_HOST,username=SQL_USER,password=SQL_PASS,database=SQL_DB1)
                cursor = conn.cursor()  #cursor to execute sql commands
                cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.var_department.get(),self.var_course.get(),self.var_year.get(),
                                self.var_semester.get(),self.var_student_id.get(),self.var_name.get(),
                                self.var_section.get(),self.var_rollno.get(),self.var_dob.get(),
                                self.var_gender.get(),self.var_email.get(),self.var_phone.get(),
                                self.var_address.get(),self.var_mentor.get(),self.var_radio1.get())) #sql insert command

                conn.commit()
                self.fetch_data()       #calling fetch function so as to update on the fly
                conn.close()
                # messagebox.showinfo("A",""+str(self.var_radio1.get()),parent=self.root)
                if str(self.var_radio1.get()) == "Yes":
                    self.generate_data()
                messagebox.showinfo("SUCESS","Student Details Added",parent=self.root)
            except Exception as er:
                messagebox.showerror("Error",f"Failed due to: {str(er)}",parent=self.root)

#fetch data into tree table----
    def fetch_data(self):
        conn = mysql.connector.connect(host=SQL_HOST,username=SQL_USER,password=SQL_PASS,database=SQL_DB1)
        cursor = conn.cursor()  #cursor to execute sql commands       
        cursor.execute("select * from student")
        data_rcv = cursor.fetchall()
        if len(data_rcv) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for dat in data_rcv:
                self.student_table.insert("",END,values=dat)
            conn.commit()
        conn.close()
#get data from tree into fields
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']
        self.var_department.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_name.set(data[5])
        self.var_section.set(data[6])
        self.var_rollno.set(data[7])
        self.var_dob.set(data[8])
        self.var_gender.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_mentor.set(data[13])
        self.var_radio1.set(data[14])

#update data into tree
    def update_data(self):
        if self.var_email.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error","All Fields need to be filled",parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update the details",parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host=SQL_HOST,username=SQL_USER,password=SQL_PASS,database=SQL_DB1)
                    cursor = conn.cursor()  #cursor to execute sql commands   
                    cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,section=%s,\
                                   roll_no=%s,dob=%s,gender=%s,email=%s,phone_no=%s,address=%s,mentor=%s,photo_sample=%s \
                                   where student_id=%s",(self.var_department.get(),self.var_course.get(),self.var_year.get(),
                                self.var_semester.get(),self.var_name.get(),
                                self.var_section.get(),self.var_rollno.get(),self.var_dob.get(),
                                self.var_gender.get(),self.var_email.get(),self.var_phone.get(),
                                self.var_address.get(),self.var_mentor.get(),self.var_radio1.get(),self.var_student_id.get()))                   
                else:
                    if update == 0:
                        return
                if str(self.var_radio1.get()) == "Yes":
                    self.generate_data()
                messagebox.showinfo("Success","Details Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as er:
                messagebox.showerror("Error",f"Error: {str(er)}",parent=self.root)
#delete data from tree

    def delete_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror("Error",f"Student ID required to delete row",parent=self.root)
        else:
            try:
                dell = messagebox.askyesno("Delete Data","Do you want to delete",parent=self.root)
                if dell > 0:
                    conn = mysql.connector.connect(host=SQL_HOST,username=SQL_USER,password=SQL_PASS,database=SQL_DB1)
                    cursor = conn.cursor()  #cursor to execute sql commands   
                    cursor.execute("delete from student where student_id=%s",(self.var_student_id.get(),))
                else:
                    if dell == 0:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delted","Data Sucessfully Deleted",parent=self.root)
            except Exception as er:
                messagebox.showerror("Error",f"Error: {str(er)}",parent=self.root)    
#reset data fields
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_section.set("")
        self.var_rollno.set("")
        self.var_dob.set("")
        self.var_gender.set("Select Gender")               
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_mentor.set("")
        self.var_radio1.set("")

#generate photos 
    def generate_data(self):
        if self.var_email.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error","All Fields need to be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host=SQL_HOST,username=SQL_USER,password=SQL_PASS,database=SQL_DB1)
                cursor = conn.cursor()  #cursor to execute sql commands 
                cursor.execute("select * from student")
                result = cursor.fetchall()
                id = 0
                for x in result:
                    id += 1;          
                cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,section=%s,\
                                roll_no=%s,dob=%s,gender=%s,email=%s,phone_no=%s,address=%s,mentor=%s,photo_sample=%s \
                                where student_id=%s",(self.var_department.get(),self.var_course.get(),self.var_year.get(),
                            self.var_semester.get(),self.var_name.get(),
                            self.var_section.get(),self.var_rollno.get(),self.var_dob.get(),
                            self.var_gender.get(),self.var_email.get(),self.var_phone.get(),
                            self.var_address.get(),self.var_mentor.get(),self.var_radio1.get(),self.var_student_id.get() == id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()    
                #load data
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropper(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)    #scaling factor 1.3 & #min neighbors 5
                    for (x,y,w,h) in faces:
                        face_cropper_ = img[y:y+h,x:x+w]
                        return face_cropper_
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,img_frame = cap.read()
                    if face_cropper(img_frame) is not None:
                        img_id = img_id + 1
                        face_ = cv2.resize(face_cropper(img_frame),(450,450))
                        face_ = cv2.cvtColor(face_,cv2.COLOR_BGR2GRAY)
                        file_path = "data_img/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face_)
                        cv2.putText(face_,str(img_id),(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
                        cv2.imshow("Cropped Image",face_)
                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Sucess","100 photo samples captured")
            except Exception as er:
                messagebox.showerror("Error",f"Error: {str(er)}",parent=self.root)   
#main function
if __name__ == "main":
    root = Tk()
    obj = Student(root)
    root.mainloop()