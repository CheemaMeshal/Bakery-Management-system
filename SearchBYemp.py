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
class SearchBILLe:
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

        labell = Label(Frame1,text="CAKES & BAKES-EMPLOYEE DASHBOARD", background="light yellow", font= ("new times roman",25,"bold")).place(x=400, y=25)
        labell = Label(Frame1,text="Time : ", background="light yellow", font= ("new times roman",15,"bold")).place(x=840, y=65)

        target.labell_hour = Label(Frame1,text="12" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labell_hour.place(x=900, y=65)
        
        target.labell_COLON = Label(Frame1,text=":" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labell_COLON.place(x=925, y=65)
       
       
        target.labell_min = Label(Frame1,text="12" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labell_min.place(x=940, y=65)
       
        target.labell_COLON = Label(Frame1,text=":" ,fg="black" ,background="light yellow",font = ("new times roman",15))
        target.labell_COLON.place(x=965, y=65)
       
        target.labell_sec = Label(Frame1,text="12" ,fg="black", background="light yellow",font = ("new times roman",15))
        target.labell_sec.place(x=980, y=65)
        

        target.labell_abv = Label(Frame1,text="AM" ,fg="black",background="light yellow", font = ("new times roman",15))
        target.labell_abv.place(x=1005, y=65)
        target.searchby=StringVar()
        target.searchval=StringVar()
        target.button_home=Button(target.window, relief=GROOVE,bd=0,text="HOME", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.homeEMP)
        target.button_home.place(x=20, y=170)
        target.employees=Button(target.window, relief=GROOVE,bd=0,text="SEARCH PRODUCTS", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.searchp)
        target.employees.place(x=150, y=170)
        target.adminss=Button(target.window, relief=GROOVE,bd=0,text="SALES", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.salesp)
        target.adminss.place(x=950, y=170)
        target.inventoryview=Button(target.window, relief=GROOVE,bd=0,text="INVENTORY", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.inventory)
        target.inventoryview.place(x=1120, y=170)
       
        
        target.ButtonRSF_8 = Button(target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.backto)
        target.ButtonRSF_8.place(x=10, y=650)



        
        lb_search=Label(target.window,text="Search By", font=("new times roman",18,"bold"),fg="black",background="blue")
        lb_search.place(x=170 ,y=305, anchor="w")
        combo_search=ttk.Combobox(target.window, textvariable=target.searchby,width=13, font=("new times roman",16,"bold"),state='readonly')
        combo_search['values']=("Bill_No")
        combo_search.place(x=285, y=305, anchor="w")

        target.search1 = Entry(target.window, bd=0,textvariable=target.searchval, background="white", font=("new times roman", 16))
        target.search1.place(x=680, y=290,width=150, height=40)

       
        
        
        lb_search_button=Button(target.window,text="SEARCH", bd=0, relief=GROOVE,command=target.searchPRODUCT,font=("new times roman",16,"bold"),fg="black",background="blue")
        lb_search_button.place(x=500 ,y=305, height=40,width=150,anchor="w")
        
        lb_search_button=Button(target.window,text="Clear Result", bd=0, relief=GROOVE,command=target.clear_screen,font=("new times roman",16,"bold"),fg="black",background="blue")
        lb_search_button.place(x=900,y=305, height=40, width=150,anchor="w")

        Table_Frame=Frame(target.window,bd=0, relief=RIDGE,background="black")
        Table_Frame.place(x=170,y=320,width=1080,height=450)
        style=ttk.Style(Table_Frame)
        style.configure("Treeview",background="black",fieldbackground="black",foreground="light yellow")


        
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        target.FetchFomTable=ttk.Treeview(Table_Frame,columns=("Bill_No","OrderNo","OrderDate","OrderTime","Customer_ID"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=target.FetchFomTable.yview)
    
        
        target.FetchFomTable.column("Bill_No", width=80)
        target.FetchFomTable.column("OrderNo", width=100)
        target.FetchFomTable.column("OrderDate", width=100)
        target.FetchFomTable.column("OrderTime",  width=100)     
        target.FetchFomTable.column("Customer_ID", width=100)
  
  
        target.FetchFomTable.bind("<ButtonRelease-1>",target.getcursor)
        
        target.fetch_data()
        target.time()

    def searchPRODUCT(target):
        target.FetchFomTable.heading("Bill_No", text="Bill_No")
        target.FetchFomTable.heading("OrderNo", text="OrderNo")
        target.FetchFomTable.heading("OrderDate", text="OrderDate")
        target.FetchFomTable.heading("OrderTime", text="OrderTime")
        target.FetchFomTable.heading("Customer_ID", text="Customer_ID")
        target.FetchFomTable['show']='headings'
  
        target.FetchFomTable.pack(fill=BOTH,expand=1)
        target.FetchFomTable.bind("<ButtonRelease-1>",target.getcursor)
        target.search_data()

    def search_data(target):
        if target.searchby.get()=="" and target.searchval.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if target.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if target.searchval.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            
            if target.searchby.get() == "Bill_No":
                try:
                    target.conn=sqlite3.connect("bakery.db")
                    target.c=target.conn.cursor()
                    target.c.execute("select * from Order_Hist where Bill_No="+target.searchval.get())
                    rows=target.c.fetchall()
                    if len(rows)!=0:
                            target.FetchFomTable.delete(*target.FetchFomTable.get_children())
                            for row in rows:
                                    target.FetchFomTable.insert('',END,values=row)
                            target.conn.commit()
                            target.conn.close()
                    else:
                        return messagebox.showerror("Error","Bill No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                #target.conn.close()
            if target.searchby.get() == "OrderNo":
                try:
                    target.conn=sqlite3.connect("bakery.db")
                    target.c=target.conn.cursor()
                    target.c.execute("select * from Order_Hist where OrderNo="+target.searchval.get())
                    rows=target.c.fetchall()
                    if len(rows)!=0:
                            target.FetchFomTable.delete(*target.FetchFomTable.get_children())
                            for row in rows:
                                    target.FetchFomTable.insert('',END,values=row)
                            target.conn.commit()
                            target.conn.close()

                    else:
                        return messagebox.showerror("Error","Bill No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
            

    def fetch_data(target):
        target.conn=sqlite3.connect("bakery.db")
        target.c=target.conn.cursor()
        target.c.execute("select * from Order_Hist")
        rows=target.c.fetchall()
        if len(rows)!=0:
                target.FetchFomTable.delete(*target.FetchFomTable.get_children())
                for row in rows:
                        target.FetchFomTable.insert('',END,values=row)
                target.conn.commit()
        target.conn.close()

    def getcursor(target,ev):
        cursor_row=target.FetchFomTable.focus()
        Content=target.FetchFomTable.item(cursor_row)
        row=Content['values']
        #print(row)
        target.Item_ID.set(row[0])
        target.Item_name.set(row[1])
        target.Stock_left.set(row[2])
        target.Price.set(row[3])
        

    def clear_screen(target):
        target.FetchFomTable.delete(*target.FetchFomTable.get_children())
        target.FetchFomTable.heading("ItemID", text="")
        target.FetchFomTable.heading("Item_name", text="")
        target.FetchFomTable.heading("Stock_Left", text="")
        target.FetchFomTable.heading("Item_Price", text="")
            
        target.FetchFomTable['show']='headings'

    

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



    
    
    def homeEMP(target):
        target.window.destroy()
        import HEmployee

    def searchp(target):
        target.window.destroy()
        import SearchBYemp

    def salesp(target):
        target.window.destroy()
        import SalesEmp

    def inventory(target):
        target.window.destroy()
        import InventoryEmployee
    def backto(target):
        target.window.destroy()
        import HEmployee
    
            
    

    def Exit(target):
        target.window.destroy()
            

window = Tk()
obj = SearchBILLe(window)
window.mainloop()
