from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from sql_credentials import SQL_HOST,SQL_PASS,SQL_USER,SQL_DB1,SQL_DB2
class Registration:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Registration Page")  #title of application
        #variables-----
        self.var_fullname = StringVar()
        self.var_username = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_security_choice = StringVar()
        self.var_security = StringVar()
        img4 = Image.open(r"images\blurred.png")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1600,height=900)

        main_frame = Frame(self.root,bg="#F6F6F6",width=1300,height=400)
        main_frame.place(x=400,y=20,width=700,height=750)

        sign_label = Label(main_frame,text="Sign Up",width=200,height=40,font=("times new roman",23,"bold"),fg="black",bg="#F6F6F6")
        sign_label.place(x=5,y=10,width=200,height=40)

        scnd_label = Label(main_frame,text="It`s quick and easy.",width=150,height=40,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        scnd_label.place(x=35,y=55,width=200,height=40)

        sub_frame = Frame(main_frame,bg="#F6F6F6")
        sub_frame.place(x=10,y=105,width=680,height=636)

        fullname_label = Label(sub_frame,text="Full Name",width=10,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        fullname_label.grid(row=0,column=0,pady=10,padx=20,sticky="W")

        fullname_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_fullname,font=("times new roman",17,"bold"))
        fullname_entry.grid(row=1,column=0,pady=10,padx=20,sticky="W")

        
        username_label = Label(sub_frame,text="Username",width=10,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        username_label.grid(row=0,column=1,pady=10,padx=40,sticky="W")

        username_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_username,font=("times new roman",17,"bold"))
        username_entry.grid(row=1,column=1,pady=10,padx=40,sticky="W")

        email_label = Label(sub_frame,text="Email",width=6,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        email_label.grid(row=2,column=0,pady=10,padx=20,sticky="W")

        email_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_email,font=("times new roman",17,"bold"))
        email_entry.grid(row=3,column=0,pady=10,padx=20,sticky="W")

        password_label = Label(sub_frame,text="Password",width=10,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        password_label.grid(row=2,column=1,pady=10,padx=40,sticky="W")

        password_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_password,font=("times new roman",17,"bold"))
        password_entry.grid(row=3,column=1,pady=10,padx=40,sticky="W")

        dob_label = Label(sub_frame,text="Date Of Birth",width=10,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        dob_label.grid(row=4,column=0,pady=10,padx=20,sticky="W")

        dob_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_dob,font=("times new roman",17,"bold"))
        dob_entry.grid(row=5,column=0,pady=10,padx=20,sticky="W")

        gender_label = Label(sub_frame,text="Gender",width=7,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        gender_label.grid(row=4,column=1,pady=10,padx=45,sticky="W")

        gender_entry = ttk.Combobox(sub_frame,width=19,textvariable=self.var_gender,font=("times new roman",15,"bold"),state='readonly')
        gender_entry['values'] = ("Select Gender","Male","Female","Other")
        gender_entry.current(0)
        gender_entry.grid(row=5,column=1,pady=10,padx=40,sticky="W")

        security_label = Label(sub_frame,text="Security Question",width=12,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        security_label.grid(row=6,column=0,pady=10,padx=25,sticky="W")

        security_entry = ttk.Combobox(sub_frame,width=22,textvariable=self.var_security_choice,font=("times new roman",15,"bold"),state='readonly')
        security_entry['values'] = ("Select Question","Name of you favourite TV show","Favourite food","Nickname")
        security_entry.current(0)
        security_entry.grid(row=7,column=0,pady=10,padx=20,sticky="W")

        security_ans = ttk.Entry(sub_frame,textvariable=self.var_security,width=23,font=("times new roman",15,"bold"))
        security_ans.grid(row=7,column=1,pady=10,padx=45,sticky="W")

        signup_button = Button(sub_frame,command=self.add_data,activeforeground="#00B8A9",activebackground="#00B8A9",text="Sign Up",font=("times new roman",17,"bold"),bd=3,relief=RIDGE,fg="white",bg="#00B8A9")
        signup_button.place(x=195,y=450,width=300,height=47)
    def add_data(self):
        if self.var_username.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error","Username and password need to filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username=SQL_USER,password=SQL_PASS,database=SQL_DB2)
                cursor = conn.cursor()  #cursor to execute sql commands
                cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_fullname.get(),self.var_username.get(),
                                                                                       self.var_email.get(),self.var_password.get(),
                                                                                       self.var_dob.get(),self.var_gender.get(),
                                                                                       self.var_security_choice.get(),self.var_security.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","User Registered Succesfully",parent=self.root)
                self.root.destroy()
            except Exception as er:
                messagebox.showerror("Error",f"Failed due to: {str(er)}",parent=self.root)

if __name__ == "main":
    root = Tk()
    obj = Registration(root)
    root.mainloop()
