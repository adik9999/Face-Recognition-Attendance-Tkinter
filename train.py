from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import numpy as np
import cv2
from tkinter import messagebox
# print("HELLO")
class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")  #setting main window size and coordinates
        self.root.title("Training Window")  #title of application
        #adding images
        # img1 = Image.open(r"images\network3.png")
        # img1 = img1.resize((800,150),Image.ANTIALIAS) #antialias to reduce jaggedness to make it smoother 
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # flabel = Label(self.root,image=self.photoimg1)
        # flabel.place(x=0,y=30,width=800,height=150)

        # img2 = Image.open(r"images\network2.png")
        # img2 = img2.resize((800,150),Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        # flabel = Label(self.root,image=self.photoimg2)
        # flabel.place(x=800,y=30,width=800,height=150)
        
        #background_image
        img4 = Image.open(r"images\bgg.jpg")
        img4 = img4.resize((1600,900),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1600,height=900)

        #title bar
        title_label = Label(self.root,text="TRAIN OVER DATA",font=("time new roman",25,"bold"),bg="red",fg="white")
        title_label.place(x=0,y=0,width=1600,height=30)

        # pb1 = ttk.Progressbar(bg_img, orient=HORIZONTAL, length=300, mode='indeterminate')
        # pb1.place(x=500,y=300)
        #train button
        button1 = Button(bg_img,command=self.training,text="TRAIN",bg="green",fg="white",cursor="hand2",font=("time new roman",20,"bold"))
        button1.place(x=650,y=190,width=300,height=80)

        title_ = Label(self.root,text="Press button to train LBPH(Local Binary Pattern Histogram) Model",
                       font=("time new roman",25,"bold"),bg="black",fg="white")
        title_.place(x=0,y=130,width=1600,height=40)
    def training(self):
        img_path = ("data_img")
        path = [os.path.join(img_path,file) for file in os.listdir(img_path)]
        faces=[]
        ids=[]
        for image in path:  
            img = Image.open(image).convert('L')    #convert to gray scale after opening
            img_np = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training",img_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        ##LOCAL BINARY PATTERN HISTOGRAM (LBPH) Classifier Training
        lbph = cv2.face.LBPHFaceRecognizer_create()
        lbph.train(faces,ids)
        lbph.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Sucess","Training images completed")
if __name__ == "main":
    root = Tk()
    obj = Train(root)
    # obj.pack(fill=BOTH, expand=True)
    root.mainloop()