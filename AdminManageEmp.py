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
from email.message import EmailMessage
from ttkthemes import ThemedTk
class ManageEmp:
    def __init__(target,window):
        target.window = window
        target.window.title("CAKES AND BAKES".center(420))  
        target.window.configure(background = "white") 
        target.window.geometry("1360x768")
        background_color ="light pink"
        target.EID = StringVar()
        target.Name = StringVar()
        target.Email = StringVar()
        target.getpassword = StringVar()
        target.contact = StringVar()
        target.code = IntVar()
        target.Addresstag = StringVar()
        target.branchID = StringVar()
        target.position = StringVar()
        target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
        target.img_background = Label(target.window, image = target.background)
        target.img_background.place(x=0, y=0)
        
        Frame1 = LabelFrame(target.window,bd=0,relief=GROOVE,background="light pink")
        Frame1.place(x=0,relwidth=2,height=150)

        labell = Label(Frame1,text="CAKES & BAKES-MANAGE EMPLOYEES", background="light pink", font= ("new times roman",25,"bold")).place(x=400, y=25)
        labell = Label(Frame1,text="Time : ", background="light pink", font= ("new times roman",15,"bold")).place(x=840, y=65)

        target.labell_hour = Label(Frame1,text="12" , fg="black",background="light pink",font = ("new times roman", 15))
        target.labell_hour.place(x=900, y=65)
        
        target.labell_COLON = Label(Frame1,text=":" , fg="black",background="light pink",font = ("new times roman", 15))
        target.labell_COLON.place(x=925, y=65)
       
       
        target.labell_min = Label(Frame1,text="12" , fg="black",background="light pink",font = ("new times roman", 15))
        target.labell_min.place(x=940, y=65)
       
        target.labell_COLON = Label(Frame1,text=":" ,fg="black" ,background="light pink",font = ("new times roman",15))
        target.labell_COLON.place(x=965, y=65)
       
        target.labell_sec = Label(Frame1,text="12" ,fg="black", background="light pink",font = ("new times roman",15))
        target.labell_sec.place(x=980, y=65)
        

        target.labell_abv = Label(Frame1,text="AM" ,fg="black",background="light pink", font = ("new times roman",15))
        target.labell_abv.place(x=1005, y=65)
       




        target.Framemov1 = Frame(target.window,bd=0,relief=RAISED,background="light pink")
        target.Framemov1.place(x=443,y=180,width=500,height=480 )


        labell_Framemov11= Label(target.Framemov1,text="Kindly Add the following Information",font=("new times roman",17,"bold"),fg="black",background="light pink")
        labell_Framemov11.place(x=0,y=0)

        labellID_roll=Label(target.Framemov1,text="Emp ID",fg="black",background="light pink",font=("new times roman",13,"bold"))
        labellID_roll.place(x=0,y=50,anchor="w")
        txtID_roll=Entry(target.Framemov1, width=17, textvariable=target.EID,font=("new times roman",13,"bold"),bd=0,relief=GROOVE)
        txtID_roll.place(x=100,y=50,anchor="w")
        button_Add=Button(target.Framemov1,text="ADD Employee",background="blue",fg="black",bd=0,width=13,font=("new times roman",13,"bold"),command=target.addEMP).place(x=185, y=380, anchor="w")
        button_update2 = Button(target.Framemov1,relief=GROOVE,width=18,background="blue",fg="black", font=("new times roman",13,"bold"),bd=0,text="Update Information",command=target.updateEMP).place(x=160, y=420, anchor="w")  
        button_Delete = Button(target.Framemov1,relief=GROOVE, width=13,fg="black",background="blue",font=("new times roman",13,"bold"),bd=0,text="Delete Employee",command=target.deleteEMP).place(x=185, y=460, anchor="w")  
        button_Clear = Button(target.Framemov1,relief=GROOVE, width=8,fg="black",background="blue",font=("new times roman",13,"bold"),bd=0,text="Clear All",command=target.clearScreen).place(x=390, y=60, anchor="w")         
        labell_roll=Label(target.Framemov1,text="Name",font=("new times roman",13,"bold"),background="light pink")
        labell_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(target.Framemov1,  width=17, textvariable=target.Name,font=("new times roman",13,"bold"),bd=0,relief=GROOVE)
        txt_roll.place(x=100,y=90,anchor="w")
        labell_roll=Label(target.Framemov1,text="E-mail",background="light pink",fg="black",font=("new times roman",13,"bold"))
        labell_roll.place(x=0,y=130,anchor="w")
        txt_roll=Entry(target.Framemov1, width=17,textvariable=target.Email, font=("new times roman",13,"bold"),bd=0,relief=GROOVE)
        txt_roll.place(x=100,y=130,anchor="w")
        labell_roll=Label(target.Framemov1,text="Password",background="light pink",fg="black",font=("new times roman",13,"bold"))
        labell_roll.place(x=0,y=170,anchor="w")
        txt_roll=Entry(target.Framemov1, width=17,textvariable=target.getpassword, font=("new times roman",13,"bold"),bd=0,relief=GROOVE)
        txt_roll.place(x=100,y=170,anchor="w")
        labell_roll=Label(target.Framemov1,text="Phone No",background="light pink",fg="black",font=("new times roman",13,"bold"))
        labell_roll.place(x=0, y=210, anchor="w")
        target.code.set(0)
        txt_roll=Entry(target.Framemov1, width=17, textvariable=target.contact, font=("new times roman",13,"bold"),bd=0,relief=GROOVE)
        txt_roll.place(x=100,y=210,anchor="w")
        lb_gender=Label(target.Framemov1,text="Position", font=("new times roman",13,"bold"),background="light pink",fg="black")
        lb_gender.place(x=0, y=250, anchor="w")
        combo_gender=Entry(target.Framemov1,textvariable=target.position, width=17, font=("new times roman",13,"bold"),relief=GROOVE)
       
        combo_gender.place(x=100, y=250, anchor="w")
        lb_zone=Label(target.Framemov1,text="Area Code", font=("new times roman",13,"bold"),background="light pink",fg="black")
        lb_zone.place(x=0,y=290, anchor="w")
        combo_zone=Entry(target.Framemov1, textvariable=target.Addresstag,width=17, font=("new times roman",13,"bold"),relief=GROOVE)

        combo_zone.place(x=100,y=290, anchor="w")
        
        lb_Branch=Label(target.Framemov1,text="BranchID", font=("new times roman",13,"bold"),background="light pink",fg="black")
        lb_Branch.place(x=0, y=330, anchor="w")
        combo_Branch=Entry(target.Framemov1, width=17,textvariable=target.branchID, font=("new times roman",13,"bold"),relief=GROOVE)
        combo_Branch.place(x=100, y=330, anchor="w")
        target.button_home=Button(target.window, relief=GROOVE,bd=0,text="HOME", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=target.admhome)
        target.button_home.place(x=20, y=170)
        target.employees=Button(target.window, relief=GROOVE,bd=0,text="EMPLOYEES", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=target.admManageEmp)
        target.employees.place(x=150, y=170)
        target.adminss=Button(target.window, relief=GROOVE,bd=0,text="ADMINS", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=target.admManageAdmin)
        target.adminss.place(x=950, y=170)
        target.inventoryview=Button(target.window, relief=GROOVE,bd=0,text="INVENTORY", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=target.inventory)
        target.inventoryview.place(x=1120, y=170)
       
        
        target.ButtonRSF_8 = Button(target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="light pink",background="light pink",activeforeground="light pink",fg="black",cursor="hand2", command=target.backto)
        target.ButtonRSF_8.place(x=370, y=170)
        target.time()


    def backto(target):
        target.window.destroy()
        #import logine
    def addEMP(target):
        if target.Name.get()=="" and target.getpassword.get()=="" and target.Email.get()=="" and target.contact.get()=="" and target.code.get()==0 and target.position.get()=="" and target.Addresstag.get()=="" and target.branchID.get()=="" :
            return messagebox.showerror("Opertion Failed","Incomplete Form")
        else:
            if str(target.position.get()) == "Cashier":
                target.var2 = str(region_code_for_country_code(target.code.get()))
                target.varrr=sqlite3.varrrect("bakery.db")
                target.c=target.varrr.cursor()
                target.c.execute("CREATE TABLE IF NOT EXISTS Emp(EmpID TEXT PRIMARY KEY ,EmpName TEXT, Email TEXT UNIQUE , Country_Code TEXT , Country TEXT, Phone_No TEXT UNIQUE, Password TEXT, FOREIGN KEY (Addresstag) REFERENCES Zone (Zone_ID),FOREIGN KEY (BranchID) REFERENCES Branch (Branch_ID) )")
                target.find_user = ("SELECT * FROM Emp WHERE Email= ?  or Phone_No = ?")
                target.c.execute(str(target.find_user),(target.Email.get(),target.contact.get()))
                results = (target.c).fetchall()
                if results:
                    messagebox.showerror("Error","Email or Contact  is already Used")
                else:
                    try:
                        target.c.execute("INSERT INTO Emp (EmpID, EmpName, Email, Country_Code, Country, Phone_No, Password, Addresstag, BranchID  ) VALUES (?,?,?,?,?,?,?,?,?)",
                        (target.EID.get(),target.Name.get(),str(target.Email.get()),str(target.code.get()),target.var2,target.contact.get(),target.getpassword.get(),target.Addresstag.get(),target.branchID.get()))
                        target.varrr.commit()
                        target.c.close()
                        target.varrr.close()
                        messagebox.showinfo("Operation Successfull","ADDED EMPLOYEE")
                        target.clear()
                    except Exception:
                        return messagebox.showerror("Operation Failed","System Failed, Try Again Later")
                        target.clear()        
            else:
                target.var2 = str(region_code_for_country_code(target.code.get()))
                target.varrr=sqlite3.varrrect("bakery.db")
                target.c=target.varrr.cursor()
                target.c.execute("CREATE TABLE IF NOT EXISTS Bakers(Baker_ID TEXT PRIMARY KEY ,Name TEXT, Email TEXT UNIQUE , Country_Code TEXT , Country TEXT, Phone_No TEXT UNIQUE, FOREIGN KEY (Zone_ID) REFERENCES Zone (Zone_ID),FOREIGN KEY (BranchID) REFERENCES Branch (Branch_ID) )")
                target.find_user = ("SELECT * FROM Bakers WHERE Email= ?  or Phone_No = ?")
                target.c.execute(str(target.find_user),(target.Email.get(),target.contact.get()))
                results = (target.c).fetchall()
                if results:
                    messagebox.showerror("Operation Failed","Cant Fetch Data")
                else:
                    try:
                        target.c.execute("INSERT INTO Bakers (Baker_ID, Name, Email, Country_Code, Country, Phone_No, Zone_ID, BranchID  ) VALUES (?,?,?,?,?,?,?,?)",
                        (target.EID.get(),target.Name.get(),str(target.Email.get()),str(target.code.get()),target.var2,target.contact.get(),target.Addresstag.get(),target.branchID.get()))
                        target.varrr.commit()
                        target.c.close()
                        target.varrr.close()
                        messagebox.showinfo("Successfull","Employee Added Data")
                        target.clear()
                    except Exception:
                        return messagebox.showerror("Operation Failed","System Down ")
                        target.clear()        

    def updateEMP(target):
        import AdminManageEmp
        
    
    def deleteEMP(target):
       import AdminManageEmp

    def clearScreen(target):
        target.Name.set("")
        target.Email.set("")
        target.getpassword.set("")
        target.contact.set("")
        target.code.set(0)
        target.Addresstag.set("")
        target.branchID.set("")
        target.position.set("")
        target.EID.set("")
        
    def time(target):
        target.h = str(time.strftime("%H"))
        target.m = str(time.strftime("%M"))
        target.s = str(time.strftime("%S"))

        if int(target.h)>=12 and int(target.h)<15 and int(target.m)>0:
            target.labell_abv.config(text="PM")

        if int(target.h)>=15 and int(target.h)<20 and int(target.m)>0:
            target.labell_abv.config(text="PM")
        
        if int(target.h)>=20 and int(target.h)<24 and int(target.m)>0:
            target.labell_abv.config(text="PM")

        if int(target.h)>12 and int(target.h)<15 and int(target.m)>0:
            target.labell_abv.config(text="PM")

        if int(target.h)>0 and int(target.h)<12 and int(target.m)>0:
            target.labell_abv.config(text="AM")

         
        target.labell_hour.config(text = target.h)
        target.labell_min.config(text = target.m)
        target.labell_sec.config(text = target.s)
        target.labell_hour.after(200,target.time)
    def admhome(target):
        target.window.destroy()
        import HAdmin

    def admManageEmp(target):
        target.window.destroy()
        import AdminManageEmp

    def admManageAdmin(target):
        target.window.destroy()
        import AdminManageEmp
    
    def inventory(target):
        target.window.destroy()
        import InventoryAdmin

   
            

window = Tk()
obj = ManageEmp(window)
window.mainloop()
