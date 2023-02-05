def Naman(number=9999999999,Name='NAMAN'):
  import time
  from Control import lenofline
  print("-"*lenofline)
  print("HELLO "+Name+" WELCOME  TO  OUR  CUSTOMER  SERVICES")
  print("-"*lenofline)
  print()
  print("-"*lenofline)
  print("HERE  WE  WILL  LISTEN  YOUR  ISSUES  AND  TRY  OUR  BEST  TO  RESOLVE  THEM  AS  SOON  AS  POSSIBLE")
  print("-"*lenofline)
  print()

  while True:
    Complaint = ''
    print('\n1. if valet had misbehaved with you.\n2. if your order of delivery is delayed.\n3. if the seal of your item is find opened.\n4. if some items of your order are missing.\n5. if you didnt get the confirmation of your order has been booked but the payment has already done.\n6. if you are finding error or some other problems while doing payment\n7.  My Problem is not listed\n')
    x=int(input("How can we help you-->"))
    if x==1:
      valet=input("Enter the valet name which was hired for your delivery-->")
      print('Contacting our servers')
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      print()
      print("Thanks for waiting we have filled your complain against ",valet,"and sorry we will ensure that this will not happen again")
      Complaint = 'misbehaved with me'
      break

    elif x==2:
      valet=input("Enter the valet name which was hired for your delivery-->")
      Time = input('How much delay you faced - ')
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      Complaint = 'Order delayed by'+Time
      print('Sorry to hear this , We have informed '+valet+' and we ensure you that this will not happen again')
      print("Sorry for inconvenience, thanks for waiting")
      break
    
    elif x==3:
      valet=input("Enter the valet name which was hired for your delivery-->")
      restaurant=input("Enter the restaurant name from where you have ordered-->")
      time.sleep(3)
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      Complaint = 'Order from '+restaurant+' has found opened'
      print("Sorry for this inconvenience, from next time pls insure first that your food items are properly sealed before valet leaves") 
      print("You have got 70% discount on minimum order of ₹500")
      break

    elif x==4:
      valet=input("Enter the valet name which was hired for your delivery-->")
      restaurant=input("Enter the restaurant name from where you have ordered-->")
      n=int(input("Number of missing items-->"))
      for i in range(0,n):
        item1=input("Enter the name of missing-->")
        quan1=int(input("Quantity of item"))
      print('''We are checking that your full order was dispatched or not please wait (loading...)''')
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      Complaint = 'some items of your order are missing'
      print("Your full order was not dispatched from ",restaurant,", we are delivering you with free of cost of that missing items only....THANKS FOR PATIENCE")
      break

    elif x==5:
      valet=input("Enter the valet name which was hired for your delivery-->")
      res3=input("Enter the restaurant name from where you have ordered-->")
      pay1=input("Payment Method-->")
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      print('First please refresh the page and check the internet connection We are checking your order or your payment will be return in some while Please wait...')
      Complaint = 'didnt get the confirmation of your order has been booked but the payment has already done'
      print("Your order is confirmed details will be send you by email")
      break
    
    elif x==6:
      valet=input("Enter the valet name which was hired for your delivery-->")
      pay2=input("Payment Method-->")
      time.sleep(3)
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      Complaint = 'you are finding error or some other problems while doing payment'
      print('''We have checked our sites we didn't find any problems may be there is internet issue on your side please retry it or reopen our app
  or if possible please do the payment in cash...''')
      break
    
    elif x==7:
      valet=input("Enter the valet name which was hired for your delivery-->")
      Complaint = input('Enter your issue - ')
      for i in range(15):
        print('■',end='')
        time.sleep(.8)
      print("We apologise...for inconvinience")
      break
    else:
      print("Please choose correct number")
        
  import mysql.connector
  Name = 'root'
  Password =  'root'
  Database =  'customer' 
  Table = 'customer_care'


  db_connection = mysql.connector.connect(host= "localhost",user= "root",password= "root")
  db_cursor = db_connection.cursor()
  try:
    db_cursor.execute('create database '+Database)
    db_cursor.execute('use '+Database)
  except:
    db_cursor.execute('use '+Database)

  try:
    db_cursor.execute("create table customer_care (Name varchar(20) , Mobile varchar(10) , Valet varchar(40), Complaint varchar(2000));")
  except:
    pass
  db_cursor.execute("insert into customer_care values('%s','%s','%s','%s') "%(Name,number,valet,Complaint))
  db_connection.commit()
  print('Thanks for Joining GooseFoot')
