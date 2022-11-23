# from OpeningPage import *
from tkinter import *
from tkinter import messagebox
from Licensing import LicenseHelper
from AESCrypto import PrpCrypt
import os
from pathlib import Path

def GenerateLicense(end_date,mac_addr):
    pc = PrpCrypt('keyskeyskeyskeys')
    oper = LicenseHelper()
    s=oper.generate_license(end_date,mac_addr)
    licenceresult = pc.encrypt(s)
    return licenceresult

def CreateLicenseDoc(result):
        
    cwd = os.getcwd()
    file_path = cwd + '/license.lic'
    with open(file_path, 'w', encoding='utf-8') as lic:
        lic.write(str(result))
        lic.close()
    # root = tk.Tk()
    # root.withdraw()
    messagebox.showinfo('my messagebox', 'Sucessfully Created License, You can now restart the program and use it.')


def CreateLicesePage():
    
    createlicensepage=Toplevel()
    createlicensepage.title('Create Licese Page')
    createlicensepage.geometry('925x500')
    createlicensepage.config(bg='white')
    heading=Label(createlicensepage,text='User Input License',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
    heading.pack()
    
    #user input result from me
    userinput = Entry(createlicensepage,width=50,length=50,fg='black',bg="white",font=('Microsoft YaHei UI Light',11))
    userinput.pack()


    def getresult():
        result=userinput.get()
        CreateLicenseDoc(result)
        
    button=Button(createlicensepage,width=39,pady=7,text='Submit',bg= '#57a1f8',fg='white',border=0,command=getresult)
    button.pack()

        
def CheckLicensing():
    #check if .lic exit
    cwd = os.getcwd()
    file_path = cwd + '/license.lic'
    
    my_file=Path(file_path)
    if not my_file.is_file():
        messagebox.showinfo('my messagebox', 'No License, Create Now')
        CreateLicesePage()
        return
    
    #read .lic file
    
    
    with open(file_path, 'r') as license_file:
        license_result = license_file.read()
    #
    
    pc = PrpCrypt('keyskeyskeyskeys')
    license_str = pc.decrypt(license_result)
    oper = LicenseHelper()
    license_dic = oper.read_license(license_str)
    return license_dic
    
