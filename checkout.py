from tkinter import *
import mysql.connector
import sys
import datetime
from datetime import date


def checkout(r):
	window=Toplevel(r)
	window.title("Check-out Form: ")
	window.geometry("450x350")

	roomval=IntVar()
	custval=IntVar()
	inval=StringVar()
	outval=StringVar()
	rateval=IntVar()
	typeval=StringVar()

	def delete():
		r=int(roomval.get())
		c=int(custval.get())
		i=str(inval.get())
		o=str(outval.get())
		ra=int(rateval.get())
		t=str(typeval.get())
		print(r,c,i,o,ra,t)
		db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
		cursor=db.cursor()
		cursor.execute("DELETE FROM checkin WHERE cust_id=%d"%c)
		cursor.execute("insert into checkout values(%d,%d,'%s','%s',%d,'%s')"%(r,c,i,o,ra,t))
		Label(window,text="Record Deleted",fg="red").place(x=50,y=280)
		db.commit()
		db.close()
		
	heading=Label(window,text="Check-out Form: ",fg="black",bg="grey",width="500",height="3").pack()

	Label(window,text="Enter Room-Id: ").place(x=15,y=60)
	Label(window,text="Enter Customer-Id: ").place(x=15,y=90)
	Label(window,text="Enter Date of check-in (in format (yyyy,mm,dd)): ").place(x=15,y=120)
	Label(window,text="Enter Date of check-out (in format (yyyy,mm,dd)): ").place(x=15,y=150)
	Label(window,text="Enter Rate: ").place(x=15,y=180)
	Label(window,text="Enter Room-Type: ").place(x=15,y=210)

	Entry(window,textvariable=roomval).place(x=110,y=60)
	Entry(window,textvariable=custval).place(x=130,y=90)
	Entry(window,textvariable=inval).place(x=280,y=120)
	Entry(window,textvariable=outval).place(x=290,y=150)
	Entry(window,textvariable=rateval).place(x=80,y=180)
	Entry(window,textvariable=typeval).place(x=120,y=210)

	Button(window,text="Delete Entry",command=delete).place(x=50,y=250)

	window.mainloop()