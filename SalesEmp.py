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
import tempfile, os
import re
class BuYuser:
    def __init__(target,window):
        target.window = window
        target.window.title("DayFresh AND BAKES-Employee-ONLINE".center(420))  
        target.window.configure(background = "white")  
        target.window.geometry("1360x768")
        background_color ="light yellow"
        target.background = ImageTk.PhotoImage(file="Pictures\\white.jpg") 
        target.img_background = Label(target.window, image = target.background)
        target.img_background.place(x=0, y=0)
        F1 = LabelFrame(target.window,bd=0,relief=GROOVE,background="light yellow")
        F1.place(x=0,relwidth=2,height=150)

        labelll = Label(F1,text="MANAGE SALES-EMPLOYEE", background="light yellow", font= ("new times roman",25,"bold")).place(x=400, y=25)
        labelll = Label(F1,text="Time : ", background="light yellow", font= ("new times roman",15,"bold")).place(x=840, y=65)

        target.labelll_hour = Label(F1,text="12" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labelll_hour.place(x=900, y=65)
        
        target.labelll_COLON = Label(F1,text=":" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labelll_COLON.place(x=925, y=65)
       
       
        target.labelll_min = Label(F1,text="12" , fg="black",background="light yellow",font = ("new times roman", 15))
        target.labelll_min.place(x=940, y=65)
       
        target.labelll_COLON = Label(F1,text=":" ,fg="black" ,background="light yellow",font = ("new times roman",15))
        target.labelll_COLON.place(x=965, y=65)
       
        target.labelll_sec = Label(F1,text="12" ,fg="black", background="light yellow",font = ("new times roman",15))
        target.labelll_sec.place(x=980, y=65)
        

        target.labelll_abv = Label(F1,text="AM" ,fg="black",background="light yellow", font = ("new times roman",15))
        target.labelll_abv.place(x=1005, y=65)
                
        target.icecream=StringVar()
        target.milo=StringVar()
        target.muffins=StringVar()
        target.DayFresh=StringVar()
        target.cupcakes=StringVar()
        target.mineralWater=StringVar()
        
        
        
        target.Chips=StringVar()
        target.Butter=StringVar()
        target.milk=StringVar()
        target.p_cake=StringVar()
        target.choc_cake=StringVar()
        target.bread=StringVar()
        
        
        
        target.Donuts=StringVar()
        target.biscuits=StringVar()
        target.coke=StringVar()
        target.yogurt=StringVar()
        target.eggs=StringVar()
        target.sprite=StringVar()
        
        
        target.sweetprices=StringVar()
        target.everydays_price=StringVar()
        target.soft_drink_price=StringVar()
        
        target.cake_tax=StringVar()
        target.icecream_tax=StringVar()
        target.soft_drink_tax=StringVar()
        
        
        
        target.c_name=StringVar()
        target.c_phno=StringVar()
        target.bill_no=StringVar()
        target.search_bill=StringVar()
        x=random.randint(1000,99999)
        target.bill_no.set(str(x))
        target.sum_bill=StringVar()
        



        
        cname_labelll=Label(target.window,text="Fill In Your Details", background="white",fg="black",font=("new times roman",15, "bold"))
        cname_labelll.place(x=0,y=150)
        cname_labelll=Label(target.window,text="Enter Your Name ",background="white", fg="black",font=("new times roman",13, "bold"))
        cname_labelll.place(x=0,y=185)
        cname_txt=Entry(target.window,width = 15, textvariable=target.c_name,font="arial 15",bd=4, relief=SUNKEN)
        cname_txt.place(x=0,y=220)
        



        

        cphn_labelll=Label(target.window,text="Enter your Phone No.",background="white", fg="black",font=("new times roman",13, "bold"))
        cphn_labelll.place(x=0,y=265)
        cphn_txt=Entry(target.window,width = 15, textvariable=target.c_phno, font="arial 15",bd=4, relief=SUNKEN)
        cphn_txt.place(x=0,y=305)
        cbill_labelll=Label(target.window,text="Enter Your Bill Number",background="white", fg="black",font=("new times roman",15, "bold"))
        cbill_labelll.place(x=0,y=345)
        cbill_txt=Entry(target.window,width = 15, textvariable=target.search_bill, font="arial 15",bd=4, relief=SUNKEN)
        cbill_txt.place(x=0,y=385)
        bill_button=Button(target.window, text="SEARCH", command=target.find, width=10,bd=4,font="arial 12 bold", cursor="hand2",background="blue")
        bill_button.place(x=15,y=435)
        target.ButtonRSF_8 = Button(target.window, relief=GROOVE,bd=0,text="Exit", font=("new times roman",20,"bold"),activebackground="light yellow",background="light yellow",activeforeground="light yellow",fg="black",cursor="hand2", command=target.Exit)
        target.ButtonRSF_8.place(x=15, y=600)
        

        
        Sweets=Label(target.window, text="SWEETS CORNER",font=("new times roman",19,"bold"),background="light yellow",fg="black")
        Sweets.place(x=260,y=170)

        c1_labelll=Label(target.window, text="Donuts",font=("new times roman",15,"bold"),background="white",fg="black")
        c1_labelll.place(x=230,y=210)
        c1=Entry(target.window,width=5, textvariable=target.icecream,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c1.place(x=450,y=210)
  
        c2_labelll=Label(target.window, text="Ice-Cream",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=230,y=250)
        c2=Entry(target.window,width=5, textvariable=target.milo,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=450,y=250)

        c2_labelll=Label(target.window, text="Muffins",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=230,y=290)
        c2=Entry(target.window,width=5, textvariable=target.muffins,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=450,y=290)

        c2_labelll=Label(target.window, text="CupDayFresh",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=230,y=330)
        c2=Entry(target.window,width=5, textvariable=target.DayFresh,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=450,y=330)

        c2_labelll=Label(target.window, text="Chocolate Cake",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=230,y=370)
        c2=Entry(target.window,width=5, textvariable=target.cupcakes,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=450,y=370)

        c2_labelll=Label(target.window, text="PineApple Cake",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=230,y=410)
        c2=Entry(target.window,width=5, textvariable=target.mineralWater,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=450,y=410)


        
        Sweets=Label(target.window, text="DRINKS CORNER",font=("new times roman",19,"bold"),background="light yellow",fg="black")
        Sweets.place(x=580,y=170)

        c1_labelll=Label(target.window, text="Milk",font=("new times roman",15,"bold"),background="white",fg="black")
        c1_labelll.place(x=550,y=210)
        c1=Entry(target.window,width=5, textvariable=target.Chips,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c1.place(x=770,y=210)
  
        c2_labelll=Label(target.window, text="Mineral Water",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=550,y=250)
        c2=Entry(target.window,width=5, textvariable=target.Butter,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=770,y=250)

        c2_labelll=Label(target.window, text="Coke",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=550,y=290)
        c2=Entry(target.window,width=5, textvariable=target.milk,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=770,y=290)

        c2_labelll=Label(target.window, text="Sprite",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=550,y=330)
        c2=Entry(target.window,width=5, textvariable=target.p_cake,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=770,y=330)

        c2_labelll=Label(target.window, text="Milo",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=550,y=370)
        c2=Entry(target.window,width=5, textvariable=target.bread,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=770,y=370)

        c2_labelll=Label(target.window, text="Day Fresh",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=550,y=410)
        c2=Entry(target.window,width=5, textvariable=target.bread,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=770,y=410)


        Sweets=Label(target.window, text="EVERYDAY CORNER",font=("new times roman",19,"bold"),background="light yellow",fg="black")
        Sweets.place(x=860,y=170)

        c1_labelll=Label(target.window, text="muffins",font=("new times roman",15,"bold"),background="white",fg="black")
        c1_labelll.place(x=850,y=210)
        c1=Entry(target.window,width=5, textvariable=target.Donuts,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c1.place(x=1090,y=210)
  
        c2_labelll=Label(target.window, text="Eggs",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=850,y=250)
        c2=Entry(target.window,width=5, textvariable=target.biscuits,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=1090,y=250)

        c2_labelll=Label(target.window, text="Biscuits",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=850,y=290)
        c2=Entry(target.window,width=5, textvariable=target.coke,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=1090,y=290)

        c2_labelll=Label(target.window, text="Yougurt",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=850,y=330)
        c2=Entry(target.window,width=5, textvariable=target.yogurt,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=1090,y=330)

        c2_labelll=Label(target.window, text="Chips",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=850,y=370)
        c2=Entry(target.window,width=5, textvariable=target.eggs,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=1090,y=370)

        c2_labelll=Label(target.window, text="Butter",font=("new times roman",15,"bold"),background="white",fg="black")
        c2_labelll.place(x=850,y=410)
        c2=Entry(target.window,width=5, textvariable=target.sprite,font=("new times roman",15,"bold"),bd=2,relief=SUNKEN)  
        c2.place(x=1090,y=410)


       
        


        Frame8=Frame(target.window, bd=10, relief=GROOVE)
        Frame8.place(x=970,y=480,width=350, height=280)
        bill_title=Label(Frame8,text="RECEIPT",font="arial 15 bold",bd=0,background="light yellow",relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(Frame8, orient=VERTICAL)
        target.txtarea=Text(Frame8,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=target.txtarea.yview)
        target.txtarea.pack(fill=BOTH,expand=1)
        


        Frame9=LabelFrame(target.window, bd=0, relief=GROOVE, text="Your Bill",font=("new times roman",15,"bold"),fg="black",background="white")
        Frame9.place(x=190,y=480,width=650, height=140)

        m1_labelll=Label(Frame9,text="sum Sweets Price ",background="white", fg="black",font=("new times roman", 14, "bold")).grid(row=0,column=0,pady=1,sticky="w")
        m1_txt=Entry(Frame9,width=18, textvariable=target.sweetprices, font="arial 10 bold",bd=3, relief=SUNKEN).grid(row=0,column=1,pady=1)
        
        m2_labelll=Label(Frame9,text="sum Drinks Price",background="white", fg="black",font=("new times roman", 14, "bold")).grid(row=1,column=0,pady=1,sticky="w")
        m2_txt=Entry(Frame9,width=18, textvariable=target.everydays_price, font="arial 10 bold",bd=3, relief=SUNKEN).grid(row=1,column=1,pady=1)
        
        m3_labelll=Label(Frame9,text="sum EveryDays Price",background="white", fg="black",font=("new times roman", 14, "bold")).grid(row=2,column=0,pady=1,sticky="w")
        m3_txt=Entry(Frame9,width=18, textvariable=target.soft_drink_price, font="arial 10 bold",bd=3, relief=SUNKEN).grid(row=2,column=1,pady=1)
        
        c1_labelll=Label(Frame9,text="Tax On Sweets",background="white", fg="black",font=("new times roman", 14, "bold")).grid(row=0,column=2,pady=1,sticky="w")
        c1_txt=Entry(Frame9,width=18, textvariable=target.cake_tax, font="arial 10 bold",bd=3, relief=SUNKEN).grid(row=0,column=3,pady=1)
        
        c2_labelll=Label(Frame9,text="Tax On Drinks",background="white", fg="black",font=("new times roman", 14, "bold")).grid(row=1,column=2,pady=1,sticky="w")
        c2_txt=Entry(Frame9,width=18, textvariable=target.icecream_tax, font="arial 10 bold",bd=3, relief=SUNKEN).grid(row=1,column=3,pady=1)
        
        c3_labelll=Label(Frame9,text="Tax On EveryDays",background="white", fg="black",font=("new times roman", 14, "bold")).grid(row=2,column=2,pady=1,sticky="w")
        c3_txt=Entry(Frame9,width=18, textvariable=target.soft_drink_tax, font="arial 10 bold",bd=3, relief=SUNKEN).grid(row=2,column=3,pady=1)
       

        
        
        sum_button=Button(target.window, command=target.sum, text="sum", background="blue",fg="black",activebackground="cadetblue",activeforeground="white",pady=15,width=10,bd=2, font="arial 11 bold")
        sum_button.place(x=1190,y=200)
        GBill_button=Button(target.window, command=target.sum_bill, text="BILL", background="blue",fg="black",pady=15,width=10,bd=2, font="arial 11 bold")
        GBill_button.place(x=1190,y=280)
        Clear_button=Button(target.window, text="Clear",command=target.clear_data, background="blue",fg="black",pady=15,width=10,bd=2, font="arial 11 bold")
        Clear_button.place(x=1190,y=360)
        
        
        target.icecream.set(0)
        target.milo.set(0)
        target.muffins.set(0)
        target.DayFresh.set(0)
        target.cupcakes.set(0)
        target.mineralWater.set(0)
        
       
        
        target.Chips.set(0)
        target.Butter.set(0)
        target.milk.set(0)
        target.p_cake.set(0)
        target.choc_cake.set(0)
        target.bread.set(0)
        
        
        
        target.Donuts.set(0)
        target.biscuits.set(0)
        target.coke.set(0)
        target.yogurt.set(0)
        target.eggs.set(0)
        target.sprite.set(0)
        
        target.time()
        
    def sum(target):
        if len(target.c_phno.get())<10 :
            return messagebox.showerror("Error","Invalid Contact")
        
        if len(target.c_phno.get())>15 :
            return messagebox.showerror("Error","Invalid Contact")

        try:
            tmp=target.c_phno.get()                
            int(tmp)                
        except ValueError:
            return messagebox.showinfo('Error','Contact must be integer')

        if target.c_name.get()=="" or str(target.c_phno.get())=="":
                messagebox.showerror("Error","Customer details are must!!")

        else:
            target.c_s_p=int(target.icecream.get())*120
            target.c_fc_p=int(target.milo.get())*312
            target.c_fw_p=int(target.cupcakes.get())*45
            target.c_hs_p=int(target.muffins.get())*35
            target.c_hg_p=int(target.DayFresh.get())*750
            target.c_bl_p=int(target.mineralWater.get())*151

            target.g_r_p=int(target.Chips.get())*70
            target.g_f_p=int(target.milk.get())*152
            target.g_d_p=int(target.choc_cake.get())*30
            target.g_w_p=int(target.Butter.get())*155
            target.g_s_p=int(target.p_cake.get())*256
            target.g_t_p=int(target.bread.get())*70
            
            target.sd_m_p=int(target.Donuts.get())*85
            target.sd_f_p=int(target.biscuits.get())*85
            target.sd_fr_p=int(target.coke.get())*92
            target.sd_t_p=int(target.yogurt.get())*90
            target.sd_l_p=int(target.eggs.get())*87
            target.sd_s_p=int(target.sprite.get())*90


            target.sum_sweetprices=float(
                                            target.c_s_p+
                                            target.c_fc_p+
                                            target.c_fw_p+
                                            target.c_hs_p+
                                            target.c_hg_p+
                                            target.c_bl_p
                                            )
            target.sweetprices.set("Rs. "+str(target.sum_sweetprices))
            target.c_tax=target.sum_sweetprices*0.05
            target.cake_tax.set("Rs. "+str(round((target.c_tax),2)))
                        
            target.sum_everydays_price=float(
                                            target.g_r_p+
                                            target.g_f_p+
                                            target.g_d_p+
                                            target.g_w_p+
                                            target.g_s_p+
                                            target.g_t_p
                                            )
                                                            
            target.everydays_price.set("Rs. "+str(target.sum_everydays_price))
            target.g_tax=target.sum_everydays_price*0.02
            target.icecream_tax.set("Rs. "+str(round((target.g_tax),2)))

            target.sum_soft_drinks_price=float(
                                                target.sd_m_p+
                                                target.sd_f_p+
                                                target.sd_fr_p+
                                                target.sd_t_p+
                                                target.sd_l_p+
                                                target.sd_s_p
                                            )
            target.soft_drink_price.set("Rs. "+str(target.sum_soft_drinks_price))
            target.sd_tax=target.sum_soft_drinks_price*0.019
            target.soft_drink_tax.set("Rs. "+str(round((target.sd_tax),2)))

            target.sum_bill=float(target.g_tax+target.sd_tax+target.c_tax+target.sum_sweetprices+target.sum_everydays_price+target.sum_soft_drinks_price)


    def View_Cust_BIll(target):
        target.txtarea.delete('1.0',END)
      
        target.txtarea.insert(END, f"\nBill Number :{target.bill_no.get()}")
        target.txtarea.insert(END, f"\nCustomer Name: {target.c_name.get()}")
        target.txtarea.insert(END, f"\nPhone Number :{target.c_phno.get()} ")
       
        target.txtarea.insert(END, f"\nProducts\tQuantity\tPrice")
        

    def sum_bill(target):
        if len(target.c_phno.get())<10 :
            return messagebox.showerror("Error","Invalid Contact")
        
        if len(target.c_phno.get())>15 :
            return messagebox.showerror("Error","Invalid Contact")

        if target.c_name.get()=="" or target.c_phno.get()=="":
            return messagebox.showerror("Error","Customer details are must!!")

        elif target.sweetprices.get()=="Rs. 0.0" and target.everydays_price.get()=="Rs. 0.0" and target.soft_drink_price.get()=="Rs. 0.0":
            return messagebox.showerror("Error","No Product purchased")

        
        else:
            try:
                a=target.icecream.get()
                b=target.milo.get()
                c=target.cupcakes.get()
                d=target.muffins.get()
                e=target.DayFresh.get()
                f=target.mineralWater.get()
                g=target.Chips.get()
                h=target.milk.get()
                i=target.choc_cake.get()
                j=target.Butter.get()
                k=target.p_cake.get()
                l=target.bread.get()
                m=target.Donuts.get()
                n=target.biscuits.get()
                o=target.coke.get()
                p=target.yogurt.get()
                q=target.eggs.get()
                r=target.sprite.get()
                
                int(a)
                int(b)
                int(c)
                int(d)
                int(e)
                int(f)
                int(g)
                int(h)
                int(i)
                int(j)
                int(k)
                int(l)
                int(m)
                int(n)
                int(o)
                int(p)
                int(q)
                int(r)
                
            except ValueError:
                return messagebox.showinfo('Error','Quantity must be integer')

            
            try:
                tmp=target.c_phno.get()                
                int(tmp)                
            except ValueError:
                return messagebox.showinfo('Error','Contact must be integer')



            target.View_Cust_BIll()
            if target.icecream.get()!=0 :
                target.txtarea.insert(END, f"\nDonuts   \t\t  {target.icecream.get()}\t   Rs. {target.c_s_p}")
            
            if target.milo.get()!=0: 
                target.txtarea.insert(END, f"\nIceCream     \t\t  {target.milo.get()}\t   Rs. {target.c_fc_p}")
                
            if target.cupcakes.get()!=0:
                target.txtarea.insert(END, f"\nMuffins \t\t  {target.cupcakes.get()}\t   Rs. {target.c_fw_p}")
                
            if target.muffins.get()!=0: 
                target.txtarea.insert(END, f"\nCupDayFresh\t\t  {target.muffins.get()}\t   Rs. {target.c_hs_p}")
                
            if target.DayFresh.get()!=0: 
                target.txtarea.insert(END, f"\nChocolate Cake         \t  {target.DayFresh.get()}\t   Rs. {target.c_hg_p}")
                
            if target.mineralWater.get()!=0:
                target.txtarea.insert(END, f"\nPineAppleCake {target.mineralWater.get()}\t   Rs. {target.c_bl_p}")

        #--------------------------------------------------#

            if target.Chips.get()!=0:
                target.txtarea.insert(END, f"\nMilk\t\t  {target.Chips.get()}\t   Rs. {target.g_r_p}")
            
            if target.milk.get()!=0: 
                target.txtarea.insert(END, f"\nMineral Water \t\t  {target.milk.get()}\t   Rs. {target.g_f_p}")

            if target.choc_cake.get()!=0:
                target.txtarea.insert(END, f"\nCoke {target.choc_cake.get()}\t   Rs. {target.g_d_p}")
            
            if target.Butter.get()!=0: 
                target.txtarea.insert(END, f"\nSprite  \t\t  {target.Butter.get()}\t   Rs. {target.g_w_p}")

            if target.p_cake.get()!=0:
                target.txtarea.insert(END, f"\nMilo \t \t  {target.p_cake.get()}\t   Rs. {target.g_s_p}")
            
            if target.bread.get()!=0: 
                target.txtarea.insert(END, f"\nDayFresh  {target.bread.get()}\t   Rs. {target.g_t_p}")
                
            
   

            if target.Donuts.get()!=0:
                target.txtarea.insert(END, f"\nmuffins\t\t  {target.Donuts.get()}\t   Rs. {target.sd_m_p}")
            
            if target.biscuits.get()!=0:
                target.txtarea.insert(END, f"\nEggs\t\t  {target.biscuits.get()}\t   Rs. {target.sd_f_p}")

            if target.coke.get()!=0:
                target.txtarea.insert(END, f"\nBiscuits\t\t  {target.coke.get()}\t   Rs. {target.sd_fr_p}")
            
            if target.yogurt.get()!=0:
                target.txtarea.insert(END, f"\nYougurt\\t\t  {target.yogurt.get()}\t   Rs. {target.sd_t_p}")
            
            if target.eggs.get()!=0:
                target.txtarea.insert(END, f"\nChips\t\t  {target.eggs.get()}\t   Rs. {target.sd_l_p}")
            
            if target.sprite.get()!=0:
                target.txtarea.insert(END, f"\nButter\t\t  {target.sprite.get()}\t   Rs. {target.sd_s_p}")
            
            target.txtarea.insert(END, f"\n-------------------------------------")


            
            target.txtarea.insert(END, f"\nsum Bill\t\t\tRs. {str(target.sum_bill)}")


            target.conn = sqlite3.connect("bakery.db")
            target.c = target.conn.cursor()
            target.c.execute("SELECT Stock_Left FROM Stock" )
            target.data3 = target.c.fetchall()
            for i in target.data3:
                target.L.append(str(i))
           
            string1 = str(target.L[0])
            string2 = str(target.L[1])
            string3 = str(target.L[2])
            string4 = str(target.L[3])
            string5 = str(target.L[4])
            string6 = str(target.L[5])
            string7 = str(target.L[6])
            string8 = str(target.L[7])
            string9 = str(target.L[8])
            string10 = str(target.L[9])
            string11 = str(target.L[10])
            string12 = str(target.L[11])
            string13 = str(target.L[12])
            string14 = str(target.L[13])
            string15 = str(target.L[14])
            string16= str(target.L[15])
            string17 = str(target.L[16])
            string18 = str(target.L[17])
            
            a1 = str(int(re.search(r'\d+', string1).group())-int(target.choc_cake.get()))
            a2 = str(int(re.search(r'\d+', string2).group())-int(target.p_cake.get()))
            a3 = str(int(re.search(r'\d+', string3).group())-int(target.milk.get()))
            a4 = str(int(re.search(r'\d+', string4).group())-int(target.Butter.get()))
            a5 = str(int(re.search(r'\d+', string5).group())-int(target.Chips.get()))
            a6 = str(int(re.search(r'\d+', string6).group())-int(target.cupcakes.get()))
            
            a7 = str(int(re.search(r'\d+', string7).group())-int(target.DayFresh.get()))
            a8 = str(int(re.search(r'\d+', string8).group())-int(target.muffins.get()))
            a9 = str(int(re.search(r'\d+', string9).group())-int(target.milo.get()))
            a10 = str(int(re.search(r'\d+', string10).group())-int(target.icecream.get()))
            a11 = str(int(re.search(r'\d+', string11).group())-int(target.sprite.get()))
            a12 = str(int(re.search(r'\d+', string12).group())-int(target.eggs.get()))
            
            a13 = str(int(re.search(r'\d+', string13).group())-int(target.yogurt.get()))
            a14 = str(int(re.search(r'\d+', string14).group())-int(target.coke.get()))
            a15 = str(int(re.search(r'\d+', string15).group())-int(target.biscuits.get()))
            a16 = str(int(re.search(r'\d+', string16).group())-int(target.Donuts.get()))
            a17 = str(int(re.search(r'\d+', string17).group())-int(target.bread.get()))
            a18 = str(int(re.search(r'\d+', string18).group())-int(target.mineralWater.get()))
            
            if int(a1)<0 or int(a2)<0 or int(a3)<0 or int(a4)<0 or int(a5)<0 or int(a6)<0 or  int(a7)<0 or int(a8)<0 or int(a9)<0 or int(a10)<0 or int(a11)<0 or int(a12)<0 or int(a13)<0 or int(a14)<0 or int(a15)<0 or int(a16)<0 or int(a17)<0 or int(a18)<0 :
                return messagebox.showerror("Error","Any of Your Product is Out of Stock or Quantity is more according to stock")
            else:
                
                target.conn=sqlite3.connect("bakery.db")
                target.c=target.conn.cursor()
    
                target.c.execute("DROP TABLE Stock")
                    
                target.c.execute("CREATE TABLE IF NOT EXISTS Stock(ItemID TEXT PRIMARY KEY, ItemName TEXT NOT NULL, Stock_Left TEXT, Item_Price TEXT)")
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SS1012","Small_Stick_Icecream",str(a1),"30"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LGC1011","p_cake",str(a2),"256"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SCU1010","milk",str(a3),"152"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LG1009","Butter",str(a4),"155"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SC1008","Chips",str(a5),"70"))

                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("PA1007","Pastries",str(a6),"45"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("C10066","DayFresh",str(a7),"750"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("BR1005","muffins",str(a8),"35"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("PI1004","milo",str(a9),"312"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("RT1003","Rusk_Toast",str(a10),"120"))

                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("S345","Sprite",str(a11),"90"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("L435","eggs",str(a12),"87"))
                        
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("TU555","yogurt",str(a13),"90"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("FR65","coke",str(a14),"92"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("F788","biscuits",str(a15),"85"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("M908","Donuts",str(a16),"85"))

                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LS1013","Large_Stick_Icecream",str(a17),"70"))
                
                target.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("CM1020","CupCake_Muffins",str(a18),"151"))
                
                target.conn.commit()

    def clear_data(target):
        op=messagebox.askyesnocancel("Clear","Do you really want to Clear?")   
        if op>0:
            target.icecream.set(0)
            target.milo.set(0)
            target.muffins.set(0)
            target.DayFresh.set(0)
            target.cupcakes.set(0)
            target.mineralWater.set(0)
            
           
            
            target.Chips.set(0)
            target.Butter.set(0)
            target.milk.set(0)


            target.p_cake.set(0)
            target.choc_cake.set(0)
            target.bread.set(0)
            
           
            
            target.Donuts.set(0)
            target.biscuits.set(0)
            target.coke.set(0)
            target.yogurt.set(0)
            target.eggs.set(0)
            target.sprite.set(0)

            target.sweetprices.set("")
            target.everydays_price.set("")
            target.soft_drink_price.set("")
            
            target.cake_tax.set("")
            target.icecream_tax.set("")
            target.soft_drink_tax.set("")


            target.c_name.set("")
            target.c_phno.set("")
            target.bill_no.set("")
            target.search_bill.set("")
            x=random.randint(1000,9999)
            target.bill_no.set(str())
            target.txtarea.delete("1.0",END)

        else:
            pass    
            

   


    def find(target):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==target.search_bill.get():
                f1=open(f"Bills/{i}","r")
                target.txtarea.delete('1.0',END)
                for d in f1:
                    target.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
           

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
       
       import USERlogin


    
 
    
            
    
                

    def Exit(target):
        target.window.destroy()
        import HEmployee

window = Tk()
obj = BuYuser(window)
window.mainloop()
