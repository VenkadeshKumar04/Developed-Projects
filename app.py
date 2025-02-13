
from tkinter import *
from tkinter import filedialog
import mysql.connector as mysql
from tkcalendar import Calendar,DateEntry
import time
from tkinter import messagebox
#from geopy.geocoders import Nominatim
from PIL import ImageTk, Image
from datetime import datetime
#from datetime import date
#import datetime
import re     
class application():
    def __init__(self,m):
        self.m=m
        self.m.geometry("450x450")
        self.m.config(bg="yellow")
        self.l1=Label(m,text="Application form",font="helvetica 20 bold",bg="yellow").place(x=110,y=20)
        self.l2=Label(m,text="Name",bg="yellow",font="helvetica 15 bold",).place(x=70,y=60)
        self.l3=Label(m,text="Degree",bg="yellow",font="helvetica 15 bold",).place(x=70,y=100)
        self.l4=Label(m,text="E-Mail",bg="yellow",font="helvetica 15 bold",).place(x=70,y=140)
        self.l5=Label(m,text="DOB",bg="yellow",font="helvetica 15 bold",).place(x=70,y=180)
        self.l6=Label(m,text="Pincode",bg="yellow",font="helvetica 15 bold",).place(x=70,y=220)
        self.l7=Label(m,text="Phone NO.",bg="yellow",font="helvetica 15 bold",).place(x=70,y=260)
        self.l8=Label(m,text="Image",bg="yellow",font="helvetica 15 bold",).place(x=70,y=300)
        self.l9=Label(m,text="Code",bg="yellow",font="helvetica 15 bold",).place(x=70,y=350)
        def validate_entry(text):
            if text=='' or (text.isdigit() and len(text)<=10):
                return True
            else :
                return False
        def validate_entry1(text):
            if text=='' or (text.isdigit() and len(text)<=6):
                return True
            else :
                return False
        def validate_entry2(text):
            return 0<=len(text)<=10
        self.e1=Entry(m,width=30)
        self.e1.place(x=175,y=65)
        self.e2=Entry(m,width=30)
        self.e2.place(x=175,y=105)
        self.e3=Entry(m,width=30)
        self.e3.place(x=175,y=145)
        self.e3.insert(0,"@gmail.com")
        validate_entry_cmd = m.register(validate_entry)
        validate_entry1_cmd = m.register(validate_entry1)
        validate_entry2_cmd = m.register(validate_entry2)
        self.e4=DateEntry(m)
        self.e4.place(x=175,y=185)
        self.e5=Entry(m,width=30, validate="key", validatecommand=(validate_entry1_cmd, '%P'))
        self.e5.place(x=175,y=225)
        self.e6=Entry(m,width=30, validate="key", validatecommand=(validate_entry_cmd, '%P'))
        self.e6.place(x=175,y=265)
        #self.e5.bind("<1>", handle_click)
        self.e7=Entry(m,width=30)
        self.e7.place(x=175,y=305)
        self.e8=Entry(m,width=30, validate="key", validatecommand=(validate_entry2_cmd, '%P'))
        self.e8.place(x=175,y=355)
        self.b1=Button(m,text="Browse",activebackground="blue",command=self.browse).place(x=365,y=300)
        self.b2=Button(m,text="Submit",activebackground="blue",command=self.adddata).place(x=235,y=400)
    def adddata(self):
        mydb=mysql.connect(host="localhost"
                           ,username="root"
                           ,password="Venkat@2003")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists studentdata")
        mydb=mysql.connect(host="localhost"
                           ,username="root"
                           ,password="Venkat@2003",
                           database="studentdata")
        mycursor=mydb.cursor()
        mycursor.execute("create table if not exists application(name varchar(45),deg varchar(45),e_mail varchar(255),dob date,place varchar(100),phone varchar(15),img varchar(500),code varchar(20) unique,s_no int AUTO_INCREMENT PRIMARY KEY)")
        def insert():
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            u_input=self.e3.get()
            d1=self.e4.get()
            d2=datetime.today().strftime("%m/%d/%y")
            from_date=datetime.strptime(d1,"%m/%d/%y")
            to_date=datetime.strptime(d2,"%m/%d/%y")
            res=abs((to_date-from_date).days)//365
            if self.e1.get()and self.e2.get() and self.e3.get() and self.e4.get() and self.e5.get() and self.e6.get() and self.e7.get() and self.e8.get():
                n,deg,email,dob1,pla,mob,img,code=self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get(),self.e6.get(),self.e7.get(),self.e8.get()
                if res>=16:
                    if(re.search(regex,u_input) and u_input.isalpha):
                    
                        s="insert into application(name,deg,e_mail,dob,place,phone,img,code) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                        v=(n,deg,email,dob1,pla,mob,img,code)
                        mycursor.execute(s,v)
                        mydb.commit()
                    else:      
                        messagebox.showinfo("Caution", "Your Email has to be in format")    
                else:
                    messagebox.showinfo("Caution", "Your are not eligible")    
            else:
                messagebox.showinfo("Caution", "Fill the Empty Field")
        mycursor.execute("SELECT COUNT(*) FROM application")
        count=mycursor.fetchall()
        exist=False
        if count==0:
            insert()
        else: 
            mycursor.execute("SELECT code FROM application")
            codelist=mycursor.fetchall()
            for i in codelist:
                if self.e8.get() in i:
                    exist=True
                    messagebox.showinfo("Caution", "Code has been alreay existed")
            if exist!=True:
                insert()
    def browse(self):
         
        file=filedialog.askopenfilename(initialdir="D:\\")
        self.e7.delete(0,END)
        self.e7.insert(0,file)
        img= (Image.open(file))
        resizedimage= img.resize((80,60))
        new_image= ImageTk.PhotoImage(resizedimage,master=self.m)
        l = Label(self.m,image=new_image)
        l.image = new_image
        l.place(x=355,y=345)
        
def main():
    m = Tk()
    mygui = application(m)
    m.mainloop()
main()