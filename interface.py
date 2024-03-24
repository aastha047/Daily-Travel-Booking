import pymysql as p
con=p.connect(host='localhost',user='root',password='aastha',database='xiia')
cur=con.cursor()
flag=0
def create():
    global flag
    if flag==0:
        q1="create table FACULTY(F_ID int(3) Primary key, FName varchar(15),LName varchar(15),Hiredate varchar(10),Salary int(6))"
        cur.execute(q1)
        q2="create table COURSES(C_ID int(5) Primary Key,F_ID int(3),CName varchar(30),Fees int(5))"
        cur.execute(q2)
        flag=1
    else:
        print('table already created') 
def insert():
    F_ID=int(input("Enter f_id"))
    FName=input("enter first name")
    LName=input("enter last name")
    Hiredate=input("enter hiredate (YYYY-MM-DD)")
    Salary=int(input("enter salary"))
    q="insert into FACULTY values({},'{}','{}','{}',{})".format(F_ID,FName,LName,Hiredate,Salary)
    cur.execute(q)
    C_ID=int(input("Enter C_id"))
    F_ID=int(input("Enter f_id"))
    CName=input("enter course name")
    F=int(input("Enter fees"))
    q="insert into COURSES values({},{},'{}',{})".format(C_ID,F_ID,CName,F)
    cur.execute(q)
    con.commit()   
def display():
    print("The details of those faculties whose salary is greater than 12000")
    q='select * from FACULTY where Salary >12000'
    cur.execute(q)
    d=cur.fetchall()
    for i in d:
        print(i)
    print("The details of courses whose fees is in the range 15000 to 50000(both value included)")
    q1='select * from COURSES where Fees>=15000 and Fees<=50000'
    cur.execute(q1)
    d=cur.fetchall()
    for i in d:
        print(i)
    print("The count of unique F_ID from the courses table")
    q2='select COUNT(DISTINCT(F_ID)) from COURSES'
    cur.execute(q2)
    d=cur.fetchall()
    for i in d:
        print(i)
    print("The details of all faculties whose course fees is more than 5500")
    q3='select * from FACULTY,COURSES where FACULTY.F_ID=COURSES.F_ID and Fees>5500'
    cur.execute(q3)
    d=cur.fetchhall()
    for i in d:
        print(i)
def delete():
    q="delete from COURSES where CName='System Design'"
    cur.execute(q)
    con.commit()
    q1='select * from COURSES'
    cur.execute(q1)
    d=cur.fetchall()
    for i in d:
        print(i)
    print("Record deleted from course table where course name is 'System Design' ")
def modify():
    q="update COURSES set Fees=Fees+500 where Cname='System Design'"
    cur.execute(q)
    con.commit()
    q1='select * from COURSES'
    d=cur.fetchall()
    for i in d:
        print(i)
    print("Fees of course 'System Designs' increased by 500")
while True:
    print("1.Create\n2.Insert\n3.Display\n4.Delete\n5.Modify\n6.Exit")
    x=int(input("Enter your choice"))
    if x==1:
        create()
    elif x==2:
        insert()
    elif x==3:
        display()
    elif x==4:
        delete()
    elif x==5:
        modify()
    elif x==6:
        break
    else:
        print("Enter valid choice")

    

