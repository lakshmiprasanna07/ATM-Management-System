import tkinter
from tkinter import *
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect("test.db")

#create the table
conn.execute("""CREATE TABLE IF NOT EXISTS DATA
           (id INT PRIMARY KEY NOT NULL,
           cardnumber TEXT NOT NULL,
           pin TEXT NOT NULL,
          balance REAL);""")

def login():
#create data for database
#conn.execute("INSERT INTO DATA (id,cardnumber,pin,balance) \
   # VALUES (1,"64445298794","2004",78000.0)");
#conn.execute("INSERT INTO DATA (id,cardnumber,pin,balance) \
      #VALUES (2,"64445298795","2005",88000.0)");
    #conn.execute("INSERT INTO DATA (id,cardnumber,pin,balance) \
        #VALUES (4,'64445298745','2002',89000.0)");

#checks whether account number and pin are matched or not
    cursor=conn.execute('SELECT cardnumber,pin FROM DATA where cardnumber=? AND pin=?',(e.get(),e1.get()) )            
    row=cursor.fetchone()
    if row:
        options()
    else:
               # if account number and entered pin are not matched then the transaction would be failed
        messagebox.showinfo("info","Transaction failed")
        exit
    cursor=conn.execute('SELECT balance FROM DATA where cardnumber=? AND pin=?',(e.get(),e1.get()))
    global balance
    balance=cursor.fetchone()
    conn.commit()
    #conn.close()
    
def options():
    global screen3
    screen3=Toplevel(root)
    screen3.geometry("750x500")
    screen3.title("Select Transcation")
    Label(screen3,text="SELECT TRANSACTION").grid(row=0,column=2,padx=100,pady=20)
    depo=Button(screen3,text="DEPOSIT",width="30",height="2",command=deposit).grid(row=1,column=0,padx=20,pady=20)
    trans=Button(screen3,text="TRANSFER",width="30",height="2",command=transfer).grid(row=2,column=0,padx=20,pady=20)
    cashwithdrawl=Button(screen3,text="CASH WITHDRAWL",width="30",height="2",command=withdrawl).grid(row=1,column=2,padx=40,pady=20)
    balanceenquiry=Button(screen3,text="BALANCE ENQUIRY",width="30",height="2",command=balance_enquiry).grid(row=2,column=2,padx=40,pady=20)


def withdrawl():
    global screen6
    screen6=Toplevel(screen3)
    screen6.geometry("750x500")
    screen6.title('withdrawl')
    Label(screen6,text='    PLEASE SELECT YOUR ACCOUNT',anchor=CENTER).grid(row=0,column=1,pady=20)
    savings=Button(screen6,text='SAVINGS',width='30',height='2',command=savings_account).grid(row=2,column=3,padx=40,pady=20)

def savings_account():
    global amountEntry
    global user_in
    user_in=IntVar()
    screen5=Toplevel(screen6)
    screen5.geometry("750x500")
    Label(screen5,text='Amount').grid(row=1,padx=25,pady=15)
    amountEntry=Entry(screen5,width=50,textvariable=user_in)
    amountEntry.grid(row=1,column=1)
    con1=Button(screen5,text='CONTINUE',padx=30,command=amountDeduct)
    con1.grid(row=2,column=1,pady=25)


def amountDeduct():
    global amo
    am=amountEntry.get()
    bal1=balance[0]
    amo=float(bal1)-float(am)
    query='UPDATE data SET balance=? WHERE cardnumber=?'
    binding=(amo,e.get())
    global abc
    abc=conn.execute(query,binding)
    conn.commit()
    global screen7
    screen7=Toplevel(screen3)
    screen7.geometry("750x500")
    Label(screen7,text='Do you want to display Balance',font='30',anchor=CENTER).grid()
    Button(screen7,text='YES',width='30',height='2',command=yes).grid(row=1,column=1,padx=40,pady=20)
    Button(screen7,text='NO',width='30',height='2',command=no).grid(row=2,column=1,padx=40,pady=20)

def yes():
    screen7=Toplevel(root)
    screen7.geometry('500x500')
    Label(screen7,text=' YOUR BALANCE IS :').grid(pady=10)
    Label(screen7,text=amo,font=50).grid(row=1)
    Button(screen7,text='Next',height='2',width='20',command=no).grid(row=2,column=1,padx=30,pady=20)
    
def no():
    screen8=Toplevel(root)
    screen8.geometry("500x500")
    Label(screen8,text='Your Transaction Is Successfully Completed',font='30',anchor=CENTER).grid(row=1,column=1,padx=40,pady=20)
    Button(screen8,text='QUIT',width='30',height='2',command=remove_allScreens).grid(row=2,column=1,padx=40,pady=20)
    
