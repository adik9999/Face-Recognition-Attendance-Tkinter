from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from Face_recognizer import face_recognizer
from attendance import attendance
import os
# print("HELLO")
class face_recon:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Face Recognition Attendance")  #title of application
        #adding images
        
        #background_image
        img4 = Image.open(r"images\bgg.jpg")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1600,height=900)

        #title bar
        title_label = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("time new roman",30,"bold"),bg="#EB455F",fg="#FCFFE7")
        title_label.place(x=0,y=0,width=1600,height=50)

        #student database button
        img5 = Image.open(r"images\database.png")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,command=self.student_details,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_name = Button(bg_img,command=self.student_details,text="Student Details",font=("times new roman",14)
                         ,bg="black",fg="yellow",cursor="hand2")
        b1_name.place(x=200,y=325,width=220,height=20)

        #detect face button
        img6 = Image.open(r"images\detect.png")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,command=self.open_recognizer,image=self.photoimg6,cursor="hand2")
        b2.place(x=480,y=100,width=220,height=220)

        b2_name = Button(bg_img,command=self.open_recognizer,text="Detect Face",font=("times new roman",14),bg="black",fg="yellow",cursor="hand2")
        b2_name.place(x=480,y=325,width=220,height=20)

        #attendance button
        img7 = Image.open(r"images\attendance.png")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img,command=self.open_attendance,image=self.photoimg7,cursor="hand2")
        b3.place(x=760,y=100,width=220,height=220)

        b3_name = Button(bg_img,command=self.open_attendance,text="Attendance",font=("times new roman",14),bg="black",fg="yellow",cursor="hand2")
        b3_name.place(x=760,y=325,width=220,height=20)


        #train button
        img9 = Image.open(r"images\train.png")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img,command=self.open_train,image=self.photoimg9,cursor="hand2")
        b5.place(x=480,y=380,width=220,height=220)

        b5_name = Button(bg_img,command=self.open_train,text="Train",font=("times new roman",14),bg="black",fg="yellow",cursor="hand2")
        b5_name.place(x=480,y=605,width=220,height=20)
        
        #photos button
        img10 = Image.open(r"images\photos.png")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img,command=self.open_photos,image=self.photoimg10,cursor="hand2")
        b6.place(x=760,y=380,width=220,height=220)

        b6_name = Button(bg_img,command=self.open_photos,text="Photos",font=("times new roman",14),bg="black",fg="yellow",cursor="hand2")
        b6_name.place(x=760,y=605,width=220,height=20)

        #Exit button
        img12 = Image.open(r"images\exit.png")
        img12 = img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b8 = Button(bg_img,command=self.close_all,image=self.photoimg12,cursor="hand2")
        b8.place(x=1040,y=100,width=220,height=220)

        b8_name = Button(bg_img,command=self.close_all,text="Exit",font=("times new roman",14),bg="black",fg="yellow",cursor="hand2")
        b8_name.place(x=1040,y=325,width=220,height=20)

#button functions-----------
    def open_photos(self):  #open photos folder
        os.startfile("data_img")
    def student_details(self):      #open student details window
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    def open_train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    def open_recognizer(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recognizer(self.new_window)
    def open_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = attendance(self.new_window)
    def close_all(self):
            root.destroy()

# if __name__ == "main":
root = Tk()
obj = face_recon(root)
# obj.pack(fill=BOTH, expand=True)
root.mainloop()