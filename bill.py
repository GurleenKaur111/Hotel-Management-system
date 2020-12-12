from tkinter import *
import mysql.connector
import sys
from datetime import date

def bill(r):
    window=Toplevel(r)
    window.title("Bill")
    window.geometry("450x350")

    heading=Label(window,text="Bill: ",fg="black",bg="grey",width="500",height="6").pack() 

    d1=IntVar()
    d2=IntVar()
    m1=IntVar()
    m2=IntVar()
    y1=IntVar()
    y2=IntVar()
    r=IntVar()

    def bill():
        f_date = date(y1.get(), m1.get(), d1.get())
        l_date = date(y2.get(), m2.get(), d2.get())
        delta = l_date - f_date
        d=delta.days
        print("days: ",d)
        rn=r.get()
        if rn>=101 and rn<=115:
            cost=1500
        elif rn>=116 and rn<=125:
            cost=2000
        elif rn>=126 and rn<=130:
            cost=5000
        else:
            cost=invalid
        print("cost per day: ",cost)
        bill=d*cost
        print("print bill: ",bill)  
        Label(window,text="Amount to be paid=%d"%bill,fg="red").place(x=15,y=210)


    Label(window,text="Enter Date of check-in(dd/mm/yyyy): ").place(x=15,y=120)
    Label(window,text="Enter Date of check-out(dd/mm/yyyy): ").place(x=15,y=150)
    Label(window,text="Room No: ").place(x=15,y=180)

    Entry(window,textvariable=d1).place(x=220,y=120,width=30)
    Entry(window,textvariable=m1).place(x=260,y=120,width=30)
    Entry(window,textvariable=y1).place(x=300,y=120,width=50)
    Entry(window,textvariable=d2).place(x=230,y=150,width=30)
    Entry(window,textvariable=m2).place(x=270,y=150,width=30)
    Entry(window,textvariable=y2).place(x=310,y=150,width=50)
    Entry(window,textvariable=r).place(x=80,y=180,width=50)

    Button(window,text="print bill",command=bill).place(x=50,y=250)

    window.mainloop()