
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk,  ImageDraw
import os 
import webbrowser
import sys
import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
from validate_email import validate_email
from datetime import datetime
import random
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
class AdminLogin:
    def __init__(Target, window):
            Target.window = window
            window.geometry("1360x768")
            window.config(background="black")
            window.title("Admin LogIn Form".center(420))
            window.resizable(False, False)
            Target.feedback_icon = ImageTk.PhotoImage(file = "Pictures\\Feedbackicon.png")
            Target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
            Target.img_background = Label(Target.window, image = Target.background)
            Target.img_background.place(x=0, y=0)
            Target.RsideF = Frame(Target.window, relief=FLAT, bd=6,background="white")
            Target.RsideF.place(x=470, y=120, width=400, height=500)

            Target.RsideF_label1= Label(Target.RsideF, fg="black",text="CAKES & BAKES",font=("times new roman",21,"bold"),background= "white")
            Target.RsideF_label1.place(x=75, y=20)
            Target.RsideF_label1= Label(Target.RsideF, fg="black",text="Admin Entry",font=("times new roman",19,"bold"),background= "white")
            Target.RsideF_label1.place(x=115, y=60)
            Target.RsideF_label2= Label(Target.RsideF, fg="black",text="Enter Your Email",font=("times new roman",15,"bold"),background= "white")
            Target.RsideF_label2.place(x=10, y=100)
            Target.RsideF_label2= Label(Target.RsideF, fg="black",text="Enter Your Password",font=("times new roman",15,"bold"),background= "white")
            Target.RsideF_label2.place(x=10, y=190)
            Target.emailentrybox = Entry(Target.RsideF, background="white", fg="black",font=("times new roman",20), bd=2)
           
            Target.emailentrybox.place(x=10, y=140)
            Target.emailentrybox.insert(0,"")

            Target.passwordentrybox = Entry(Target.RsideF,show=".", background="white", fg="black",font=("times new roman",20), bd=2)
            Target.passwordentrybox.place(x=10, y=220,width=240)
            Target.passwordentrybox.insert(0,"")

           
            
            Target.Partition_label1 = Label(Target.RsideF, text="For FeedBack Click Here",  fg="black",font=("times new roman",10),background="white")
            Target.Partition_label1.place(x=1, y=350)
            Target.Partition_label3 = Label(Target.RsideF, text="Address",  fg="black",font=("times new roman",10),background="white")
            Target.Partition_label3.place(x=-1, y=405)

            Target.Partition_label2 = Label(Target.RsideF, text="NPF,o9,Block-B,Main Market,Plaza-No#2,Shop-No#3,Islamabad",  fg="black",font=("times new roman",10),background="white")
            Target.Partition_label2.place(x=-1, y=420)


            
            
            Target.rightSideBut_1 = Button(Target.RsideF,bd=0, text="Show Password?",activebackground="white",background="white",cursor="hand2")#, command=Target.show)
            Target.rightSideBut_1.place(x=280, y=230)

            Target.rightSideBut_2 = Button(Target.RsideF, bd=0,text="Forget Your Password?", activebackground="white", fg="black",font=("times new roman",10),background="white",cursor="hand2")
            Target.rightSideBut_2.place(x=10, y=250)

            Target.rightSideBut_3 = Button(Target.RsideF,bd=0, text="Sign In",font=("times new roman",20,"bold"), activebackground="white",background="blue",cursor="hand2", command=Target.signin)
            Target.rightSideBut_3.place(x=50, y=300, width=290,height=30)

           

            Target.rightSideBut_5 = Button(Target.RsideF,bd=0, image = Target.feedback_icon, activebackground="white",background="white",cursor="hand2", command=Target.feedlink)
            Target.rightSideBut_5.place(x=150, y=350)

          

            Target.rightSideBut_8 = Button(Target.window, relief=GROOVE,bd=0,text="Exit", font=("times new roman",20,"bold"),activebackground="blue",background="blue",activeforeground="blue",fg="black",cursor="hand2", command=Target.logintou)
            Target.rightSideBut_8.place(x=20, y=650)

          


            

    def feedlink(Target):
        webbrowser.open_new("http://www.gmail.com")
   
    def logintou(Target):
        import USERlogin   
    

    def signin(Target):
        confirm_entry = validate_email(Target.emailentrybox.get())
        if Target.emailentrybox.get() == "" or Target.passwordentrybox.get() == "":
            return messagebox.showerror("","Kindly Fill all the Fields. Can't LogIN")
        
        
        
        if confirm_entry == False:
            return messagebox.showerror("Invalid Email Entry. Can't LogIN")   
        else:
            with open("History2.txt", "w+") as file:
                file.write(Target.emailentrybox.get())
            Target.conn = sqlite3.connect("bakery.db")
            Target.c = Target.conn.cursor()
            Target.find_user = (
                "SELECT * FROM admin WHERE Email = ?  AND Password = ?")
            Target.c.execute(str(Target.find_user), (str(
                Target.emailentrybox.get()), str(Target.passwordentrybox.get())))
            results = (Target.c).fetchall()
            if results:
                for i in results:
                   
                    messagebox.showinfo("Wait Please.","logging-IN")
                    Target.window.destroy()
                    import HAdmin
            else:
                messagebox.showerror("","Wrong Password or Email")

    
            
    
window =Tk()
obj = AdminLogin(window)
window.mainloop()
