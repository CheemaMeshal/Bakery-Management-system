from tkinter import *
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
class AdminHome:
    def __init__(Target,window):
        Target.window = window
        Target.window.title("CAKES AND BAKES-ADMIN DASHBOARD".center(420))  
        Target.window.configure(background = "white")  
        Target.window.geometry("1360x768")
        background_color ="light pink"
        Target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
        Target.img_background = Label(Target.window, image = Target.background)
        Target.img_background.place(x=0, y=0)
        Frame1 = LabelFrame(Target.window,bd=0,relief=GROOVE,background="light pink")
        Frame1.place(x=0,relwidth=2,height=150)
        

        labeldefined = Label(Frame1,text="CAKES & BAKES-ADMIN DASHBOARD", background="light pink", font= ("new times roman",25,"bold")).place(x=400, y=25)
        labeldefined = Label(Frame1,text="Time : ", background="light pink", font= ("new times roman",15,"bold")).place(x=840, y=65)

        Target.labeldefined_hour = Label(Frame1,text="12" , fg="black",background="light pink",font = ("new times roman", 15))
        Target.labeldefined_hour.place(x=900, y=65)
        
        Target.labeldefined_COLON = Label(Frame1,text=":" , fg="black",background="light pink",font = ("new times roman", 15))
        Target.labeldefined_COLON.place(x=925, y=65)
       
       
        Target.labeldefined_min = Label(Frame1,text="12" , fg="black",background="light pink",font = ("new times roman", 15))
        Target.labeldefined_min.place(x=940, y=65)
       
        Target.labeldefined_COLON = Label(Frame1,text=":" ,fg="black" ,background="light pink",font = ("new times roman",15))
        Target.labeldefined_COLON.place(x=965, y=65)
       
        Target.labeldefined_sec = Label(Frame1,text="12" ,fg="black", background="light pink",font = ("new times roman",15))
        Target.labeldefined_sec.place(x=980, y=65)
        

        Target.labeldefined_abv = Label(Frame1,text="AM" ,fg="black",background="light pink", font = ("new times roman",15))
        Target.labeldefined_abv.place(x=1005, y=65)
        Target.conn=sqlite3.connect("bakery.db")
        Target.c=Target.conn.cursor()
        

        Frame4 = LabelFrame(Target.window,bd=0,relief=GROOVE,background="light pink")
        Frame4.place(x=500,y=170,width=400,height=500 )

       
        labeldefined_1= Label(Frame4,text="ADMIN DETAILS",fg="black",background="light pink",font=("new times roman",20,"bold"))
        labeldefined_1.place(x=100,y=10)
        labeldefined_2= Label(Frame4,text="NAME : Meshal Cheema",fg="black",background="light pink",font=("new times roman",15))
        labeldefined_2.place(x=0,y=55)
        labeldefined_3= Label(Frame4,text="PASSWORD : ********",fg="black",background="light pink",font=("new times roman",15))
        labeldefined_3.place(x=0,y=90)
        labeldefined_3= Label(Frame4,text="GMAIL : cheemameshaal@gmail.com",fg="black",background="light pink",font=("new times roman",15))
        labeldefined_3.place(x=0,y=125)
        labeldefined_3= Label(Frame4,text="PHONE : 923360590613",fg="black",background="light pink",font=("new times roman",15))
        labeldefined_3.place(x=0,y=160)
        labeldefined_3= Label(Frame4,text="Click Here to change Password",fg="black",background="light pink",font=("new times roman",15))
        labeldefined_3.place(x=0,y=200)
        button_changepass = Button(Frame4, text="Change Password",relief=RAISED,width =15,height=1, font=("new times roman",13,"bold"),background="black",foreground="white",command=Target.PasswordChange).place(x=105,y=255,anchor="w")
        button_logoutAdmin= Button(Frame4, text="Log Out",relief=RAISED,width =10,height=1, font=("new times roman",13,"bold"),background="black",foreground="white",command=Target.logoutAdmin).place(x=250,y=450,anchor="w")
        labeldefined_3= Label(Frame4,text="Click Here to change Phone Number",fg="black",background="light pink",font=("new times roman",15))
        labeldefined_3.place(x=0,y=280)
        button_changephoe = Button(Frame4, text="Change Phone Number",relief=RAISED,width =20,height=1, font=("new times roman",13,"bold"),background="black",foreground="white",command=Target.phonechange).place(x=85,y=347,anchor="w")
       
        Target.button_home=Button(Target.window, relief=GROOVE,bd=0,text="HOME", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=Target.AdminHome)
        Target.button_home.place(x=20, y=170)
        Target.employees=Button(Target.window, relief=GROOVE,bd=0,text="EMPLOYEES", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=Target.Managing_Emp)
        Target.employees.place(x=150, y=170)
        Target.adminss=Button(Target.window, relief=GROOVE,bd=0,text="ADMINS", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=Target.backwards)
        Target.adminss.place(x=950, y=170)
        Target.inventoryview=Button(Target.window, relief=GROOVE,bd=0,text="INVENTORY", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=Target.inventory)
        Target.inventoryview.place(x=1120, y=170)
        Target.ButtonRSF_8 = Button(Target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=Target.backwards)
        Target.ButtonRSF_8.place(x=370, y=170)
        Target.Time()
    
    def backwards(Target):
        Target.window.destroy()
        import LoginAdmin
    def Time(Target):
        Target.h = str(time.strftime("%H"))
        Target.m = str(time.strftime("%M"))
        Target.s = str(time.strftime("%S"))

        if int(Target.h)>=12 and int(Target.h)<15 and int(Target.m)>0:
            Target.labeldefined_abv.config(text="PM")

        if int(Target.h)>=15 and int(Target.h)<20 and int(Target.m)>0:
            Target.labeldefined_abv.config(text="PM")
        
        if int(Target.h)>=20 and int(Target.h)<24 and int(Target.m)>0:
            Target.labeldefined_abv.config(text="PM")

        if int(Target.h)>12 and int(Target.h)<15 and int(Target.m)>0:
            Target.labeldefined_abv.config(text="PM")

        if int(Target.h)>0 and int(Target.h)<12 and int(Target.m)>0:
            Target.labeldefined_abv.config(text="AM")

        
        Target.labeldefined_hour.config(text = Target.h)
        Target.labeldefined_min.config(text = Target.m)
        Target.labeldefined_sec.config(text = Target.s)
        Target.labeldefined_hour.after(200,Target.Time)



    def logoutAdmin(Target):
         Target.window.destroy()
         import LoginAdmin
        

    
    def AdminHome(Target):
        Target.window.destroy()
        import HAdmin
        
    def Managing_Emp(Target):
        Target.window.destroy()
        import AdminManageEmp

   
        
    
    def inventory(Target):
        Target.window.destroy()
        import InventoryAdmin

    def PasswordChange(Target):  
        Target.window2 = Toplevel(window)  
        Target.window2.title("CAKES & BAKES")
        Target.window2.geometry("1000x500+0+0")
        Target.window2.configure(background="white")
        
        Target.window2.grab_set() 
        Target.window2.resizable(False, False)

        title_child = Label(Target.window2, text="Kindly Fill in details to Change your Password", background="white", fg="black",compound=LEFT, font=("new times roman", 18, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_labeldefined = Label(Target.window2, text="Enter Your Phone Number", font=("time new roman", 13), background="white", fg="black").place(x=0, y=60)
        Target.phone_ = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.phone_.place(x=0, y=100)
        
        current_labeldefined = Label(Target.window2, text="Enter Your Current Password", font=("time new roman", 13), fg="black", background="white").place(x=0, y=140)
        Target.current_ = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.current_.place(x=0, y=180)
        
        pass_labeldefined = Label(Target.window2, text="Enter Your New Password", font=("time new roman", 13), fg="black", background="white").place(x=0, y=220)
        Target.pass_ = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.pass_.place(x=0, y=260)
        
        passcon_labeldefined = Label(Target.window2, text="Confirm Your  Password", font=("time new roman", 13), fg="black", background="white").place(x=0, y=300)
        Target.passcon = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.passcon.place(x=0, y=330)
        
        Reset_button = Button(Target.window2, text="SAVE", font=("new times roman", 18, "bold"), activebackground="blue",activeforeground="white", background="blue", fg="white", cursor="hand2", command=Target.reset)
        Reset_button.place(x=400, y=430, width=140, height=30) 

    def phonechange(Target):  
        Target.window2 = Toplevel(window)  
        Target.window2.title("CAKES & BAKES")
        Target.window2.geometry("1000x500+0+0")
        Target.window2.configure(background="white")
       
        Target.window2.grab_set() 
        Target.window2.resizable(False, False)

        title_child = Label(Target.window2, text="Kindly Fill in details to Change your Phone Number", background="white", fg="black",compound=LEFT, font=("new times roman", 18, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_labeldefined = Label(Target.window2, text="Enter Your Password", font=("time new roman", 13), background="white", fg="black").place(x=0, y=60)
        Target.phone_ = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.phone_.place(x=0, y=100)
        
        current_labeldefined = Label(Target.window2, text="Enter Your Current Phone Number", font=("time new roman", 13), fg="black", background="white").place(x=0, y=140)
        Target.current_ = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.current_.place(x=0, y=180)
        
        pass_labeldefined = Label(Target.window2, text="Enter Your New Phone Number", font=("time new roman", 13), fg="black", background="white").place(x=0, y=220)
        Target.pass_ = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.pass_.place(x=0, y=260)
        
        passcon_labeldefined = Label(Target.window2, text="Confirm Your Phone Number", font=("time new roman", 13), fg="black", background="white").place(x=0, y=300)
        Target.passcon = Entry(Target.window2, bd=5, width=20, background="white", font=("new times roman", 13))
        Target.passcon.place(x=0, y=330)
        
        Reset_button = Button(Target.window2, text="SAVE", font=("new times roman", 18, "bold"), activebackground="blue",activeforeground="white", background="blue", fg="white", cursor="hand2", command=Target.apply)
        Reset_button.place(x=400, y=430, width=140, height=30) 

        
    def apply(Target):
        Target.window.destroy()
    
    
    def Exit(Target):
        Target.window.destroy()
            

window = Tk()
obj = AdminHome(window)
window.mainloop()
