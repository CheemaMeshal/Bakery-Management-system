from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import random
from ttkthemes import ThemedTk
from tkcalendar import Calendar, DateEntry
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
import smtplib
from tkinter import ttk 
from ttkthemes import ThemedTk
class EmpHome:
    def __init__(target,window):
        target.window = window
        target.window.title("CAKES AND BAKES-EMPLOYEE DASHBOARD".center(420))  
        target.window.configure(background = "white")  
        target.window.geometry("1360x768")
        background_color ="light yellow"
        target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
        target.img_background = Label(target.window, image = target.background)
        target.img_background.place(x=0, y=0)
        
        
        Frame1 = LabelFrame(target.window,bd=0,relief=GROOVE,background="light yellow")
        Frame1.place(x=0,relwidth=2,height=150)

        labelll = Label(Frame1,text="CAKES & BAKES-EMPLOYEE DASHBOARD", background="light yellow", font= ("new times roman",25,"bold")).place(x=400, y=25)
        labelll = Label(Frame1,text="Time : ", background="light yellow", font= ("new times roman",15,"bold")).place(x=840, y=65)

        target.labelll_hour = Label(Frame1,text="12" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labelll_hour.place(x=900, y=65)
        
        target.labelll_COLON = Label(Frame1,text=":" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labelll_COLON.place(x=925, y=65)
       
       
        target.labelll_min = Label(Frame1,text="12" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labelll_min.place(x=940, y=65)
       
        target.labelll_COLON = Label(Frame1,text=":" ,fg="black" ,background="light yellow",font = ("new times roman",15))
        target.labelll_COLON.place(x=965, y=65)
       
        target.labelll_sec = Label(Frame1,text="12" ,fg="black", background="light yellow",font = ("new times roman",15))
        target.labelll_sec.place(x=980, y=65)
        

        target.labelll_abv = Label(Frame1,text="AM" ,fg="black",background="light yellow", font = ("new times roman",15))
        target.labelll_abv.place(x=1005, y=65)
       
       
        
        target.conn=sqlite3.connect("bakery.db")
        target.c=target.conn.cursor()
        

        frame4 = LabelFrame(target.window,bd=0,relief=GROOVE,background="light yellow")
        frame4.place(x=500,y=170,width=400,height=500 )

        
        labelll_1= Label(frame4,text="EMPLOYEE DETAILS",fg="black",background="light yellow",font=("new times roman",20,"bold"))
        labelll_1.place(x=70,y=10)
        labelll_2= Label(frame4,text="NAME : Haris Baig",fg="black",background="light yellow",font=("new times roman",15))
        labelll_2.place(x=0,y=55)
        labelll_3= Label(frame4,text="PASSWORD : ***************",fg="black",background="light yellow",font=("new times roman",15))
        labelll_3.place(x=0,y=90)
        labelll_3= Label(frame4,text="GMAIL : harisB12@yahoo.com",fg="black",background="light yellow",font=("new times roman",15))
        labelll_3.place(x=0,y=125)
        labelll_3= Label(frame4,text="PHONE : 923335394817",fg="black",background="light yellow",font=("new times roman",15))
        labelll_3.place(x=0,y=160)
        labelll_3= Label(frame4,text="Click Here to change Password",fg="black",background="light yellow",font=("new times roman",15))
        labelll_3.place(x=0,y=200)
        button_changepass = Button(frame4, text="Change Password",relief=RAISED,width =15,height=1, font=("new times roman",13,"bold"),background="black",foreground="white",command=target.passwordchange).place(x=105,y=255,anchor="w")
        button_logout = Button(frame4, text="Log Out",relief=RAISED,width =10,height=1, font=("new times roman",13,"bold"),background="black",foreground="white",command=target.logout).place(x=250,y=450,anchor="w")
        labelll_3= Label(frame4,text="Click Here to change Phone Number",fg="black",background="light yellow",font=("new times roman",15))
        labelll_3.place(x=0,y=280)
        button_changephoe = Button(frame4, text="Change Phone Number",relief=RAISED,width =20,height=1, font=("new times roman",13,"bold"),background="black",foreground="white",command=target.phonechange).place(x=85,y=347,anchor="w")
        
        target.button_home=Button(target.window, relief=GROOVE,bd=0,text="HOME", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.homeEmp)
        target.button_home.place(x=20, y=170)
        target.employees=Button(target.window, relief=GROOVE,bd=0,text="SEARCH PRODUCTS", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.M_EMP)
        target.employees.place(x=150, y=170)
        target.adminss=Button(target.window, relief=GROOVE,bd=0,text="SALES", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.SAL_EMP)
        target.adminss.place(x=950, y=170)
        target.inventoryview=Button(target.window, relief=GROOVE,bd=0,text="INVENTORY", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.inventory)
        target.inventoryview.place(x=1120, y=170)
       
        target.ButtonRSF_8 = Button(target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.backto)
        target.ButtonRSF_8.place(x=10, y=650)
        
        
        
        
        
        


        target.time()
    def backto(target):
        target.window.destroy()
        import loginEmployee
    def time(target):
        target.h = str(time.strftime("%H"))
        target.m = str(time.strftime("%M"))
        target.s = str(time.strftime("%S"))

        if int(target.h)>=12 and int(target.h)<15 and int(target.m)>0:
            target.labelll_abv.config(text="PM")

        if int(target.h)>=15 and int(target.h)<20 and int(target.m)>0:
            target.labelll_abv.config(text="PM")
        
        if int(target.h)>=20 and int(target.h)<24 and int(target.m)>0:
            target.labelll_abv.config(text="PM")

        if int(target.h)>12 and int(target.h)<15 and int(target.m)>0:
            target.labelll_abv.config(text="PM")

        if int(target.h)>0 and int(target.h)<12 and int(target.m)>0:
            target.labelll_abv.config(text="AM")

        
        target.labelll_hour.config(text = target.h)
        target.labelll_min.config(text = target.m)
        target.labelll_sec.config(text = target.s)
        target.labelll_hour.after(200,target.time)



    def logout(target):
        import loginEmployee
        

    
    def homeEmp(target):
        target.window.destroy()
        import HEmployee
        
    def M_EMP(target):
        target.window.destroy()
        import SearchBYemp

    def SAL_EMP(target):
        target.window.destroy()
        import SalesEmp
    
    def inventory(target):
        target.window.destroy()
        import InventoryEmployee

    def passwordchange(target):  
        target.window2 = Toplevel(window)  
        target.window2.title("CAKES & BAKES")
        target.window2.geometry("1000x500+0+0")
        target.window2.configure(background="white")
        
        target.window2.grab_set() 
        target.window2.resizable(False, False)

        title_child = Label(target.window2, text="Kindly Fill in details to Change your Password", background="white", fg="black",compound=LEFT, font=("new times roman", 18, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_labelll = Label(target.window2, text="Enter Your Phone Number", font=("time new roman", 13), background="white", fg="black").place(x=0, y=60)
        target.phone_ = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.phone_.place(x=0, y=100)
        
        current_labelll = Label(target.window2, text="Enter Your Current Password", font=("time new roman", 13), fg="black", background="white").place(x=0, y=140)
        target.current_ = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.current_.place(x=0, y=180)
        
        pass_labelll = Label(target.window2, text="Enter Your New Password", font=("time new roman", 13), fg="black", background="white").place(x=0, y=220)
        target.pass_ = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.pass_.place(x=0, y=260)
        
        passcon_labelll = Label(target.window2, text="Confirm Your  Password", font=("time new roman", 13), fg="black", background="white").place(x=0, y=300)
        target.passcon = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.passcon.place(x=0, y=330)
        
        Reset_button = Button(target.window2, text="SAVE", font=("new times roman", 18, "bold"), activebackground="blue",activeforeground="white", background="blue", fg="white", cursor="hand2", command=target.reset)
        Reset_button.place(x=400, y=430, width=140, height=30) 

    def phonechange(target):  
        target.window2 = Toplevel(window)  
        target.window2.title("CAKES & BAKES")
        target.window2.geometry("1000x500+0+0")
        target.window2.configure(background="white")
       
        target.window2.grab_set() 
        target.window2.resizable(False, False)

        title_child = Label(target.window2, text="Kindly Fill in details to Change your Phone Number", background="white", fg="black",compound=LEFT, font=("new times roman", 18, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_labelll = Label(target.window2, text="Enter Your Password", font=("time new roman", 13), background="white", fg="black").place(x=0, y=60)
        target.phone_ = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.phone_.place(x=0, y=100)
        
        current_labelll = Label(target.window2, text="Enter Your Current Phone Number", font=("time new roman", 13), fg="black", background="white").place(x=0, y=140)
        target.current_ = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.current_.place(x=0, y=180)
        
        pass_labelll = Label(target.window2, text="Enter Your New Phone Number", font=("time new roman", 13), fg="black", background="white").place(x=0, y=220)
        target.pass_ = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.pass_.place(x=0, y=260)
        
        passcon_labelll = Label(target.window2, text="Confirm Your Phone Number", font=("time new roman", 13), fg="black", background="white").place(x=0, y=300)
        target.passcon = Entry(target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        target.passcon.place(x=0, y=330)
        
        Reset_button = Button(target.window2, text="SAVE", font=("new times roman", 18, "bold"), activebackground="blue",activeforeground="white", background="blue", fg="white", cursor="hand2", command=target.reset)
        Reset_button.place(x=400, y=430, width=140, height=30) 

        
    def reset(target):
        target.window.destroy()

   

    
    def Exit(target):
        target.window.destroy()
            

window = Tk()
obj = EmpHome(window)
window.mainloop()
