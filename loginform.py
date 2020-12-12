from tkinter import *
import mysql.connector
import sys
import checkin
import checkout
import RoomEnquiry
import viewdetails
import editdetails
import bill

root=Tk()
root.title("Login Form")
root.geometry("300x300")

def create_window(r):
    window=Toplevel(r)
    window.title("Reset Password")
    window.geometry("400x400")
    username=StringVar()
    password1=StringVar()
    password2 = StringVar()

    Label(window, text="Enter Username: ").place(x=15,y=70)
    Entry(window, textvariable=username).place(x=15, y=100)

    Label(window, text="Enter Password: ").place(x=15,y=140)
    Entry(window, textvariable=password1, show="*").place(x=15,y=170)

    Label(window, text="Re-Enter Password: ").place(x=15,y=210)
    Entry(window, textvariable=password2, show="*").place(x=15,y=240)

    Button(window,text="Save Password").place(x=50,y=290)

    db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="cbse")
    cursor=db.cursor()
    try:
        sql="UPDATE cbse set username='%s' and password=%d"%(username.get(),password1.get())
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
    window.mainloop()

def login():
    print("username: ",username.get())
    print("password: ",password.get())
    if username.get()=='root' and password.get()=='1234':
       l3=Label(root,text="Login Successful!!",fg="red")
       l3.pack()
       window=Tk()
       window.title("Menu Form")
       window.geometry("300x300")

       heading=Label(window,text="HOTEL MANAGEMENT SYSTEM",fg="blue",bg="grey",width="500",height="3").pack()

       Label(window,text="Select Options: ",fg="red").place(x=15,y=70)
       Button(window,text="Check-In Form",command=lambda:checkin.check_in(root)).place(x=10,y=120)
       Button(window,text="Check-Out Form",command=lambda:checkout.checkout(root)).place(x=150,y=120)
       Button(window,text="Enquiry Form",command=lambda:RoomEnquiry.enquiry(root)).place(x=10,y=170)
       Button(window,text="Print Bill",command=lambda:bill.bill(root)).place(x=150,y=170)
       Button(window,text="Print Details",command=lambda:viewdetails.view_details(root)).place(x=10,y=220)
       Button(window,text="Edit Details",command=lambda:editdetails.edit_details(root)).place(x=150,y=220)

       window.mainloop()
    else:
        l4= Label(root, text="Incorrect values!!",fg="red")
        l4.pack()
    return

heading=Label(root,text="Login form: ",fg="black",bg="grey",width="500",height="3").pack()

username = StringVar()
password = StringVar()

l1=Label(root,text="Enter Username: ").place(x=15,y=70)
l2=Label(root,text="Enter Password: ").place(x=15,y=140)

Button(root,text="Submit",command=login).place(x=50,y=210)
Button(root, text="Forgot Password? ",command=lambda:create_window(root)).place(x=50,y=240)

Entry(root,textvariable=username).place(x=15,y=100)
Entry(root,textvariable=password,show='*').place(x=15,y=170)

root.mainloop()