#Login page
from prettytable import PrettyTable
global table
def information():
    global b
    b=[]
    a=int(input("Enter for how many employees you want to enter data: "))
    for i in range (a):
        d={}
        d["Email"]=str(input("Enter your email: "))
        d["Password"]=str(input("Enter your password: "))
        d["Name"]=str(input("Enter your name: "))
        d["Employee ID"]=str(input("Enter your employee id: "))
        b.append(d)
    
    table = PrettyTable()
    table.field_names = ["Name","Emp-ID", "Email", "Password"]
    for d in b:
        table.add_row([d["Name"],d["Employee ID"],d["Email"],d["Password"]])

    print(table)
def check():
    l=str(input("Have you logged in previously:"))
    if l=='YES' or "yes":
        y=str(input("Enter your name:"))
        for d in b:
            if d["Name"]==y:
                print("Data found")
                table = PrettyTable()
                table.field_names = ["Name","Emp-ID", "Email", "Password"]
                for d in b:
                    if d["Name"]==y:
                        table.add_row([d["Name"],d["Employee ID"],d["Email"],d["Password"]])
            print(table)
            break
        else:
            print("Data not found")
def login():
    j=str(input("Enter your email: "))
    k=str(input("Enter your password: "))
    for d in b:
        if d["Email"]==j and d["Password"]==k:
            print("Log in successful")
            break
    else:
        ("Invalid information.")

def removeitem():
    w=str(input("Enter name: "))
    for d in b:
        if d["Name"]==w:
            b.remove(d)
    table = PrettyTable()
    table.field_names = ["Name","Emp-ID", "Email", "Password"]
    for d in b:
        table.add_row([d["Name"],d["Employee ID"],d["Email"],d["Password"]])
    print(table)

information()
print("Press 1 for checking whether you have previously logged in or not")
print("Press 2 to login")
print("Press 3 to delete yor information from the list")
g=int(input("How many operation you want to perform: "))
for u in range (g):
    m=int(input("Enter your choice: "))
    if m==1:
        check()
    elif m==2:
        login()
    elif m==3:
        removeitem()
    else:
        print("Invalid oinformation.")


