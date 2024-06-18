import mysql.connector
import random
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE airline12")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="airline12")
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE TICKET (name VARCHAR(255), phoneno VARCHAR(255), adharno VARCHAR(255), seatno VARCHAR(255), tickettype VARCHAR(255),NOofticket VARCHAR(255),PRICE VARCHAR(255))")
#mycursor.execute("CREATE TABLE bill (name VARCHAR(255), quantitypfBag VARCHAR(255), billcharged VARCHAR(255))")
#mycursor.execute("CREATE TABLE parking (name VARCHAR(255), vehiclestype VARCHAR(255), billcharged VARCHAR(255), parkingnumber VARCHAR(255))")

def ticket():
    m="y"
    while m=="y":
        print("1.BOOK TICKET")
        print("2.CANCEL TICKET")
        print("3.CHECK YOUR SEAT NUMBER AND DETAILS")
        print("4.Exit")
        p=int(input("enter your choice"))
        if p==1:
            N=input("enter your name")
            E=int(input("enter the number of ticket you want to book"))
            G=str(E)
            print("We have the following ticket prices and type for you:")
            print("1.type First class (price=4000)")
            print("2.type Business class(price=3500)")
            print("3.type Economy class(price=3000)")
            c=int(input("press the above numbers which type you want"))
            if c==1:
                S="first class"
                V=str(4000*E)
            if c==2:
                S="business class"
                V=str(3500*E)
            if c==3:
                S="economy class"
                V=str(3000*E)
            D=input("enter the phone number")
            W=input("enter you adhar number")
            P=str(random.randrange(1,80))
            sql = "INSERT INTO TICKET (name ,phoneno ,adharno ,seatno ,tickettype ,NOofticket ,PRICE ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (N,D,W,P,S,G,V)
            mycursor.execute(sql, val)
            mydb.commit()
        elif p==2:
            print("CANCEL THE TICKET")
            
            g=input("enter your adhar number")
            sql = "DELETE FROM TICKET WHERE adharno =%s"
            a=(g,)
            mycursor.execute(sql,a)
            mydb.commit()
            print("your ticket has been cancel")
        elif p==3:
            g=input("enter your adhar number")
            f="SELECT * FROM TICKET WHERE adharno =%s"
            a=(g,)
            print("your room number and details")
            mycursor.execute(f,a)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        elif p==4:
            exit()
        else:
            print("you enter the wrong choice")
        m=input("if you want to continue then press y or press any key for exit")
    else:
        exit()

def orderfood():
    m="y"
    while m=="y":
        print("1.tea,2.coffee,3.cold drink,4.samosa,5.sandwich,6.dhokla,7.kachori,8.milk,9.noodles,10.pasta")
        d=int(input("enter the choice which ypu want just press number only"))
        if(d==1):
            print("you have ordered tea")
            a=int(input("enter quantity"))
            s=10*a
            print("your amount for tea is:",s,"\n")
        elif(d==2):
            print("you have ordered coffee")
            a=int(input("enter quantity"))
            s=10*a
            print("your amount for coffee is:",s,"\n")
        elif(d==3):
            print("you have ordered cold drink")
            a=int(input("enter quantity"))
            s=20*a
            print("your amount for cold drink is:",s,"\n")
        elif(d==4):
            print("you have ordered samosa" )
            a=int(input("enter quantity"))
            s=10*a
            print("your amount for samosa is: ",s,"\n")
        elif(d==5): 
            print("you have ordered sandwich")
            a=int(input("enter quantity"))
            s=50*a
            print("your amount for sandwich is:",s,"\n")
        elif(d==6):
            print("you have ordered dhokla")
            a=int(input("enter quantity"))
            s=30*a
            print("your amount for dhokla is:",s,"\n")
        elif(d==7):
            print("you have ordered kachori")
            a=int(input("enter quanti ty"))
            s=10*a
            print("your amount for kachori is:",s,"\n")
        elif(d==8):
            print("you have ordered milk")
            a=int(input("enter quantity"))
            s=20*a
            print("your amount for milk is:",s,"\n")
        elif(d==9):
            print("you have ordered noodles")
            a=int(input("enter quantity"))
            s=50*a
            print("your amount for noodles is:",s,"\n")
        elif(d==10):
            print("you have ordered pasta")
            a=int(input("enter quantity"))
            s=50*a
            print("your amount for pasta is:",s,"\n")
        else:
            print("please enter your choice from the menu")
        m=input("if you want to continue then press y or press any key for exit")
    else:
        exit()

