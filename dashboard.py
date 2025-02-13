from tkinter import *
from app import application, main
#from save1 import view,main3
import mysql.connector as mysql
from tkinter import ttk
from PIL import Image, ImageTk
import time
class dashboard(application):
    def __init__(self, m2):
        self.m2 = m2
        self.m2.geometry("250x200+1150+300")
        self.m2.config(bg='blue')
        self.b1 = Button(self.m2, text="Register", activebackground="blue",
                         width=10, bg="#93ff93", command=self.register)
        self.b1.place(x=80, y=20)
        self.b1 = Button(self.m2, text="View", activebackground="blue",
                         width=10, bg="#93ff93", command=self.view)
        self.b1.place(x=80, y=50)
        self.b1 = Button(self.m2, text="Print",
                         activebackground="blue", width=10, bg="#93ff93",command=self.save)
        self.b1.place(x=80, y=80)
        self.b1 = Button(self.m2, text="Edit", activebackground="blue",
                         width=10, bg="#93ff93", command=self.edit)
        self.b1.place(x=80, y=110)
    def register(self):
        main()
    def view(self):
        self.r = 1
        root = Tk()
        t = Table(root)
        root.mainloop()
    def save(self):
        k = Toplevel(self.m2)
        mygui = view(k)
        k.mainloop()
    def edit(self):
        self.r = 2
        root = Tk()
        t = edit(root)
        root.mainloop()
class Table:
    def __init__(self, root):
        mydb = mysql.connect(host="localhost", username="root",
                             password="Venkat@2003", database="studentdata")
        mycursor = mydb.cursor()
        mycursor.execute("select s_no,name,phone,code from application ")
        data = mycursor.fetchall()
        # code for creating table
        col = ["s_no", "name", "code", "phone"]
        def press(n):
            # print(n)
            mydb = mysql.connect(host="localhost", username="root",
                                 password="Venkat@2003", database="studentdata")
            mycursor = mydb.cursor()
            mycursor.execute(f"select * from application where s_no={n}")
            data = mycursor.fetchall()
            # print(data)
            j = Toplevel(root)
            j.geometry("600x300")
            # j.resizable(False,False)
            j.config(bg="blue")
            l=Label(j,text=n,bg="blue",font="arial 15",fg="#93ff93")
            l.place(x=10,y=6)
            l1 = Label(j, text="Name        :", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=25, y=30)
            l2 = Label(j, text=f"{data[0][0]}", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=150, y=30)
            l3 = Label(j, text="Degree      :", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=25, y=90)
            l4 = Label(j, text=f"{data[0][1]}", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=150, y=90)
            l5 = Label(j, text="Mail           :", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=25, y=120)
            l6 = Label(j, text=f"{data[0][2]}", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=150, y=120)
            l7 = Label(j, text="Date of Birth:", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=25, y=150)
            l8 = Label(j, text=f"{data[0][3]}", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=150, y=150)
            l9 = Label(j, text="Pincode      :", font="helvetica 15",
                       fg="#93ff93", bg="blue").place(x=25, y=180)
            l10 = Label(j, text=f"{data[0][4]}", font="helvetica 15",
                        fg="#93ff93", bg="blue").place(x=150, y=180)
            l11 = Label(j, text="Code         :", font="helvetica 15",
                        fg="#93ff93", bg="blue").place(x=25, y=210)
            l12 = Label(j, text=f"{data[0][5]}", font="helvetica 15",
                        fg="#93ff93", bg="blue").place(x=150, y=210)
            l13 = Label(j, text="Phone       :", font="helvetica 15",
                        fg="#93ff93", bg="blue").place(x=25, y=60)
            l14 = Label(j, text=f"{data[0][7]}", font="helvetica 15",
                        fg="#93ff93", bg="blue").place(x=150, y=60)
            y = data[0][6]
            image = Image.open(y)
            resize_image = image.resize((150, 100))
            img = ImageTk.PhotoImage(resize_image, master=j)
            label2 = Label(j, image=img)
            label2.image = img
            label2.place(x=425, y=50)
        """def check(e):
            ty=e10.get()
            if ty=="":
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, data[i][j])
                self.b = ttk.Button(root, text="View",
                                    command=lambda v=i+1: press(v))
                self.b.grid(row=i+1, column=j+1)
            else:
                 data=[]
                 #for """
        for i in range(len(col)):
            self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
            self.e.grid(row=0, column=i)
            self.e.insert(END, col[i])
        for i in range(len(data)):
            for j in range(4):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, data[i][j])
                self.b = ttk.Button(root, text="View",
                                    command=lambda v=i+1: press(v))
                self.b.grid(row=i+1, column=j+1)
        """l10=Label(root,text="serach",font="arial 10").grid(row=i+2,column=0)
        e10=Entry(root,width=40)
        e10.bind("<1>",check)
        e10.grid(row=i+2,column=1)"""
