import datetime
import random

import datetime
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    database="ticketbooking",
    user="root",
    password="12345"
)

def ticbook():

    print("Available destinations:\n1.Vellore\n2.Madurai\n3.Kanchipuram\n4.Coimbatore\n5.Kallakurichi" )
    user=int(input("Enter your Destination? 1 or 2 or 3 or 4 or 5\n"))
    if user==1:
        to="Vellore"
        ticket=70
        choose(to,ticket)
    elif user==2:
        to="Madurai"
        ticket=90
        choose(to,ticket)
    elif user==3:
        to="Kanchipuram"
        ticket=50
        choose(to,ticket)
    elif user==4:
        to="Coimbatore"
        ticket=200
        choose(to,ticket)
    elif user==5:
        to="Kallakurichi"
        ticket=150
        choose(to,ticket)
    else:
        print("Choose correct option")
        ticbook()



def choose(to,ticket):
    i=1
    date=str(input("enter date of travel:"))
    no=int(input("How many Tickets you want to book? :"))
    ticketnum=random.randint(100000,999999)
    while i<=no:
        print(f"TICKET{i}")
        name=str(input("enter name:"))
        age=int(input("enter your age:"))
        num=int(input("enter your phone number:"))
        mycursor=mydb.cursor()
        sq="INSERT INTO busbooking(name,age,phonenumber,to,ticketnum,dot) values(%s,%s,%s,%s,%s,%s)"
        val=(name,age,num,to,ticketnum,date)
        mycursor.execute(sq,val)
        mydb.commit()
        i=i+1
    fare=ticket*no
    print(f"Your total cost is {fare}")
    mycursor=mydb.cursor()
    mycursor.execute("""UPDATE busbooking SET  fare= '%s' WHERE name = '%s'"""%(fare,name))
    mydb.commit()    



def status():
    no=int(input("Enter ticket no:"))
    mycursor=mydb.cursor()
    mycursor.execute(""" SELECT * FROM busbooking where ticketno='%s'"""%(no))
    row=mycursor.fetchall()
    count=mycursor.rowcount
    if count>=1:
        print("ID,Name,age,phno,destination,fare,ticket no")
        for i in row:
            print(i)
    else:
        print("not found \nenter valid number ")
        status()



    

def cancel():
    ticketno=int(input("ticket no:"))
    mycursor=mydb.cursor()
    mycursor.execute(""" DELETE * FROM busbooking where ticketno='%s'"""%(ticketno))
    mydb.commit()



print("***********WELCOME*********")
user=int(input("1.Ticket Booking\n2.Status of booked ticket\n3.cancel ticket\nEnter ypur option:"))

if user==1:
    ticbook()

elif user==2:
    status()

elif user==3:
    cancel()

else:
    print("select only from the option")

print("*******THANK YOU*******")
print("<><><><>Visit again<><><><>")