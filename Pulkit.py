#Pulkit
import Signin,Menu,time
import Order as Order
from Sql import enter_records
from Function import Print,pattern,Input
from Control import Company_name

def Pulkit(number=9818525576,Name='Pulkit',password='123456'):
    Print()
    Print('Moving to Main page of '+Company_name)
    pattern()
    line='Hello '+Name+' Welcome Back'
    Print(line)
    pattern()


    today , Items , Bill , ispaid , Modeofpayment = Order.Order(number,Name) # Accepting the user's order of edible items from the given menu + payment method
    # Enteing records in Sql
    enter_records(Name,str(number),today,Items,str(Bill),ispaid,password,Modeofpayment)
#Pulkit

