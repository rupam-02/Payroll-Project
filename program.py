
import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',password='Riki@004',database='payroll')
if mycon.is_connected():
    print('Connected')
mycur=mycon.cursor()

def addreco():
    eid=int(input('Employee ID-:'))
    ename=input('Employee name-:')
    department=input("Employee's department-:")
    basic_salary=float(input('Basic Monthly Salary-:'))
    working_days=int(input('Number of working days this month-:'))
    HRA=basic_salary*0.2
    DA=basic_salary*0.5
    MA=basic_salary*0.1
    PF=basic_salary*0.12
    query="insert into payroll values({0},'{1}','{2}',{3},{4},{5},{6},{7},{8})".format(eid,ename,department,basic_salary,working_days,HRA,DA,MA,PF)
    mycur.execute(query)
    mycon.commit()


def displayreco():
    query='select * from payroll'
    mycur.execute(query)
    data=mycur.fetchall()
    print('%13s'%'Employee ID','%20s'%"Name",'%22s'%"Department",'%22s'%'Basic Salary','%28s'%'Working Days this month','%10s'%'HRA','%10s'%'DA','%25s'%'Medical Allowance','%15s'%'PF')
    print()
    print()
    for row in data:
        print('%13d'%row[0],'%20s'%row[1],"%22s"%row[2],'%22d'%row[3],'%28d'%row[4],'%30d'%row[5],'%15d'%row[6],'%25d'%row[7],'%15d'%row[8])
        print()


def searchreco():
    eid=int(input('Enter the employee ID to search-:'))
    query1='select * from payroll where eid={}'.format(eid)
    mycur.execute(query1)
    data=mycur.fetchall()
    if data==[]:
        print('Record not found')
    else:
        print('Record Found')
        print('%13s'%'Employee ID','%20s'%"Name",'%22s'%"Department",'%22s'%'Basic Salary','%28s'%'Working Days this month','%10s'%'HRA','%10s'%'DA','%25s'%'Medical Allowance','%15s'%'PF')
        print()
        for row in data:
            print('%13d'%row[0],'%20s'%row[1],"%22s"%row[2],'%22d'%row[3],'%28d'%row[4],'%30d'%row[5],'%15d'%row[6],'%25d'%row[7],'%15d'%row[8])
            print()

def modifyreco():
    eid=int(input('Enter the employee ID to modify-:'))
    query1='select * from payroll where eid={0}'.format(eid)
    mycur.execute(query1)
    data=mycur.fetchall()
    if data==[]:
        print('Record not found')
    else:
        ch=int(input('''
1. Employee ID
2. Employee Name
3. Department
4. Basic Monthly Salary
5. Working Days Per Year
Enter the corresponding number for the record u want to modify-:
'''))
        if ch==1:
            print('Modifying Employee ID...')
            eid1=int(input('Enter the new employee ID-:'))
            query="update payroll set eid={} where eid={}".format(eid1,eid)
            mycur.execute(query)
            mycon.commit()
        elif ch==2:
            print('Modifying Employee Name...')
            ename1=input('Enter the new name-:')
            query="upate payroll set ename='{}' where eid={}".format(ename1,eid)
            mycur.execute(query)
            mycon.commit()
        elif ch==3:
            print('Modifying Department...')
            dept1=input('Enter the new department name-:')
            query="upate payroll set department='{}' where eid={}".format(dept1,eid)
            mycur.execute(query)
            mycon.commit()
        elif ch==4:
            print('Modifying Basic Monthly Salary...')
            basic_salary1=float(input('Enter the new monthly salary-:'))
            HRA=basic_salary1*0.2
            DA=basic_salary1*0.5
            MA=basic_salary1*0.1
            PF=basic_salary1*0.12
            query="update payroll set basic_salary={},HRA={},DA={},medical_allowance={},PF={} where eid={}".format(basic_salary1,HRA,DA,MA,PF,eid)
            mycur.execute(query)
            mycon.commit()
        elif ch==5:
            print('Modifying Working Days Per Year')
            working_days1=int(input('Enter the number of working days per year-:'))
            query="update payroll set working_days={} where eid={}".format(working_days1,eid)
            mycur.execute(query)
            mycon.commit()
        else:
            print('Invalid Choice... Start again')
            modifyreco()
        query2='select * from payroll where eid={0}'.format(eid)
        mycur.execute(query2)
        data=mycur.fetchall()
        for row in data:
            if eid==row[0]:
                print('\nUpdated record-:','\nEmployee ID-:',row[0],'\nEmployee name-:',row[1],"\nEmployee's department-:",row[2],'\nMonthly Salary-:',row[3],'\nWorking Days Per Year-:',row[4],'\nHRA-:',row[5],'%','\nDA-:',row[6],'%','\nMedical allowance-:',row[7],'%','\nProvident Fund-:',row[8],'%',end='\n--------------------------')

def delreco():
    eid=int(input("Enter the Employee's ID corresponding to the record you want to delete-:"))
    query="delete from payroll where eid={}".format(eid)
    mycur.execute(query)
    mycon.commit()
    print('Record Deleted')

def salary_slip():
    eid=int(input('Enter the Employee ID of the respective emloyee-:'))
    query="select eid,ename,basic_monthly_salary,HRA,DA,medical_allowance,PF,basic_monthly_salary+HRA+DA+medical_allowance+pf,basic_monthly_salary+HRA+DA+medical_allowance FROM PAYROLL where eid=%d"%eid
    mycur.execute(query)
    data=mycur.fetchall()
    print('%13s'%'Employee ID','%17s'%"Name",'%22s'%'Basic Salary','%10s'%'HRA','%10s'%'DA','%25s'%'Medical Allowance','%15s'%'PF','%20s'%'Gross Salary','%20s'%'Net Salary')
    print()
    print()
    for row in data:
        print('%13d'%row[0],'%20s'%row[1],'%22d'%row[2],'%10d'%row[3],'%15d'%row[4],'%25d'%row[5],'%15d'%row[6],'%20d'%row[7],'%20d'%row[8])
        print()

while True:
    print('''
========================================
MENU''')
    ch=int(input('''
1. Add a record
2. Display a record
3. Search a record
4. Modify a record
5. Delete a record
6. Salary Slip
7. Exit
Enter your choice-:
'''))
    if ch==1:
        print('Adding a record...')
        addreco()
    elif ch==2:
        print('Displaying records...')
        displayreco()
    elif ch==3:
        print('Searching record...')
        searchreco()
    elif ch==4:
        print('Modifying record...')
        modifyreco()
    elif ch==5:
        print('Deleting record...')
        delreco()
    elif ch==6:
        print('The salary slip is...')
        salary_slip()
    elif ch==7:
        break
    else:
        print('Invalid Choice... Try again')