def luggagebill():
    m="y"
    while m=="y":
        print("1.calculate bill")
        print("2.check detail of bill")
        print("3. press any key for exit")
        p=int(input("enter choice"))
        if p==1:
            b=input("enter your name")
            d=int(input("enter the number of bags"))
            y=str(d)
            print("cost 1 bag is 100 rupess")
            j=d*100
            f=str(j)
            print("your bill of ",d,"bags is",j,"ruppess")
            sql = "INSERT INTO bill (name, quantitypfBag, billcharged) VALUES (%s, %s, %s)"
            val = (b,d,f)
            mycursor.execute(sql,val)
            mydb.commit()
        elif p==2:
            l=input("enter your name")
            f="SELECT * FROM bill WHERE name =%s"
            a=(l,)
            mycursor.execute(f,a)
            myrecord6=mycursor.fetchall()
            for z in myrecord6:
                print(z)
        else:
            exit()
        m=input("if you want to continue then press y or press any key for exit")
    else:
        exit()

def parking():
        apb="y"
        while apb=="y":
                print("1. press 1 buying parking ticket")
                print("2. press 2 cancel parking ticket")
                print("3. press 3 for to kown your ticket number and details")
                print("press any key for exit")
                aap=int(input("enter your choice"))
                if aap==1:
                        print("1. press 1 for two wheeler.........price = 20 per day")
                        print("2. press 2 for three wheeler.............price=40 per day")
                        print("3. press 3 for four wheeler..........price=60 per day")
                        print("press any key for exit")
                        apr=int(input("enter your choice"))
                        N=input("enter your name")
                        if apr==1:
                                jj="two wheeler"
                                ee=int(input("enter number of day for booking a parking"))
                                bill=ee*20
                                bi=str(bill)
                                print("your parking bill",bill)
                                P=str(random.randrange(100,8000))
                                print("your ticket number",P)
                                sql = "INSERT INTO  parking (name ,vehiclestype ,billcharged) VALUES (%s, %s, %s)"
                                val = (N,jj,bi)
                                mycursor.execute(sql, val)
                                mydb.commit()
                        elif apr==2:
                                jj="three wheeler"
                                ee=int(input("enter number of day for booking a parking"))
                                bill=ee*40
                                bi=str(bill)
                                print("your parking bill",bill)
                                P=str(random.randrange(100,8000))
                                print("your ticket number",P)
                                sql = "INSERT INTO  parking (name ,vehiclestype ,billcharged) VALUES (%s, %s, %s)"
                                val = (N,jj,bi)
                                mycursor.execute(sql, val)
                                mydb.commit()
                        elif apr==3:
                                jj="four wheeler"
                                ee=int(input("enter number of day for booking a parking"))
                                bill=ee*60
                                bi=str(bill)
                                print("your parking bill",bill)
                                P=str(random.randrange(100,8000))
                                print("your ticket number",P)
                                sql = "INSERT INTO  parking (name ,vehiclestype ,billcharged ,parkingnumber) VALUES (%s, %s, %s ,%s)"
                                val = (N,jj,bi,P)
                                mycursor.execute(sql, val)
                                mydb.commit()
                        else:
                                exit()
                elif aap==2:
                        g=input("enter your ticket number")
                        sql = "DELETE FROM parking WHERE  parkingnumber=%s"
                        a=(g,)
                        mycursor.execute(sql,a)
                        mydb.commit()
                        print("your ticket has been cancel")
                elif aap==3:
                        g=input("enter your  parking ticket number")
                        f="SELECT * FROM parking WHERE parkingnumber=%s"
                        a=(g,)
                        mycursor.execute(f,a)
                        myresult = mycursor.fetchall()
                        print("your parking number and details..........(if no details is not display then your praking ticket is not booked or may be cancelled)")
                        for x in myresult:
                                print(x)
                else:
                        exit()
                apb=input("press y for continue or press any key for exit")


print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")                    
print("--------------------------AIR INDIA AIRLINE--------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print()
print("1. Check Or Book Ticket")
print("2. Order Food")
print("3. Luggage Bill")
print("4. Book Parking Ticket For Your Vehicles")
print("5. Press 5 For Exit")
qm=int(input("Enter the choice"))

def main():
    if qm==1:
        ticket()
    elif qm==2:
        orderfood()
    elif qm==3:
        luggagebill()
    elif qm==4:
        parking()
    else:
        exit()
main()

    
    
