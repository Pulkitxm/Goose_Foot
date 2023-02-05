from Pulkit import *
from Control import *
import Signin as Signin
from Naman import *
pattern()
Print()
Print('Welcome to '+Company_name)
pattern()
Print()
Print()
Print('To continue on '+Company_name+' you need to Sign in/up ')
Print('Moving to Signup/login page')
Print()
number,Name,password=Signin.signin() # Signin.signin() is a function used to provide a sign - in / up option to the users


choice = Input('Would you like to Order a meal(m) or Use the customer service(c) - ')
if choice.lower() in 'mc':
    if choice.lower() == 'm':
        Pulkit(number,Name,password)
    else:
        Naman(number,Name)
