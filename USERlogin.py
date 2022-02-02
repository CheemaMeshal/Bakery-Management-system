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
class LogInuser:
    def __init__(target, window):
            target.window = window
            window.geometry("1360x768+0+0")
            window.config(background="#6ACD32")
            window.title("User Login".center(420))
            window.resizable(False, False)
           
            target.feedback_icon = ImageTk.PhotoImage(file = "Pictures\\Feedbackicon.png")
            target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
           
            target.img_background = Label(target.window, image = target.background)
            target.img_background.place(x=0, y=0)
            target.pass_l = StringVar()
            target.pass_l1 = StringVar()
            target.MainPframe = Frame(target.window, relief=FLAT, background= "white")
            target.MainPframe.place(x=460, y=100, width=500, height=500)
            target.name_labelll = Label(target.MainPframe,text="CAKES AND BAKES",anchor="w",font=("new times roman",20),background="white")
            target.name_labelll.place(x=135,y=30)
            target.name_labelll = Label(target.MainPframe,text="LOG IN-USER",anchor="w",font=("new times roman",17),background="white")
            target.name_labelll.place(x=180,y=80)
            target.name_labelll = Label(target.MainPframe,text="Enter Your Email",anchor="w",font=("new times roman",15),background="white")
            target.name_labelll.place(x=30,y=150)
            target.email_entry = Entry(target.MainPframe,bd=3,font=("new times roman",15,"bold"),background="white", fg="black")
            target.email_entry.place(x=30,y=180, width= 250)

            target.pass_labelll = Label(target.MainPframe, text="Enter Your Password",anchor="w",font=("new times roman",12),background="white")
            target.pass_labelll.place(x=30,y=210)
            target.pass_entry= Entry(target.MainPframe,show=".",bd=3,font=("new times roman",15,"bold"),background="white", fg="black")
            target.pass_entry.place(x=30,y=240, width= 200)

           

        

            target.ButtonRSF_1 = Button(target.MainPframe,bd=0, text="Sign In",font=("new times roman",20,"bold"), activebackground="white",background="blue",cursor="hand2", command=target.signin)
            target.ButtonRSF_1.place(x=200, y=300, height=30,width=130)
            target.partition_labelll1 = Label(target.MainPframe, text="For FeedBack Click Here",  fg="black",font=("new times roman",10),background="white")
            target.partition_labelll1.place(x=0, y=400)
            target.ButtonRSF_5 = Button(target.MainPframe,bd=0, image = target.feedback_icon, activebackground="white",background="white",cursor="hand2", command=target.feedbacklink)
            target.ButtonRSF_5.place(x=90, y=420)
            target.partition_labelll2 = Label(target.MainPframe, text="NPF,o9,Block-B,Main Market,Plaza-No#2,Shop-No#3,Islamabad",  fg="black",font=("new times roman",10),background="white")
            target.partition_labelll2.place(x=0, y=480)

            

            target.ButtonRF_7 = Button(target.MainPframe,bd=5, font=("iimes new roman",10,"bold"),text="Sign In As Employee",fg="black",borderwidth=0,background="blue",cursor="hand2", command=target.employeelogin)
            target.ButtonRF_7.place(x=180, y=340, height=30,width=160)
            target.ButtonRF_8 = Button(target.MainPframe,bd=5, font=("iimes new roman",10,"bold"),text="Sign In As Admin",fg="black",borderwidth=0,background="blue",cursor="hand2", command=target.adminlogin)
            target.ButtonRF_8.place(x=180, y=380, height=30,width=160)
           

    def employeelogin(target):
        target.window.destroy()
        import loginEmployee

    def adminlogin(target):
        target.window.destroy()
        import LoginAdmin

    def feedbacklink(target):
        webbrowser.open_new("http://www.gmail.com")
    
    def signin(target):
        is_valid = validate_email(target.email_entry.get())
        if target.email_entry.get() == "" or target.pass_entry.get() == "":
            return messagebox.showerror("","Kindly Fill all the Fields. Can't LogIN")
        
        
        
        if is_valid == False:
            return messagebox.showerror("Invalid Email Entry. Can't LogIN")   
        else:
            with open("History2.txt", "w+") as file:
                file.write(target.email_entry.get())
            target.conn = sqlite3.connect("bakery.db")
            target.c = target.conn.cursor()
            target.find_user = (
                "SELECT * FROM user WHERE Email = ?  AND Password = ?")
            target.c.execute(str(target.find_user), (str(
                target.email_entry.get()), str(target.pass_entry.get())))
            results = (target.c).fetchall()
            if results:
                for i in results:
                    #messagebox.showinfo("Success","Successfully Logined")
                    messagebox.showinfo("Wait Please.","logging-IN")
                    target.window.destroy()
                    import UserBuyInter
            else:
                messagebox.showerror("","Wrong Password or Email")
   
                

    
    

window =Tk()
obj = LogInuser(window)
window.mainloop()
