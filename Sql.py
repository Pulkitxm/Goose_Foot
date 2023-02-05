#Pulkit
import mysql.connector
from Control import *

def create_table(db_cursor):
  Command = "create table "+Table+"(serial_no int auto_increment Primary Key , Name varchar(20) , Mobile varchar(10) , Date varchar(20) , Items varchar(1000) , Bill varchar(15) , Status_of_Payment varchar(100) , password varchar(25) , ModeofPayment varchar(10))"
  db_cursor.execute(Command)
  
def Insert(Name,Mobile,Date,Items,Bill,ispaid,Pass,Modeofpayment):
  db_cursor.execute("insert into %s values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s') "%(Table,Name,Mobile,Date,','.join(Items),Bill,ispaid,str(Pass),Modeofpayment))

# creating database_cursor to perform SQL operation
db_connection = mysql.connector.connect(host= "localhost",user= "root",password= "root")
db_cursor = db_connection.cursor()

def enter_records(Name = 'Pulkit' , Mobile = 9818525576 , Date = '2021-11-30 ' , Items = ['1', '11', '21', '31'] , Bill = 825.0 , ispaid = 'Paid on delicery' , Pass = 'astrongone' , Modeofpayment = 'COD'):
  db_cursor.execute('show databases')
  if (Database,) not in db_cursor.fetchall():
    db_cursor.execute('create database '+Database)
    db_cursor.execute('use '+Database)
    create_table(db_cursor)
  else:
    db_cursor.execute('use '+Database)
    db_cursor.execute('show tables')
    if (Table,) not in db_cursor.fetchall():
      create_table(db_cursor)
  Insert(Name,Mobile,Date,Items,Bill,ispaid,Pass,Modeofpayment)
  db_connection.commit()
  db_connection.close()
#Pulkit
