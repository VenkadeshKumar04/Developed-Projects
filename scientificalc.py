from tkinter import *
import tkinter as tk
import math
import re

class clac():
    def __init__(self):
        self.c=Tk()
        c=self.c
        self.c.geometry('540x390')
        self.c.config(bg='#FFF8E7')
        self.c.resizable(False,False)
        def validate_entry(text):
            if self.e1[0].text=='' or text.isdigit():
                return True
            else :
                return False
        validate_entry_cmd = c.register(validate_entry)
        self.e1=Entry(self.c,width=25,font=("Times",30),border=10,borderwidth=10,bg='#E0FFFF',validatecommand=(validate_entry_cmd, '%P'))
        self.e1.place(x=8,y=0)
        self.b1=tk.Button(self.c,text='C',height=3,width=32,font='arial 10 bold',activebackground='lightblue',bg='red',command=self.clear)
        self.b1.place(x=2,y=80)
        self.b2=tk.Button(self.c,text='7',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("7"))
        self.b2.place(x=0,y=140)
        self.b3=tk.Button(self.c,text='4',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("4"))
        self.b3.place(x=0,y=200)
        self.b4=tk.Button(self.c,text='1',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("1"))
        self.b4.place(x=0,y=260)
        self.b5=tk.Button(self.c,text='.',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("."))
        self.b5.place(x=0,y=320)
        self.b6=tk.Button(self.c,text='8',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("8"))
        self.b6.place(x=90,y=140)
        self.b7=tk.Button(self.c,text='5',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("5"))
        self.b7.place(x=90,y=200)
        self.b8=tk.Button(self.c,text='2',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("2"))
        self.b8.place(x=90,y=260)
        self.b9=tk.Button(self.c,text='0',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("0"))
        self.b9.place(x=90,y=320)
        self.b10=tk.Button(self.c,text='9',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("9"))
        self.b10.place(x=180,y=140)
        self.b11=tk.Button(self.c,text='6',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("6"))
        self.b11.place(x=180,y=200)
        self.b12=tk.Button(self.c,text='3',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("3"))
        self.b12.place(x=180,y=260)
        self.b13=tk.Button(self.c,text='=',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=self.eva)
        self.b13.place(x=180,y=320)
        self.b14=tk.Button(self.c,text='+',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("+"))
        self.b14.place(x=270,y=80)
        self.b15=tk.Button(self.c,text='-',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("-"))
        self.b15.place(x=270,y=140)
        self.b16=tk.Button(self.c,text='*',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("*"))
        self.b16.place(x=270,y=200)
        self.b17=tk.Button(self.c,text='/',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda:self.press("/"))
        self.b17.place(x=270,y=260)
        self.b18=tk.Button(self.c,text='⟵',height=3,width=21,font='arial 10 bold',bg='yellow',activebackground='lightblue',command=self.bs)
        self.b18.place(x=270,y=320)
        self.b19=tk.Button(self.c,text='Exp',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda t='exp':self.trig(t))
        self.b19.place(x=360,y=80)
        self.b20=tk.Button(self.c,text='Deg',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=self.deg)
        self.b20.place(x=360,y=140)
        self.b21=tk.Button(self.c,text='sin',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda t='sin':self.trig(t))
        self.b21.place(x=360,y=200)
        self.b22=tk.Button(self.c,text='Tan',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda t='tan':self.trig(t))
        self.b22.place(x=360,y=260)
        self.b23=tk.Button(self.c,text='x²',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=self.po)
        self.b23.place(x=450,y=80)
        self.b24=tk.Button(self.c,text='Rad',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=self.rad)
        self.b24.place(x=450,y=140)
        self.b25=tk.Button(self.c,text='Cos',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda t='cos':self.trig(t))
        self.b25.place(x=450,y=200)
        self.b26=tk.Button(self.c,text='√',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda t='sqrt':self.trig(t))
        self.b26.place(x=450,y=260)
        self.b27=tk.Button(self.c,text='loge',height=3,width=10,font='arial 10 bold',bg='#FFF8E7',activebackground='lightblue',command=lambda t='log':self.trig(t))
        self.b27.place(x=450,y=320)
        self.dis()
    def disall(self):
        self.b2['state']=tk.DISABLED
        self.b3['state']=tk.DISABLED
        self.b4['state']=tk.DISABLED
        self.b5['state']=tk.DISABLED
        self.b6['state']=tk.DISABLED
        self.b7['state']=tk.DISABLED
        self.b8['state']=tk.DISABLED
        self.b9['state']=tk.DISABLED
        self.b10['state']=tk.DISABLED
        self.b11['state']=tk.DISABLED
        self.b12['state']=tk.DISABLED
        self.b13['state']=tk.DISABLED
        self.b14['state']=tk.DISABLED
        self.b15['state']=tk.DISABLED
        self.b16['state']=tk.DISABLED
        self.b17['state']=tk.DISABLED
        self.b18['state']=tk.DISABLED
        self.b19['state']=tk.DISABLED
        self.b20['state']=tk.DISABLED
        self.b21['state']=tk.DISABLED
        self.b22['state']=tk.DISABLED
        self.b23['state']=tk.DISABLED
        self.b24['state']=tk.DISABLED
        self.b25['state']=tk.DISABLED
        self.b26['state']=tk.DISABLED
        self.b27['state']=tk.DISABLED
    def ennum(self):
        self.b2['state']=tk.NORMAL
        self.b3['state']=tk.NORMAL
        self.b4['state']=tk.NORMAL
        self.b5['state']=tk.NORMAL
        self.b6['state']=tk.NORMAL
        self.b7['state']=tk.NORMAL
        self.b8['state']=tk.NORMAL
        self.b9['state']=tk.NORMAL
        self.b10['state']=tk.NORMAL
        self.b11['state']=tk.NORMAL
        self.b12['state']=tk.NORMAL
        self.b13['state']=tk.NORMAL
    def dis(self):
        self.b14['state']=tk.DISABLED
        self.b15['state']=tk.DISABLED
        self.b16['state']=tk.DISABLED
        self.b17['state']=tk.DISABLED
        self.b19['state']=tk.DISABLED
        self.b20['state']=tk.DISABLED
        self.b21['state']=tk.DISABLED
        self.b22['state']=tk.DISABLED
        self.b23['state']=tk.DISABLED
        self.b24['state']=tk.DISABLED
        self.b25['state']=tk.DISABLED
        self.b26['state']=tk.DISABLED
        self.b27['state']=tk.DISABLED
    def ana(self):
        self.b14['state']=tk.NORMAL
        self.b15['state']=tk.NORMAL
        self.b16['state']=tk.NORMAL
        self.b17['state']=tk.NORMAL
        self.b19['state']=tk.NORMAL
        self.b20['state']=tk.NORMAL
        self.b21['state']=tk.NORMAL
        self.b22['state']=tk.NORMAL
        self.b23['state']=tk.NORMAL
        self.b24['state']=tk.NORMAL
        self.b25['state']=tk.NORMAL
        self.b26['state']=tk.NORMAL
        self.b27['state']=tk.NORMAL
        self.b13['state']=tk.NORMAL
    def trig(self,b):
        result=getattr(math,b)(float(self.e1.get()))
        self.e1.delete(0,END)
        self.e1.insert(END,result)
    def po(self):                         
        w=int(self.e1.get())
        w=w*w
        self.e1.delete(0,END)
        self.e1.insert(END,w)
    def bs(self):
        w=self.e1.get()                  
        c=w[:-1]
        self.e1.delete(0,END)
        self.e1.insert(END,c)
        if len(self.e1.get())==0:
            self.dis()
    def press(self,n):
        value=self.e1.get()
        s=['*','/','+','-','√']
        if value:
            if n in s and value[-1] in s:
                if n==value[-1]:
                    n="" 
                else :
                    self.e1.delete(len(self.e1.get())-1,END)
            elif n=="." and value[-1]=="." :
                n=""
            elif n=="." and value[-1] in s:
                n="0."
        self.e1.insert(END,n)
        self.ana()
    def deg(self):
        try:
            n=self.e1.get()
            de=math.degrees(int(n))
            self.e1.delete(0,END)
            self.e1.insert(END,de)
        except ValueError:
            self.e1.delete(0,END)   
            self.e1.insert(END,"Syntax Error")
            self.dis()
            self.disall()
    def rad(self):
        try:
            n=self.e1.get()
            rad=math.radians(int(n))
            self.e1.delete(0,END)
            self.e1.insert(END,rad)
        except ValueError:
            self.e1.delete(0,END)   
            self.e1.insert(END,"Syntax Error")
            self.dis()
            self.disall()
    def clear(self):
        self.e1.delete(0,END)
        self.dis()
        self.ennum()
    def eva(self):
        try:
            x=eval(self.e1.get())
            self.e1.delete(0,END)
            self.e1.insert(END,x)
        except ZeroDivisionError:
            r="∞"
            self.e1.delete(0,END)   
            self.e1.insert(END,r)
            self.disall()
        except ValueError:
            self.e1.delete(0,END)   
            self.e1.insert(END,"Syntax Error")
def main():
    mygui = clac()
    mainloop()
main()