from tkinter import *
import mysql.connector
import sys

def view_details(r):
	window=Toplevel(r)
	window.title("View Customer Details")
	window.geometry("300x400")

	heading=Label(window,text="Customer Details: ",fg="black",bg="grey",width="500",height="3").pack()

	roomval=IntVar()

	def select():
		r=int(roomval.get())
		db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
		cursor=db.cursor()
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
			Label(window,text="cust_id=%d,\nroom_id=%d,\nname='%s',\naddress='%s',\npincode=%d,\nno_of_persons=%d,\nphone_no='%s',\nemail_id='%s',\ndate_check_in='%s'"%(cust_id,room_id,name,address,pincode,no_of_persons,phone_no,email_id,date_check_in),fg="red").place(x=10,y=190)
			Label(window,text="Details Printed",fg="red").place(x=50,y=160)
		db.commit()
		db.close()

	Label(window,text="Enter Room No: ").place(x=15,y=70)

	Entry(window,textvariable=roomval).place(x=15,y=100)

	Button(window,text="View Customer Details",command=select).place(x=50,y=130)

	window.mainloop()