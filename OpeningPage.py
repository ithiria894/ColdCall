from tkinter import *
from tkinter import messagebox
from Licensing import LicenseHelper
from AESCrypto import PrpCrypt
import os
from LicensePage import *
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

img=PhotoImage(file='roboticF.png')
Label(root,image=img,bg='white').place(x=50,y=10)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in to ColdCall 神器',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
heading.place(x=30,y=5)

def licensingPage():
        screen=Toplevel()
        screen.title("Licensing")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        checkLicense=Label(screen,text='Check Licensing',bg='#fff',font=('Calibri(Body)',20,'bold'))
        checkLicense.place(x=10,y=10)
        CheckLicensing()
        screen.mainloop()#??

def signin():
    username=user.get()
    password=code.get()
    if username=='admin' and password=='1234':
        licensingPage()
    elif username!='admin' and password!='1234':
        messagebox.showerror('Invalid','invalid username and password')

#########.......................................................
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###########.....................................................
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
###############################################################
# Button(frame,width=39,pady=7,text='Sign in',bg= '#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

Button(frame,width=39,pady=7,text='licensingPage',bg= '#57a1f8',fg='white',border=0,command=licensingPage).place(x=35,y=204)

label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270) 
      
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand1',fg='#57a1f8')
sign_up.place(x=210,y=270)


root.mainloop()
# licensingPage()