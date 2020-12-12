from tkinter import *
import mysql.connector
import sys
import checkin
import checkout
import RoomEnquiry
import viewdetails
import editdetails
import bill

window=Tk()
window.title("Menu Form")
window.geometry("300x300")

heading=Label(window,text="HOTEL MANAGEMENT SYSTEM",fg="blue",bg="grey",width="500",height="3").pack()

Label(window,text="Select Options: ",fg="red").place(x=15,y=70)
Button(window,text="Check-In Form",command=lambda:checkin.check_in(window)).place(x=10,y=120)
Button(window,text="Check-Out Form",command=lambda:checkout.checkout(window)).place(x=150,y=120)
Button(window,text="Enquiry Form",command=lambda:RoomEnquiry.enquiry(window)).place(x=10,y=170)
Button(window,text="Print Bill",command=lambda:bill.bill(window)).place(x=150,y=170)
Button(window,text="Print Details",command=lambda:viewdetails.view_details(window)).place(x=10,y=220)
Button(window,text="Edit Details",command=lambda:editdetails.edit_details(window)).place(x=150,y=220)

window.mainloop()