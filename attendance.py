from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from Face_recognizer import face_recognizer
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
data_lis = []           #global variable to strore data from csv
class attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Attendance Page")  #title of application
        #background_image
        img4 = Image.open(r"images\bgcolor.png")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1600,height=900)

        #title bar
        title_label = Label(bg_img,text="Attendance",font=("time new roman",22,"bold"),bg="#EB455F",fg="black")
        title_label.place(x=0,y=0,width=1600,height=30)

        #variables---
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_rollno = StringVar()
        self.var_attendance = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()

        #main_frame
        main_frame = Frame(bg_img,bd=3)         #setting farme over background image
        main_frame.place(x=15,y=40,width=1505,height=740)

        #left frame -----------------------------------------
        left_frame = LabelFrame(main_frame,bg="#EAFDFC",bd=3,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=700,height=720)

        img_left = Image.open(r"images\books.png")
        img_left = img_left.resize((800,150),Image.ANTIALIAS) #antialias to reduce jaggedness to make it smoother 
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        flabel = Label(left_frame,image=self.photoimg_left)
        flabel.place(x=5,y=0,width=685,height=150)
        #inner frame
        left_frame2 = Frame(left_frame,bg="#EAFDFC",bd=3,relief=RIDGE)
        left_frame2.place(x=10,y=170,width=675,height=520)

        #entries
        studentid_label = Label(left_frame2,text='Student ID:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        studentid_label.grid(row=0,column=0,padx=20,pady=2,sticky=W)  #grid location 
        studentid_entry = ttk.Entry(left_frame2,textvariable=self.var_student_id,width=18,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=3,pady=10)

        roll_no_label = Label(left_frame2,text='Roll Number:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        roll_no_label.grid(row=0,column=2,padx=20,pady=2,sticky=W)  #grid location 
        roll_no_entry = ttk.Entry(left_frame2,textvariable=self.var_rollno,width=18,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=3,pady=10)

        student_name_label = Label(left_frame2,text='Student Name:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        student_name_label.grid(row=1,column=0,padx=20,pady=2,sticky=W)  #grid location 
        student_name_entry = ttk.Entry(left_frame2,textvariable=self.var_name,width=18,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=3,pady=10)

        date_label = Label(left_frame2,text='Date:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        date_label.grid(row=1,column=2,padx=20,pady=2,sticky=W)  #grid location 
        date_entry = ttk.Entry(left_frame2,textvariable=self.var_date,width=18,font=("times new roman",12,"bold"))
        date_entry.grid(row=1,column=3,padx=3,pady=30)

        department_label = Label(left_frame2,text='Department:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        department_label.grid(row=2,column=0,padx=20,sticky=W)  #grid location 
        department_combo = ttk.Combobox(left_frame2,textvariable=self.var_department,font=("times new roman",12,"bold"),width=18,state="readonly")  #read only to not be able to edit content
        department_combo["values"] = ("Select Department","CSE","IT","Electronics","Mechanical","Civil","ECS","ETC")
        department_combo.current(0)     #setting default value in combobox
        department_combo.grid(row=2,column=1,padx=3)    #padx - padding along x axis

        time_label = Label(left_frame2,text='Time:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        time_label.grid(row=2,column=2,padx=20,pady=2,sticky=W)  #grid location 
        time_entry = ttk.Entry(left_frame2,textvariable=self.var_time,width=18,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=3,padx=3,pady=20)

        attendance_label = Label(left_frame2,text='Attendance:',font=("times new roman",13,"bold"),bg="#EAFDFC")
        attendance_label.grid(row=3,column=0,padx=20,pady=2,sticky=W)  #grid location 
        attendance_entry = ttk.Combobox(left_frame2,textvariable=self.var_attendance,width=18,font=("times new roman",12,"bold"),state="readonly")
        attendance_entry["values"] = ("Select","Present","Absent")
        attendance_entry.current(0)
        attendance_entry.grid(row=3,column=1,padx=3,pady=20)

        #button frame
        button_frame = Frame(left_frame2,bd=2,relief=RIDGE,bg="#EAFDFC")
        button_frame.place(x=10,y=300,width=650,height=205)

        #buttons
        import_button = Button(button_frame,command=self.import_csv,width=25,height=2,text="Import csv",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        import_button.grid(row=0,column=0,pady=20,padx=45)

        export_button = Button(button_frame,command=self.export_csv,width=25,height=2,text="Export csv",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        export_button.grid(row=0,column=1,pady=20,padx=45)

        reset_button = Button(button_frame,command=self.reset_data,width=25,height=2,text="Reset",font=("times new roman",12,"bold"),bg="green",fg="yellow")
        reset_button.grid(row=1,column=0,pady=20,padx=45)


        #right frame ------------------------------------
        right_frame = LabelFrame(main_frame,bg="#EAFDFC",bd=3,relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"))
        right_frame.place(x=720,y=10,width=770,height=720)

        img_right = Image.open(r"images\books.png")
        img_right = img_left.resize((800,150),Image.ANTIALIAS) #antialias to reduce jaggedness to make it smoother 
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        flabel = Label(right_frame,image=self.photoimg_right)
        flabel.place(x=7,y=0,width=750,height=150)

        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="#EAFDFC")
        table_frame.place(x=5,y=160,width=755,height=530)

        #scroll bar & table

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame,columns=("Student ID","Name","Roll No","Department","Time","Date","Attendance"),
                                                               xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("Student ID",text="Student ID")
        self.attendance_table.heading("Roll No",text="Roll No")
        self.attendance_table.heading("Name",text="Name")
        self.attendance_table.heading("Department",text="Department")
        self.attendance_table.heading("Time",text="Time")
        self.attendance_table.heading("Date",text="Date")
        self.attendance_table.heading("Attendance",text="Attendance")
        self.attendance_table['show'] = "headings"
        self.attendance_table.column("Student ID",width=100)
        self.attendance_table.column("Roll No",width=100)
        self.attendance_table.column("Name",width=100)
        self.attendance_table.column("Department",width=100)
        self.attendance_table.column("Time",width=100)
        self.attendance_table.column("Date",width=100)
        self.attendance_table.column("Attendance",width=100)
        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)  #adding get_cursor to fill fields with selected row
#--------import data from attendance.csv------
    def add_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
    #import data from attendance.csv
    def import_csv(self):
        global data_lis 
        data_lis.clear()    #clear previous data so as to avoid duplicates
        filee = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV"
                                           ,filetypes=(("CSV FILE","*csv"),("All File","*.*")),parent=self.root)
        with open(filee) as ff:
            csvread = csv.reader(ff,delimiter=",")
            for i in csvread:
                data_lis.append(i)
            self.add_data(data_lis)
    def get_cursor(self,event=""):
        cursor_focus = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_focus)
        data = content['values']
        self.var_student_id.set(data[0])
        self.var_name.set(data[1])
        self.var_rollno.set(data[2])
        self.var_department.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5])
        self.var_attendance.set(data[6])
    def export_csv(self):
        try:
            if len(data_lis) == 0:
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            filee = filedialog.asksaveasfilename(initialdir=os.getcwd()
                                               ,title="Open CSV",filetypes=(("CSV FILE","*csv"),("All File","*.*")),parent=self.root)
            with open(filee,mode="w",newline="") as ff:
                exp = csv.writer(ff,delimiter=",")
                for i in data_lis:
                    exp.writerow(i)
                messagebox.showinfo("Exported","Data exported to "+os.path.basename(filee),parent=self.root)
        except Exception as er:
            messagebox.showerror("Failed",f"Failed dur to {er}",parent=self.root)
    def reset_data(self):
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_rollno.set("")
        self.var_department.set("Select Department")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

if __name__ == "main":
    root = Tk()
    obj = attendance(root)
    root.mainloop()