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
class LOGINEMP:
    def __init__(target, window):
            target.window = window
            window.geometry("1360x768")
            window.config(background="black")
            window.title("Employee LogIn Form".center(420))
            window.resizable(False, False)
            target.feedback_icon = ImageTk.PhotoImage(file = "Pictures\\Feedbackicon.png")
            target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
            target.img_background = Label(target.window, image = target.background)
            target.img_background.place(x=0, y=0)
            target.MainFrame = Frame(target.window, relief=FLAT, bd=6,background="white")
            target.MainFrame.place(x=470, y=120, width=400, height=500)
            target.MainFrame_labelll1= Label(target.MainFrame, fg="black",text="CAKES & BAKES",font=("new times roman",21,"bold"),background= "white")
            target.MainFrame_labelll1.place(x=75, y=20)
            target.MainFrame_labelll1= Label(target.MainFrame, fg="black",text="Employee Entry",font=("new times roman",19,"bold"),background= "white")
            target.MainFrame_labelll1.place(x=115, y=60)
            target.MainFrame_labelll2= Label(target.MainFrame, fg="black",text="Enter Your Email",font=("new times roman",15,"bold"),background= "white")
            target.MainFrame_labelll2.place(x=10, y=100)
            target.MainFrame_labelll2= Label(target.MainFrame, fg="black",text="Enter Your Password",font=("new times roman",15,"bold"),background= "white")
            target.MainFrame_labelll2.place(x=10, y=190)
            target.email_entry = Entry(target.MainFrame, background="white", fg="black",font=("new times roman",20), bd=2)
            target.email_entry.place(x=10, y=140)
            target.email_entry.insert(0,"")
            target.pass_entry = Entry(target.MainFrame,show=".", background="white", fg="black",font=("new times roman",20), bd=2)
            target.pass_entry.place(x=10, y=220,width=240)
            target.pass_entry.insert(0,"")
            target.partition_labelll1 = Label(target.MainFrame, text="For FeedBack Click Here",  fg="black",font=("new times roman",10),background="white")
            target.partition_labelll1.place(x=1, y=350)
            target.partition_labelll3 = Label(target.MainFrame, text="Address",  fg="black",font=("new times roman",10),background="white")
            target.partition_labelll3.place(x=-1, y=405)

            target.partition_labelll2 = Label(target.MainFrame, text="NPF,o9,Block-B,Main Market,Plaza-No#2,Shop-No#3,Islamabad",  fg="black",font=("new times roman",10),background="white")
            target.partition_labelll2.place(x=-1, y=420)
            target.tapbutton_1 = Button(target.MainFrame,bd=0, text="Show Password?",activebackground="white",background="white",cursor="hand2")
            target.tapbutton_1.place(x=280, y=230)

            target.tapbutton_2 = Button(target.MainFrame, bd=0,text="Forget Your Password?", activebackground="white", fg="black",font=("new times roman",10),background="white",cursor="hand2")
            target.tapbutton_2.place(x=10, y=250)

            target.tapbutton_3 = Button(target.MainFrame,bd=0, text="Sign In",font=("new times roman",20,"bold"), activebackground="white",background="blue",cursor="hand2", command=target.signin)
            target.tapbutton_3.place(x=50, y=300, width=290,height=30)

            

            target.tapbutton_5 = Button(target.MainFrame,bd=0, image = target.feedback_icon, activebackground="white",background="white",cursor="hand2", command=target.feedbacklog)
            target.tapbutton_5.place(x=150, y=350)

           

            target.tapbutton_8 = Button(target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="blue",background="blue",activeforeground="blue",fg="black",cursor="hand2", command=target.backto)
            target.tapbutton_8.place(x=20, y=650)

          
    def backto(target):
        target.window.destroy()
        import USERlogin

    def feedbacklog(target):
        webbrowser.open_new("http://www.gmail.com")
   
    def signin(target):
        is_valid = validate_email(target.email_entry.get())
        if target.email_entry.get() == "" or target.pass_entry.get() == "":
            return messagebox.showerror("","Kindly Fill all the Fields. Can't LogIN")
        
       
        
        if is_valid == False:
            return messagebox.showerror("Invalid Email Entry. Can't LogIN")   
        else:
            with open("History.txt", "w+") as file:
                file.write(target.email_entry.get())
            target.conn = sqlite3.connect("bakery.db")
            target.c = target.conn.cursor()
            target.find_user = (
                "SELECT * FROM Emp WHERE Email = ?  AND Password = ?")
            target.c.execute(str(target.find_user), (str(
                target.email_entry.get()), str(target.pass_entry.get())))
            results = (target.c).fetchall()
            if results:
                for i in results:
                   
                    messagebox.showinfo("Wait Please.","logging-IN")
                    target.window.destroy()
                    import HEmployee
            else:
                messagebox.showerror("","Wrong Password or Email")

    
            
    

    

window =Tk()
obj = LOGINEMP(window)
window.mainloop()
