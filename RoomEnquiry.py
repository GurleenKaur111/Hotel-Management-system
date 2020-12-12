from tkinter import *
import mysql.connector
import sys

def enquiry(r):
	window=Toplevel()
	window.title("Enquiry Form")
	window.geometry("400x300")

	heading=Label(window,text="Room Enquiry: ",fg="black",bg="grey",width="500",height="3").pack()

	roomval=IntVar()
	roomtype=StringVar()

	def select():
		r=int(roomval.get())
		rt=str(roomtype.get())
		db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
		cursor=db.cursor()
		try:
			cursor.execute("SELECT * FROM checkin WHERE room_id=%d"%r)
			results=cursor.fetchall()
			for row in results:
				cust_id=row[0]
				room_id=row[1]
				name=row[2]
				address=row[3]
				pincode=row[4]
				no_of_persons=row[5]
				phone_no=row[6]
				email_id=row[7]
				date_check_in=row[8]
			print("cust_id=%d,room_id=%d,name='%s',address='%s',pincode=%d,no_of_persons=%d,phone_no='%s',email_id='%s',date_check_in='%s'"%(cust_id,room_id,name,address,pincode,no_of_persons,phone_no,email_id,date_check_in))
			Label(window,text="Room Booked",fg="red").place(x=50,y=250)
		except:
			Label(window,text="Room Empty",fg="red").place(x=50,y=250)
		db.commit()
		db.close()

	Label(window,text="Enter Room No: ").place(x=15,y=70)
	Label(window,text="Enter Room Type: ").place(x=15,y=140)

	Entry(window,textvariable=roomval).place(x=15,y=100)
	Entry(window,textvariable=roomtype).place(x=15,y=170)

	Button(window,text="Check Room Status",command=select).place(x=50,y=200)

	window.mainloop()