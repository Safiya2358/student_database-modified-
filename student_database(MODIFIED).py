import mysql.connector as mycon 
 
cn = mycon.connect(host='localhost', user='root', password="Safi2005" ) 
if cn.is_connected(): 
    print('connected successfully') 
cur = cn.cursor() 
#cur.execute("create database STUDENT_MANAGEMENT") 
cur.execute("use  STUDENT_MANAGEMENT") 
'''
cur.execute("create table stu (regno varchar(8) primary key, rollno varchar(8),name varchar(50) not null,\n" 
            "dept varchar(40), cgpa int)") 
'''
 
def showAll(): 
    global cn 
    global cur 
 
    try: 
        query = "select * from stu" 
        cur.execute(query) 
        results = cur.fetchall() 
        print("*" * 110) 
        print('%5s' % "REGISTRATION NO.", '%25s' % 'ROLL NO.', '%25s' % 'STUDENT NAME','%25s' % 'DEPARTMENT', 
              '%10s' % 'CGPA') 
        print("*" * 110)
        count = 0 
 
 
        for row in results: 
            print('%10s' % row[0], '%30s' % row[1], '%30s' % row[2] , '%20s' % row[3],'%10s' % row[4]) 
            count += 1 
        print("*" * 45, "TOTAL RECORD : ", count, "*" * 46) 
        print("\n")
    except: 
        print("error") 
def addStu(): 
    global cn, cur 
    print("*"*47,"ADD NEW STUDENT","*"*46) 
    rino = input("Enter Registration No. :")
    rno = input("Enter Roll No. : ")  
    nam = input("Enter Student Name :") 
    dp = input("Enter Department: ")
    cgpa = int(input("Enter CGPA score :")) 
    query = f"insert into stu values('{rino}','{rno}','{nam}','{dp}',{cgpa})" 
    cur.execute(query) 
    cn.commit() 
    print("\n  RECORD ADDED SUCCESSFULLY!")
    print("\n")
 
def searchStu(): 
    global cn, cur 
    print("CHOICE:") 
 
 
    print("1.SINGLE STUDENT DETAILS.\n2.DETAILS OF ALL THE STUDENTS IN A DEPARTMENT.\n3.TOTAL NUMBER OF STUDENTS IN A DEPARTMENT.")
    print("\n") 
    c=int(input("Enter choice:")) 
    if c==1: 
        print("*"*40,"SEARCH SINGLE STUDENT DETAILS","*"*40) 
        rn = input("Enter Registration No. to search :")
        query = f"select * from stu where regno='{rn}' " 
        cur.execute(query) 
        results = cur.fetchall() 
        if cur.rowcount <= 0: 
            print("SORRY! NO MATCHING DETAILS AVAILABLE.")
            print("\n") 
        else: 
 
            print("*" * 110) 
            print('%5s' % "REGISTRATION NO.", '%25s' % 'ROLL NO.', '%25s' % 'STUDENT NAME','%25s' % 'DEPARTMENT', 
              '%10s' % 'CGPA') 
            print("*" * 110) 
            for row in results: 
                print('%10s' % row[0], '%30s' % row[1], '%30s' % row[2] , '%20s' % row[3],'%10s' % row[4])
        print("-" * 110)
        print("\n") 
    elif c==2: 
        print("*"*30,"SEARCH DETAILS OF ALL THE STUDENTS IN A DEPARTMENT","*" *30) 
        dp = input("Enter Department name to search :") 
 
 
        query = f"select * from stu where dept='{dp}' " 
        cur.execute(query) 
        results = cur.fetchall() 
        if cur.rowcount <= 0: 
            print("SORRY! NO MATCHING DETAILS AVAILABLE.") 
        else: 
 
            print("*" * 110) 
            print('%5s' % "REGISTRATION NO.", '%25s' % 'ROLL NO.', '%25s' % 'STUDENT NAME','%25s' % 'DEPARTMENT', 
              '%10s' % 'CGPA') 
            print("*" * 110) 
            for row in results: 
                print('%10s' % row[0], '%30s' % row[1], '%30s' % row[2] , '%20s' % row[3],'%10s' % row[4]) 
        print("-" * 110)
        print("\n") 
    elif c==3: 
        print("*"*30,"TOTAL NUMBER OF STUDENTS IN A DEPARTMENT","*"*30) 
        dp = input("Enter Department name to search :") 
        query = f"select count(name) from stu group by dept having  dept= '{dp}'" 
        cur.execute(query) 
        results = cur.fetchall() 
        c=0 
        for i in results: 
            c=c+i[0] 
 
 
        if cur.rowcount > 0: 
            print("TOTAL NUMBER OF STUDENTS IN", dp, "DEPARTMENT:", c )
            print("\n") 
        else: 
            print("TOTAL NUMBER OF STUDENTS IN", dp, "DEPARTMENT: 0")
            print("\n") 
 
