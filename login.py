from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from registration import Registration
from forgot import Forgot
import subprocess
from sql_credentials import SQL_HOST,SQL_PASS,SQL_USER,SQL_DB1,SQL_DB2
# from main import face_recon
import mysql.connector
class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Login Page")  #title of application
        #variables-----
        self.var_username = StringVar()
        self.var_password = StringVar()
        
        #background_image
        img4 = Image.open(r"images\blurred.png")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1600,height=900)

        frame = Frame(self.root,bg="black")
        frame.place(x=600,y=180,width=380,height=500)

        img5 = Image.open(r"images\login_icon.png")
        img5 = img5.resize((100,100),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        icon_img = Label(self.root,bg="black",image=self.photoimg5)
        icon_img.place(x=745,y=190,width=100,height=100)

        #entries
        username_label = Label(frame,text="Username",font=("times new roman",17,"bold"),fg="white",bg="black")
        username_label.place(x=44,y=120,width=100)

        username_entry = ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",17,"bold"))
        username_entry.place(x=25,y=155,width=330,height=25)

        password_label = Label(frame,text="Password",font=("times new roman",17,"bold"),fg="white",bg="black")
        password_label.place(x=44,y=195,width=100)

        password_entry = ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",17,"bold"))
        password_entry.place(x=25,y=230,width=330,height=25)
        
        img6 = Image.open(r"images\admin.png")
        img6 = img6.resize((30,30),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        icon_img = Label(frame,bg="black",image=self.photoimg6)
        icon_img.place(x=8,y=118,width=30,height=30)
        
        img7 = Image.open(r"images\password.png")
        img7 = img7.resize((30,30),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        icon_img = Label(frame,bg="black",image=self.photoimg7)
        icon_img.place(x=8,y=193,width=30,height=30)

        login_button = Button(frame,command=self.open_login,activebackground="green",text="Login",font=("times new roman",17,"bold"),bd=3,relief=RIDGE,fg="white",bg="green")
        login_button.place(x=45,y=280,width=300,height=32)

        register_button = Button(frame,command=self.open_registration,activebackground="black",
                                 activeforeground="white",bd=0,text="Register",
                                 font=("times new roman",13,"bold"),fg="white",bg="black")
        register_button.place(x=25,y=345,width=80,height=32)

        forgot_button = Button(frame,command=self.open_forgot,activebackground="black",
                                 activeforeground="white",bd=0,text="Forgot Password",
                                 font=("times new roman",13,"bold"),fg="white",bg="black")
        forgot_button.place(x=25,y=375,width=150,height=32)
    def open_login(self):
        try:
            conn = mysql.connector.connect(host="localhost",username=SQL_USER,password=SQL_PASS,database=SQL_DB2)
            cursor = conn.cursor(buffered=True)  #cursor to execute sql commands
            cursor.execute("select password from register where username=%s",(self.var_username.get(),))
            store = cursor.fetchone()
            conn.commit()
            conn.close()
            # messagebox.showinfo("E",f"{store}",parent=self.root)
            # print(store[0])
            if store[0] == self.var_password.get():
                subprocess.call(" python main.py 1", shell=True)
            else:
                messagebox.showinfo("FAIL","WRONG PASSWORD",parent=self.root)
        except Exception as er:
            messagebox.showerror("ERROR",f"Failed due to : {str(er)}",parent=self.root)
    # def openn(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = face_recon(self.new_window)
    def open_registration(self):
        self.new_window = Toplevel(self.root)
        self.app = Registration(self.new_window)
    def open_forgot(self):
        self.new_window = Toplevel(self.root)
        self.app = Forgot(self.new_window)
# if __name__ == "main":
root = Tk()
obj = Login(root)
root.mainloop()