from tkinter import *
from tkinter import filedialog
from tkinter import Canvas
from PIL import Image, ImageTk
import mysql.connector as mysql
from PIL import ImageGrab
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

class view():
    def __init__(self,k):
        self.k=k
        self.k.geometry("350x250+1150+500")
        self.k.l1=Label(self.k,text="img 1").place(x=30,y=20)
        self.k.l2=Label(self.k,text="img 2").place(x=30,y=55)
        canvas = Canvas(self.k, bg="black")
        canvas.pack()
        self.lb1=Entry(self.k,width=35)
        self.lb1.place(x=70,y=23)
        self.k.b4=Button(self.k,text="Genrate Jpeg",width=10,command=self.genratejpeg)
        self.k.b4.place(x=130,y=130)
        self.k.b3=Button(self.k,text="Genrate Pdf",width=10,command=self.genratepdf)
        self.k.b3.place(x=130,y=170)
        self.k.b1=Button(self.k,text="Browse",width=10,command=self.browse1)
        self.k.b1.place(x=130,y=50)
        self.k.b2=Button(self.k,text="Color for Text",width=10,command=self.color)
        self.k.b2.place(x=130,y=90)
        self.k.b5=Button(self.k,text="Single print",width=10,command=self.one)
        self.k.b5.place(x=130,y=210)
    def browse1(self):
            global c1
            file=filedialog.askopenfilename(initialdir="D:\\")
            s=file.split("/")[-1]
            self.lb1.insert(END,s)
            c1=file
    def color(self):
            global cl
            choser=colorchooser.askcolor()
            lis=list(choser)
            cl=lis.pop(1)
    def one(self):
        global c0
        if self.lb1.get():
            self.b=Toplevel(self.k)
            self.b.config(bg="orange")
            self.b.geometry("350x200+1150+100")
            l0=Label(self.b,text="Enter the S.No",bg="orange").place(x=20,y=20)
            self.e0=Entry(self.b)
            self.e0.place(x=165,y=25)
            b0=Button(self.b,text="Genrate one",command=self.oneget)
            b0.place(x=110,y=55)
        else:
            messagebox.showinfo("Caution", "fill all the field")
    def oneget(self):
        
        c0=self.e0.get()
        mydb=mysql.connect(host="localhost"
                               ,username="root"
                               ,password="Venkat@2003"
                               ,database="studentdata")
        mycursor=mydb.cursor()
        mycursor.execute(f"select name,phone,code,img from application where s_no={c0}")
        data=mycursor.fetchall()
        for i in data:
            self.n=Toplevel(self.k)
            self.n.geometry("800x1500+50+20") 
            canvas= Canvas(self.n, width= 1000, height= 1000)
            canvas.pack()
            self.bg=Image.open(c1)
            self.resized_image= self.bg.resize((750,1334))
            self.img1= ImageTk.PhotoImage(self.resized_image)
            canvas.create_image(1,1,anchor=NW,image=self.img1)
            self.image1 = Image.open(i[3])
            self.resize_image1 = self.image1.resize((130,110))
            self.img2 = ImageTk.PhotoImage(self.resize_image1)
            canvas.create_image(600,550,anchor=NW,image=self.img2)
            self.t1=i[0]
            canvas.create_text(650,700,text=self.t1,font="arial 20 bold",fill=str(cl))
            self.t2=i[1]
            canvas.create_text(650,740,text=self.t2,font="arial 20 bold",fill=str(cl))
            self.t3=i[2]
            canvas.create_text(650,780,text=self.t3,font="arial 20 bold",fill=str(cl))
            s=0
            def save_as_image(self):
                s=1
                self.filepath =filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG", "*.jpeg")])
                if self.filepath:
                    x = 58
                    y = 60
                    width = self.n.winfo_width()
                    height = self.n.winfo_height()  
                    screenshot = ImageGrab.grab((x,y,width,height-30))
                    #print(type(self.filepath))
                    screenshot.save(self.filepath)
                    messagebox.showinfo("Success", "Image saved successfully!")
                messagebox.showinfo("Success", "Image saved successfully!")
                self.n.destroy()
            save_as_image(self) 
            if s==0:
                self.n.destroy()
    def genratejpeg(self):
        if self.lb1.get():
            mydb=mysql.connect(host="localhost"
                               ,username="root"
                               ,password="Venkat@2003"
                               ,database="studentdata")
            mycursor=mydb.cursor()
            mycursor.execute(f"select name,phone,code,img from application")
            data=mycursor.fetchall()
            for i in data:
                self.n=Toplevel(self.k)
                self.n.geometry("800x1500+50+20") 
                canvas= Canvas(self.n, width= 1000, height= 1000)
                canvas.pack()
                self.bg=Image.open(c1)
                self.resized_image= self.bg.resize((750,1334))
                self.img1= ImageTk.PhotoImage(self.resized_image)
                canvas.create_image(1,1,anchor=NW,image=self.img1)
                self.image1 = Image.open(i[3])
                self.resize_image1 = self.image1.resize((130,110))
                self.img2 = ImageTk.PhotoImage(self.resize_image1)
                canvas.create_image(600,550,anchor=NW,image=self.img2)
                self.t1=i[0]
                canvas.create_text(650,700,text=self.t1,font="arial 20 bold",fill=str(cl))
                self.t2=i[1]
                canvas.create_text(650,740,text=self.t2,font="arial 20 bold",fill=str(cl))
                self.t3=i[2]
                canvas.create_text(650,780,text=self.t3,font="arial 20 bold",fill=str(cl))
                s=0
                def save_as_image(self):
                    s=1
                    self.filepath =filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG", "*.jpeg")])
                    if self.filepath:
                        x = 58
                        y = 60
                        width = self.n.winfo_width()
                        height = self.n.winfo_height()  
                        screenshot = ImageGrab.grab((x,y,width,height-30))
                        #print(type(self.filepath))
                        screenshot.save(self.filepath)
                        messagebox.showinfo("Success", "Image saved successfully!")
                        self.n.destroy()
                    self.n.destroy()
                save_as_image(self) 
                if s==0:
                    self.n.destroy()
        else:
            messagebox.showinfo("Caution", "fill all the field")
    def genratepdf(self):
        if self.lb1.get():
            mydb=mysql.connect(host="localhost"
                               ,username="root"
                               ,password="Venkat@2003"
                               ,database="studentdata")
            mycursor=mydb.cursor()
            mycursor.execute(f"select name,phone,code,img from application")
            data=mycursor.fetchall()
            for i in data:
                self.n=Toplevel(self.k)
                self.n.geometry("800x1500+50+20") 
                canvas= Canvas(self.n, width= 1000, height= 1000)
                canvas.pack()
                self.bg=Image.open(c1)
                self.resized_image= self.bg.resize((750,1334))
                self.img1= ImageTk.PhotoImage(self.resized_image)
                canvas.create_image(1,1,anchor=NW,image=self.img1)
                self.image1 = Image.open(i[3])
                self.resize_image1 = self.image1.resize((130,110))
                self.img2 = ImageTk.PhotoImage(self.resize_image1)
                canvas.create_image(600,550,anchor=NW,image=self.img2)
                self.t1=i[0]
                canvas.create_text(650,700,text=self.t1,font="arial 20 bold",fill=str(cl))
                self.t2=i[1]
                canvas.create_text(650,740,text=self.t2,font="arial 20 bold",fill=str(cl))
                self.t3=i[2]
                canvas.create_text(650,780,text=self.t3,font="arial 20 bold",fill=str(cl))
                s=0
                def save_as_image(self):
                   s=1
                   self.filepath =filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
                   if self.filepath:
                       x = 58
                       y = 60
                       width = self.n.winfo_width()
                       height = self.n.winfo_height()  
                       screenshot = ImageGrab.grab((x,y,width,height-30))
                       #print(type(self.filepath))
                       screenshot.save(self.filepath)
                       messagebox.showinfo("Success", "Image saved successfully!")
                       self.n.destroy()
                save_as_image(self)
                if s==0:  
                    self.n.destroy()    
        else:
            messagebox.showinfo("Caution", "fill all the field")              
