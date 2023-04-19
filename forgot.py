from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from sql_credentials import SQL_HOST,SQL_PASS,SQL_USER,SQL_DB1,SQL_DB2
class Forgot:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Forgot Password Page")
        #--variables
        self.var_username = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_new_password1 = StringVar()
        self.var_new_password2 = StringVar()
        img4 = Image.open(r"images\blurred.png")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1600,height=900)

        main_frame = Frame(self.root,bg="#F6F6F6")
        main_frame.place(x=450,y=60,width=600,height=650)

        main_label = Label(main_frame,text="Enter Details",font=("times new roman",16,"bold"),fg="black",bg="white")
        main_label.place(x=240,y=10,width=150,height=40)

        sub_frame = Frame(main_frame,bg="#F6F6F6")
        sub_frame.place(x=15,y=50,width=570,height=585)

        username_label = Label(sub_frame,text="Enter Username",width=12,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        username_label.grid(row=0,column=0,pady=30,padx=35,sticky="W")

        username_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_username,font=("times new roman",17,"bold"))
        username_entry.grid(row=0,column=1,pady=30,padx=35,sticky="W")

        security_q_label = Label(sub_frame,text="Select Security Question",width=18,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        security_q_label.grid(row=1,column=0,pady=30,padx=35,sticky="W")

        security_q_entry = ttk.Combobox(sub_frame,width=19,textvariable=self.var_security_q
                                        ,font=("times new roman",14,"bold"),state='readonly')
        security_q_entry['values'] = ("Select Question","Name of you favourite TV show","Favourite food","Nickname")
        security_q_entry.current(0)
        security_q_entry.grid(row=1,column=1,pady=30,padx=35,sticky="W")

        security_a_label = Label(sub_frame,text="Security Answer",width=12,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        security_a_label.grid(row=2,column=0,pady=30,padx=35,sticky="W")

        security_a_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_security_a,font=("times new roman",17,"bold"))
        security_a_entry.grid(row=2,column=1,pady=30,padx=35,sticky="W")

        new_password1_label = Label(sub_frame,text="New Password",width=12,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        new_password1_label.grid(row=3,column=0,pady=30,padx=35,sticky="W")

        new_password1_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_new_password1,font=("times new roman",17,"bold"))
        new_password1_entry.grid(row=3,column=1,pady=30,padx=35,sticky="W")

        new_password2_label = Label(sub_frame,text="Repeat Password",width=12,font=("times new roman",15,"bold"),fg="black",bg="#F6F6F6")
        new_password2_label.grid(row=4,column=0,pady=30,padx=35,sticky="W")

        new_password2_entry = ttk.Entry(sub_frame,width=23,textvariable=self.var_new_password2,font=("times new roman",17,"bold"))
        new_password2_entry.grid(row=4,column=1,pady=30,padx=35,sticky="W")

        submit_button = Button(sub_frame,command=self.submit_press,activebackground="black",
                                 activeforeground="white",bd=0,text="Submit",
                                 font=("times new roman",15,"bold"),fg="white",bg="blue",relief=RIDGE)
        submit_button.place(x=245,y=465,width=135,height=48)
    def submit_press(self):
        # pass
        if self.var_username == "" or self.var_security_q == "" or self.var_security_a == "" or self.var_new_password1 == "" or self.var_new_password2 == "":
            messagebox.showerror("Error","All Fields must be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username=SQL_USER,password=SQL_PASS,database=SQL_DB2)
                cursor = conn.cursor()  #cursor to execute sql commands
                cursor.execute("select security_q from register where username=%s",(self.var_username.get(),))
                store_security_q = cursor.fetchone()
                cursor.execute("select security_a from register where username=%s",(self.var_username.get(),))
                store_security_a = cursor.fetchone()
                # messagebox.showinfo("S",f"{store_security_q[0]} {store_security_a[0]}",parent=self.root)
                if store_security_q[0] != self.var_security_q.get():
                    messagebox.showerror("Error","Wrong Security Question",parent=self.root)
                else:
                    if store_security_a[0] != self.var_security_a.get():
                        messagebox.showerror("E","Wrong Security Answer",parent=self.root)
                    else:
                        if self.var_new_password1.get() != self.var_new_password2.get():
                            messagebox.showerror("E","Passwords should match",parent=self.root)
                        else:
                            cursor.execute("update register set password=%s where username=%s",(self.var_new_password1.get(),
                                                                                                self.var_username.get()))
                            messagebox.showinfo("Success","Password Changed",parent=self.root)
                            self.root.destroy()
                conn.commit()
                conn.close()
            except Exception as er:
                messagebox.showerror("E",f"Failed due to: {str(er)}",parent=self.root)
if __name__ == "main":
    root = Tk()
    obj = Forgot(root)
    root.mainloop()