from tkinter import *
import mysql.connector
import sys

def check_in(r):
	window=Toplevel(r)
	window.title("Check-in Form")
	window.geometry("400x450")

	custval=IntVar()
	roomval=IntVar()
	nameval=StringVar()
	addval=StringVar()
	pinval=IntVar()
	perval=IntVar()
	phnval=IntVar()
	emailval=StringVar()
	inval=StringVar()

	def insert():
		c=int(custval.get())
		r=int(roomval.get())
		n=str(nameval.get())
		a=str(addval.get())
		p=int(pinval.get())
		pe=int(perval.get())
		ph=str(phnval.get())
		e=str(emailval.get())
		i=str(inval.get())
		print(c,r,n,a,p,pe,ph,e,i)
		db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
		cursor=db.cursor()
		cursor.execute("insert into checkin values(%d,%d,'%s','%s',%d,%d,'%s','%s','%s')"%(c,r,n,a,p,pe,ph,e,i))
		Label(window,text="Record Inserted",fg="red").place(x=50,y=410)
		db.commit()
		db.close()
				
	heading=Label(window,text="Check-in Form: ",fg="black",bg="grey",width="500",height="3").pack()	

	Label(window,text="Enter Customer Id: ").place(x=15,y=60)
	Label(window,text="Enter Room Id: ").place(x=15,y=90)
	Label(window,text="Enter Customer Name: ").place(x=15,y=120)
	Label(window,text="Enter Adress: ").place(x=15,y=150)
	Label(window,text="Enter Pincode: ").place(x=15,y=180)
	Label(window,text="Enter No of Persons: ").place(x=15,y=210)
	Label(window,text="Enter Phone no: ").place(x=15,y=240)
	Label(window,text="Enter Email-id: ").place(x=15,y=270)
	Label(window,text="Enter Date of Check in: ").place(x=15,y=300)

	Entry(window,textvariable=custval).place(x=130,y=60)
	Entry(window,textvariable=roomval).place(x=110,y=90)
	Entry(window,textvariable=nameval).place(x=150,y=120)
	Entry(window,textvariable=addval).place(x=110,y=150)
	Entry(window,textvariable=pinval).place(x=110,y=180)
	Entry(window,textvariable=perval).place(x=130,y=210)
	Entry(window,textvariable=phnval).place(x=110,y=240)
	Entry(window,textvariable=emailval).place(x=110,y=270)
	Entry(window,textvariable=inval).place(x=150,y=300)

	Button(window,text="Submit Entry",command=insert).place(x=100,y=370)

	window.mainloop()