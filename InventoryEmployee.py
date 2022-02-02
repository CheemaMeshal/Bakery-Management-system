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

from tkinter import ttk 
from ttkthemes import ThemedTk
class InventoryEmployee:
    def __init__(target,window):
        target.window = window
        target.window.title("CAKES AND BAKES-INVENTORY".center(420))  # title for Window 
        target.window.configure(background = "white")  # background color for window 
        target.window.geometry("1360x768")
        background_color ="light yellow"
        target.background = ImageTk.PhotoImage(file="Pictures\\donuts.png") 
        target.img_background = Label(target.window, image = target.background)
        target.img_background.place(x=0, y=0)
        Frame1 = LabelFrame(target.window,bd=0,relief=GROOVE,background="light yellow")
        Frame1.place(x=0,relwidth=2,height=150)
        labell = Label(Frame1,text="CAKES & BAKES-INVENTORY", background="light yellow", font= ("new times roman",25,"bold")).place(x=400, y=25)
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
        lb_search_button=Button(target.window,text="SEARCH", bd=0, relief=GROOVE,command=target.Search_Inventory,font=("new times roman",18,"bold"),fg="black",background="dark blue")
        lb_search_button.place(x=130 ,y=260, height=50,width=150,anchor="w")
        lb_search_button=Button(target.window,text="CLEAR", bd=0, relief=GROOVE,command=target.clear_Screen,font=("new times roman",18,"bold"),fg="black",background="dark blue")
        lb_search_button.place(x=290 ,y=260, height=50, width=150,anchor="w")
        Table_Frame=Frame(target.window,bd=0, relief=RIDGE,background="light yellow")
        Table_Frame.place(x=130,y=270,width=1080,height=430)
        style=ttk.Style(Table_Frame)
        style.configure("Treeview",background="light yellow",fieldbackground="light yellow",foreground="light yellow")
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        target.Stock_table=ttk.Treeview(Table_Frame,columns=("ItemID" ,"ItemName"  , "Stock_Left"  , "Item_Price"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=target.Stock_table.yview)
        target.Stock_table.column("ItemID", width=80)
        target.Stock_table.column("ItemName", width=200)
        target.Stock_table.column("Stock_Left", width=200)
        target.Stock_table.column("Item_Price", width=300)      
       
       

        target.varr=sqlite3.connect("bakery.db")
        target.Contodb=target.varr.cursor()
        

       
      
        target.button_home=Button(target.window, relief=GROOVE,bd=0,text="HOME", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.ADMhome)
        target.button_home.place(x=20, y=170)
        target.employees=Button(target.window, relief=GROOVE,bd=0,text="SEARCH", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.ADMManageAdmin)
        target.employees.place(x=150, y=170)
        target.adminss=Button(target.window, relief=GROOVE,bd=0,text="SALES", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.ADMManageEmp)
        target.adminss.place(x=950, y=170)
        target.inventoryview=Button(target.window, relief=GROOVE,bd=0,text="INVENTORY", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.inventory)
        target.inventoryview.place(x=1120, y=170)
       
        
        target.ButtonRSF_8 = Button(target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.backto)
        target.ButtonRSF_8.place(x=370, y=170)
        
        
        target.time()
    def Search_Inventory(target):
        target.Stock_table.heading("ItemID", text="Product ID")
        target.Stock_table.heading("ItemName", text="Product Name")
        target.Stock_table.heading("Stock_Left", text="Product Left")
        target.Stock_table.heading("Item_Price", text="Product Price")
    
        target.Stock_table['show']='headings'

        target.Stock_table.pack(fill=BOTH,expand=1)
        target.Stock_table.bind("<ButtonRelease-1>",target.getcontrol)
        target.fetch_inventort_data()

    def fetch_inventort_data(target):
        try:
            target.conn=sqlite3.connect("bakery.db")
            target.Contodb=target.conn.cursor()
            target.Contodb.execute("select * from Stock")
            rows=target.Contodb.fetchall()
            if len(rows)!=0:
                    target.Stock_table.delete(*target.Stock_table.get_children())
                    for row in rows:
                            target.Stock_table.insert('',END,values=row)
                    target.conn.commit()
            target.conn.close()
        except Exception:
            return messagebox.showerror("Error","Operation Failed")

    def getcontrol(target,ev):
        cursor_row=target.Stock_table.focus()
        Content=target.Stock_table.item(cursor_row)
        row=Content['values']
        #print(row)
        target.Item_ID.set(row[0])
        target.Item_name.set(row[1])
        target.Stock_left.set(row[2])
        target.Price.set(row[3])
        

    def clear_Screen(target):
        target.Stock_table.delete(*target.Stock_table.get_children())
        target.Stock_table.heading("ItemID", text="")
        target.Stock_table.heading("ItemName", text="")
        target.Stock_table.heading("Stock_Left", text="")
        target.Stock_table.heading("Item_Price", text="")
            
        target.Stock_table['show']='headings'

    
    def backto(target):
        target.window.destroy()
        import LoginAdmin
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



    
    
    def ADMhome(target):
        target.window.destroy()
        import HEmployee
        
    def ADMManageEmp(target):
        target.window.destroy()
        import SalesEmp

    def ADMManageAdmin(target):
        target.window.destroy()
        import SearchBYemp
    
    def inventory(target):
        target.window.destroy()
        import InventoryEmployee

    
    
            

window = Tk()
obj = InventoryEmployee(window)
window.mainloop()