class edit:
    def __init__(self, root):
         mydb = mysql.connect(host="localhost", username="root",
                              password="Venkat@2003", database="studentdata")
         mycursor = mydb.cursor()
         mycursor.execute("select s_no,name,phone,code from application")
         data = mycursor.fetchall()
         # code for creating table
         col = ["s_no", "name", "phoneno", "code"]
         def press(n):
             mydb = mysql.connect(host="localhost", username="root",
                                  password="Venkat@2003", database="studentdata")
             mycursor = mydb.cursor()
             mycursor.execute(f"select * from application where s_no={n}")
             data = mycursor.fetchall()
             # print(data)
         for i in range(len(col)):
             self.e = Entry(root, width=20, fg='blue',
                                font=('Arial', 16, 'bold'))
             self.e.grid(row=0, column=i)
             self.e.insert(END, col[i])
         for i in range(len(data)):
             for j in range(4):
                 self.e = Entry(root, width=20, fg='blue',
                                font=('Arial', 16, 'bold'))
                 self.e.grid(row=i+1, column=j)
                 self.e.insert(END, data[i][j])
                 # button = tk.Button(root, text=value, command=lambda v=value: button_click(v))
                 self.b = ttk.Button(root, text="Edit",
                                     command=lambda v=i+1: funedit(v))
                 self.b.grid(row=i+1, column=j+1)
         def funedit(n):
             global a
             a=n
             mydb = mysql.connect(host="localhost", username="root",
                                  password="Venkat@2003", database="studentdata")
             mycursor = mydb.cursor()
             mycursor.execute(f"select * from application where s_no={n}")
             data = mycursor.fetchall()
             #print(data)
             h = Toplevel(root)
             h.geometry("600x300")
               # j.resizable(False,False)
               #print(self.data)
             n = data[0][0]
             p = data[0][5]
             de = data[0][1]
             co = data[0][7] 
             em = data[0][2]
             do = data[0][3]
             pl = data[0][4]
             #im = data[0][6] 
             h.config(bg="blue") 
             l1 = Label(h, text="Name:", font="helvetica 15",
                         fg="#93ff93", bg="blue").place(x=25, y=30)
             self.e1 = Entry(h)
             self.e1.place(x=150, y=30)
             self.e1.insert(0,n)       
             l3 = Label(h, text="phone:", font="helvetica 15",
                          fg="#93ff93", bg="blue").place(x=25, y=90)
             self.e2 = Entry(h)
             self.e2.insert(0,p)
             self.e2.place(x=150, y=90)
             l5 = Label(h, text="degree:", font="helvetica 15",
                          fg="#93ff93", bg="blue").place(x=25, y=120)
             self.e3 = Entry(h)
             self.e3.insert(0,de)
             self.e3.place(x=150, y=120)
             l7 = Label(h, text="code:", font="helvetica 15",
                          fg="#93ff93", bg="blue").place(x=25, y=150)
             self.e4 = Entry(h)
             self.e4.insert(0,co)
             self.e4.config(state= "disabled")

             self.e4.place(x=150, y=150)
             l9 = Label(h, text="e_mail:", font="helvetica 15",
                          fg="#93ff93", bg="blue").place(x=25, y=180)
             self.e5 = Entry(h)
             self.e5.insert(0,em)
             self.e5.place(x=150, y=180)
             l11 = Label(h, text="Dob:", font="helvetica 15",
                         fg="#93ff93", bg="blue").place(x=25, y=210)
             self.e6 = Entry(h)
             self.e6.insert(0,do)
             self.e6.place(x=150, y=210)
             l13 = Label(h, text="Place:", font="helvetica 15",
                          fg="#93ff93", bg="blue").place(x=25, y=60)
             self.e7 = Entry(h)
             self.e7.insert(0,pl)
             self.e7.place(x=150, y=60)
             y = data[0][8]
             b1 = Button(master=h, text="Submit",command=lambda:submit(a))
             b1.place(x=420, y=150)
         def submit(n):
            na,de,em,do,pl,ph,co=self.e1.get(),self.e3.get(),self.e5.get(),self.e6.get(),self.e7.get(),self.e2.get(),self.e4.get()
            #print(na,de,em,do,pl,ph,co)
            mydb = mysql.connect(host="localhost", username="root",
                                 password="Venkat@2003", database="studentdata")
            mycursor = mydb.cursor()
            #print("UPDATE application SET name={na}, deg={de}, e_mail={em}, dob={do}, place={pl}, phone={ph}, code={co}  WHERE s_no={n}")
            #q="UPDATE application SET name=%s, deg=%s, e_mail=%s, dob=%s, place=%s, phone=%s, code=%sWHERE s_no=%s"%(na,de,em,do,pl,ph,co,n)
            q='UPDATE application SET name=%s , deg=%s, e_mail=%s, dob=%s, place=%s, phone=%s, code=%s WHERE s_no=%s'
            v=(na,de,em,do,pl,ph,co,n)
            mycursor.execute(q,v)
            mycursor.close()
            mydb.commit()
def main1():
    m2 = Tk()
    mygui = dashboard(m2)
    m2.mainloop()
main1()