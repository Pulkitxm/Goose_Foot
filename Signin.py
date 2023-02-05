#Pulkit
import random,os,string,time
from Function import *
from Control import *


def signin():
    def Password(): # formalities related to password management
        if a == 'i':
            while True:
                password = Input('Enter your password - ')
                if len(password) >= 5:
                        return password
                else:
                    print('Try  again !')
                    continue
        elif a=='u':
            while True:
                password = Input('Enter a strong password (enter / for suggestion) - ')
                if password == '/' :
                    import string,random
                    chars = list(string.ascii_letters + string.digits + '!@#$%&*()')
                    password=''
                    for i in range(10):
                        password+=random.choice(chars)
                    return password
                elif len(password) >= 5:
                    repassword = Input('Re-enter the password - ')
                    if password == repassword :
                        return password
                else:
                    continue
    def otp(): # This functions deals with otp management
        while True:
            otp=''
            for i in range(4):
              otp+=str(random.randint(0,10))
            file=open('otp.txt','w')
            file.write(Company_name+'\nYour otp is '+otp+' .Dont share it with anyone')
            file.close()
            os.system('start otp.txt')# opens otp file for user
            Num = str(number)[:2]+'......'+str(number)[-2:]
            inp_otp=input('Enter otp sent to your mobile number ('+Num+') - ')
            if inp_otp.strip()==otp:
                os.remove('otp.txt')
                if a=='i':
                    Print('Signed in Succssfully')
                    break
                elif a == 'u':
                    Print('Signed up succesfully')
                    break
            else:
                Print('invalid otp')
    Pass , num = False , False # Pass refers to corection of password and similarly numbers corresponds to mobile number
    pattern()
    Print('Please Sign/up to continue to '+Company_name)
    pattern()
    Name=Input('Enter your name - ')
    while True:
        a = Input('What do you wanna do Sign-in(i) or Sign-up(u) ? - ')
        if a=='i' : # Condition to check if user wants to Sign-in
            Print('Sign in to continue to '+Company_name)
            while  num != True and Pass != True :
                number=int(Input('Enter  you mobile number - +91'))
                if len(str(number))==10:
                    num = True # Indicates that user's number is correct
                    Pass = Password()
                    otp()
                else:
                  Print('Number not matched')
            break

        elif a=='u': # Condition to check if user wants to Sign-up
            Print('Sign up to continue to '+Company_name)
            number=int(Input('Enter your mobile number - +91'))
            if len(str(number))==10:
                num=True
                Pass =  Password()
                print('Your password is',Pass)
                otp()
            else:
              Print('Invalid Number')
            break
        else:
            Print('Invalid Choice')
        
    return number , Name , Pass # If the Sign-in/up process is finishd correctly then True is returned
#Pulkit