def editStu(): 
    global cn, cur 
    print("*" * 44,"EDIT STUDENT DETAILS", "*" * 44) 
    rn = input("Enter Registration No. to edit :")
    query = f"select * from stu where regno='{rn}' "
    cur.execute(query) 
    results = cur.fetchall() 
    if cur.rowcount <= 0: 
        print("SORRY! NO MATCHING DETAILS AVAILABLE.") 
    else: 
 
        print("*" * 110) 
        print('%5s' % "REGISTRATION NO.", '%25s' % 'ROLL NO.', '%25s' % 'STUDENT NAME','%25s' % 'DEPARTMENT', '%10s' % 'CGPA') 
        print("*" * 110) 
        for row in results: 
             print('%10s' % row[0], '%30s' % row[1], '%30s' % row[2] , '%20s' % row[3],'%10s' % row[4]) 
        print("-" * 110)
        print("\n") 
 
 
    ans = input("Are you sure to update ? (y/n)") 
    if ans == "y" or ans == "Y": 
        dp = input("Enter new department to update (enter old value if not to update) :") 
        cgpa = float(input("Enter new cgpa to update (enter old value if not to update) :")) 
        query = f"update stu set dept='{dp}',cgpa= {cgpa}  where regno= '{rn}' "
        cur.execute(query) 
        cn.commit() 
        print("\nRECORD UPDATED") 
        print("\n")
 
def delStu(): 
    global cn, cur 
    print("*" * 43, "DELETE STUDENT DETAILS" ,"*"* 43) 
    rn = input("Enter Registration No. to delete :")
    query = f"select * from stu where regno='{rn}' "
    cur.execute(query) 
    results = cur.fetchall() 
    if cur.rowcount <= 0: 
        print("SORRY! NO MATCHING DETAILS AVAILABLE.") 
    else:
        print("*" * 110) 
        print('%5s' % "REGISTRATION NO.", '%25s' % 'ROLL NO.', '%25s' % 'STUDENT NAME','%25s' % 'DEPARTMENT', '%10s' % 'CGPA') 
        print("*" * 110) 
        for row in results: 
             print('%10s' % row[0], '%30s' % row[1], '%30s' % row[2] , '%20s' % row[3],'%10s' % row[4]) 
        print("-" * 110)
        print("\n")
 
    ans = input("Are you sure to delete ? (y/n)") 
    if ans == "y" or ans == "Y": 
        query = f"delete from stu where regno='{rn}' " 
        cur.execute(query) 
        cn.commit() 
        print("\n## RECORD DELETED  ##") 
        print("\n")
 


 
while True: 
    print("%70s" % "STUDENT TABLE") 
    print("CHOICES:") 
    print("1. SHOW  ALL STUDENT DETAILS. ") 
    print("2. ADD A NEW STUDENT RECORD.") 
    print("3. SEARCH STUDENT DETAILS.") 
    print("4. EDIT STUDENT DETAILS. ") 
    print("5. DELETE STUDENT DETAILS. ") 
    print("6. EXIT") 
    ans = int(input("Enter your choice :")) 
    print("\n")
    if ans == 1: 
        showAll() 
    elif ans == 2: 
        addStu() 
    elif ans == 3: 
        searchStu()
    elif ans == 4: 
        editStu()
    elif ans == 5: 
        delStu()   
    elif ans == 6: 
        print("\nlogging out...") 
        cn.close() 
        break 
    else: 
        print("NO SUCH CHOICE AVAILABLE." )

    