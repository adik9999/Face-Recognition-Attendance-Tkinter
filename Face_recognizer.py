from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
from sql_credentials import SQL_HOST,SQL_PASS,SQL_USER,SQL_DB1,SQL_DB2
class face_recognizer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Face Recognizer")  #title of application
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
        bg_img.place(x=0,y=180,width=1600,height=900)

        title = Label(self.root,text="Face Recognizer",font=("times new roman",25,"bold"),fg="black",bg="#EB455F")
        title.place(x=0,y=150,width=1600,height=40)

        #main frame
        main_frame = Frame(bg_img,bd=3,bg="#18122B")
        main_frame.place(x=15,y=15,width=1495,height=572)

        #left frame
        left_frame = Frame(main_frame,bg="#18122B",bd=3)
        left_frame.place(x=5,y=5,width=747,height=560)

        img5 = Image.open(f"images/face_recognizer.png")
        img5 = img5.resize((747,560),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        left_img = Label(left_frame,image=self.photoimg5)
        left_img.place(x=0,y=0,width=750,height=565)      

        #right frame
        right_frame = Frame(main_frame,bg="#18122B",bd=3)
        right_frame.place(x=762,y=5,width=720,height=560)

        right_title = Label(right_frame,text="Press Run to Start the Attendance System",font=("times new roman",30,"bold"),fg="white",bg="#18122B")
        right_title.place(x=0,y=150,width=720,height=45)

        button1 = Button(right_frame,command=self.recognizer,text="RUN",bg="green",fg="white",cursor="hand2",font=("time new roman",20,"bold"))
        button1.place(x=300,y=280,width=200,height=80)
#attendance------------
    def mark_attendance(self,id,name,roll,dept):
        with open("attendance.csv","r+",newline="\n") as f:
            mydata = f.readlines()
            lis = []
            for line in mydata:
                entry = line.split((","))
                lis.append(entry[0])
            if ((name not in lis) and (roll not in lis) and (dept not in lis) and (id not in lis)):
                now = datetime.now()
                dd = now.strftime("%d/%m/%Y")
                d_d = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{name},{roll},{dept},{d_d},{dd},Present")


#face recognizer---------
    def recognizer(self):
        def draw_border(img,classifier,scale_factor,min_n,Color,Text,clf):
            gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img,scale_factor,min_n)
            coor = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(host="localhost",username=SQL_USER,password=SQL_PASS,database=SQL_DB1)
                cursor = conn.cursor()  #cursor to execute sql commands
                
                #fetch data from mysql database using predicted id
                cursor.execute("select name from student where student_id = "+str(id))
                namee = cursor.fetchone()
                namee = "+".join(namee)

                cursor.execute("select student_id from student where student_id = "+str(id))
                idd = cursor.fetchone()
                idd = "+".join(idd)

                cursor.execute("select roll_no from student where student_id = "+str(id))
                roll_no = cursor.fetchone()
                roll_no = "+".join(roll_no)

                cursor.execute("select department from student where student_id = "+str(id))
                dept = cursor.fetchone()
                dept = "+".join(dept)

                if confidence > 77:
                    cv2.putText(img,f"ID: {idd}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
                    cv2.putText(img,f"Roll: {roll_no}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
                    cv2.putText(img,f"Name: {namee}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
                    cv2.putText(img,f"Department: {dept}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
                    self.mark_attendance(idd,namee,roll_no,dept)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)                
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)   
                coor = [x,y,w,h]
            return coor
        def recognize(img,clf,Cascade):
            coor = draw_border(img,Cascade,1.2,10,(255,255,255),"Face",clf)
            return img
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        try:

            video_capture = cv2.VideoCapture(0)
            while True:
                ret,img = video_capture.read()
                img = recognize(img,clf,face_cascade)
                cv2.imshow("Attendance System",img)
                if cv2.waitKey(1)==13:
                    break
            video_capture.release()
            cv2.destroyAllWindows()
        except Exception as es:
            messagebox.showerror("FAILURE",f"Failed due to {str(es)}")

                    

if __name__ == "main":
    root = Tk()
    obj = face_recognizer(root)
    root.mainloop()