def hello():
    acc_dep=e2.get()
    bala=e3.get()
    query='SELECT balance FROM data WHERE cardnumber=?'
    bindings=(acc_dep,)
    result=conn.execute(query,bindings)
    results=result.fetchall()
    res=results[0]
    re=res[0]
    bal=float(re)+float(bala)
    Label(screen4,text='BALANCE IS DEPOSITED').grid(row=3)
    query1='UPDATE data SET balance=? WHERE cardnumber=?'
    binding=(bal,acc_dep)
    ab=conn.execute(query1,binding)
    conn.commit()
    Button(screen4,text='Next',height='2',width='20',command=no).grid(row=4,column=1,padx=30,pady=20)

def deposit():
    global screen4
    screen4=Toplevel(root)
    screen4.geometry("500x500")
    screen4.title("Deposit")
    Label(screen4,text='PLEASE ENETR ACCOUNT NUMBER AND BALANCE',font=("calibri"),anchor=CENTER).grid(row=0,column=1)
    global e2
    global e3
    user=StringVar()
    bal=DoubleVar()
    Label(screen4,text='Account number').grid(row=1,padx=25)
    e2=Entry(screen4,width=50,textvariable=user)
    e2.grid(row=1,column=1)
    Label(screen4,text='Balance').grid(row=2,pady=25)
    e3=Entry(screen4,width=50,textvariable=bal)
    e3.grid(row=2,column=1)
    enter1=Button(screen4,text='Continue',padx=20,pady=5,command=hello)
    enter1.grid(row=3,column=1)

def balance_enquiry():
    screen7=Toplevel(root)
    screen7.geometry('500x500')
    Label(screen7,text=' YOUR BALANCE IS :').grid(pady=10)
    Label(screen7,text=balance,font=50).grid(row=1)
    Button(screen7,text='Next',height='2',width='20',command=no).grid(row=2,column=1,padx=30,pady=20)

    
def transfer():
    global screen4
    screen4=Toplevel(root)
    screen4.geometry("500x500")
    screen4.title("Transfer")
    Label(screen4,text='PLEASE ENETR ACCOUNT NUMBER AND BALANCE',font=("calibri"),anchor=CENTER).grid(row=0,column=1)
    global e2
    global e3
    user=StringVar()
    bal=DoubleVar()
    Label(screen4,text='Account number').grid(row=1,padx=25)
    e2=Entry(screen4,width=50,textvariable=user)
    e2.grid(row=1,column=1)
    Label(screen4,text='Balance').grid(row=2,pady=25)
    e3=Entry(screen4,width=50,textvariable=bal)
    e3.grid(row=2,column=1)
    enter1=Button(screen4,text='Continue',padx=20,pady=5,command=transfer_deduct)
    enter1.grid(row=3,column=1)

    
def transfer_deduct():
    acc_dep=e2.get()
    bala=e3.get()
    query='SELECT balance FROM data WHERE cardnumber=?'
    bindings=(acc_dep,)
    result=conn.execute(query,bindings)
    results=result.fetchall()
    res=results[0]
    re=res[0]
    bal=float(re)+float(bala)
    Label(screen4,text='BALANCE IS TRANSFERRED').grid(row=3)
    query1='UPDATE data SET balance=? WHERE cardnumber=?'
    binding=(bal,acc_dep)
    ab=conn.execute(query1,binding)
    conn.commit()
    bal1=balance[0]
    amt=float(bal1)-float(bala)
    query='UPDATE data SET balance=? WHERE cardnumber=?'
    binding=(amt,e.get())
    abcd=conn.execute(query,binding)
    conn.commit()
    Button(screen4,text='Next',height='2',width='20',command=no).grid(row=4,column=1,padx=30,pady=20)

def remove_allScreens():
    e.delete(0,'end')
    e1.delete(0,'end')
    e.icursor(0)
    for widget in root.winfo_children():
        if isinstance(widget,tkinter.Toplevel):
            widget.destroy()

            
def main_screen():
    global root
    root=Tk()
    root.geometry("500x500")
    root.title("ATM services")
    label=Label(root,text="Please Enter Your Details",font=10,anchor=CENTER).grid(row=0,column=1,pady=20)
    user_input=StringVar()
    password_input=StringVar()
    global e
    global e1
    username=Label(root,text="Cardnumber")
    username.grid(row=1,column=0,padx=25)
    e=Entry(root,width=25,textvariable=user_input)
    e.grid(row=1,column=1)
    password=Label(root,text="Password")
    password.grid(row=2,column=0,pady=20)
    e1=Entry(root,width=25,textvariable=password_input,show='*')
    e1.grid(row=2,column=1)
    enter=Button(root,text="Enter",padx=20,pady=5,command=login).grid(row=4,column=1)
    root.mainloop()
main_screen()
