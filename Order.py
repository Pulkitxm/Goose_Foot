#Pulkit
from Riya import randompicker
from Function import *
from Control import *
import Menu as Menu
import Function as Function
import random,os,time
from datetime import datetime
def pattern():
    for i in range(lenofline):
        print('-',end='')
        time.sleep(.0001)
def Order_snacks():
    Snack=Input('Snacks ?  - ')
    freq=float(Input(item_name(Snack)+'  X '))
    d=item_price(Snack)
    return Snack,d*freq,freq

def Order_alacarte():
      Main=Input('Main Course ? - ')
      freq=float(Input(item_name(Main)+'  X '))
      d=item_price(Main)
      return Main,d*freq,freq

def Order_sweet():
    Sweet=Input('Some Sweet ? - ')
    freq=float(Input(item_name(Sweet)+'  X '))
    d=item_price(Sweet)
    return Sweet,d*freq,freq

def Order_combo():
    Combo=Input('Any Combo ? - ')
    freq=float(Input(item_name(Combo)+'  X '))
    d=item_price(Combo)
    return Combo,d*freq,freq

def Order(number=9654950988,Name='Pulkit'):
  Bill , Items_index , Bill_List = 0 , [] , []
  Print('Our Menu')
  Print('1) Snacks')
  Print('2) a la carte')
  Print('3) Sweet')
  Print('4) Combos')
  
  while True:
    print()
    ch = Input('What would you like to have (to skip simply press enter) ? - ')
    if ch=='1':
        print()
        Menu.Menu('1')
        while True:
            Snack,Amount,freq=Order_snacks()
            Bill+=Amount
            Bill_List.append(freq)
            Items_index.append(Snack)
            s=Input('Would you like to have more snacks(yes/no) -')
            if s[0] in 'nN':
              break
            elif s[0] in 'yY':
                pass
            else:
              Print('Enter yes/no')

    elif ch=='2':
        print()
        Print("Remember the best things to fill up your tummy is chapati")
        Menu.Menu('2')
        while True:
            Main,Amount,freq=Order_alacarte()
            Bill+=Amount
            Bill_List.append(freq)
            Items_index.append(Main)
            s=Input('Would you like to have more snacks(yes/no) -')
            if s[0] in 'nN':
              break
            elif s[0] in 'yY':
                pass
            else:
              Print('Enter yes/no')
    elif ch=='3':
        print()
        Print('खाने के बाद कुछ मेठा हो जाए ?')
        Menu.Menu('2')
        while True:
            Sweet,Amount,freq=Order_sweet()
            Bill+=Amount
            Bill_List.append(freq)
            Items_index.append(Sweet)
            s=Input('Would you like to have more snacks(yes/no) -')
            if s[0] in 'nN':
              break
            elif s[0] in 'yY':
                pass
            else:
              Print('Enter yes/no')
    elif ch=='4':
        Menu.Menu('2')
        while True:
            Combo,Amount,freq=Order_combo()
            Bill+=Amount
            Bill_List.append(freq)
            Items_index.append(Combo)
            s=Input('Would you like to have more snacks(yes/no) -')
            if s[0] in 'nN':
              break
            elif s[0] in 'yY':
                pass
            else:
              Print('Enter yes/no')
    elif ch== '':
        break
    else:
        print('Invalid choicee')
  import time  
  Print()
  gst=0.05*Bill
  gst=int(gst)
  Print('Searhing for restaurants.......Be Patient')  
  for i in range(15):
      print('■',end='')
      time.sleep(.8)
  print()
  Print('Yay Found some restaurants')
  Print()
  restaurants = ['Foodforia', 'Eativo', 'VitaPlate', 'Foodatory', 'ForkFresh', 'Foodzito', 'UpMunch', 'FoodCue', 'FinestPlate', 'OnlineGrub', 'BlueApron', 'Eat24', 'Foodler', 'GrubMarket', 'Deliveroo', 'FoodGenius', 'Munchery', 'Sprig', 'InstaCart', 'Plated', 'HomeChef', 'SmartLunches', 'PurpleCarrot', 'SpoonRocket', 'Starbelly', 'Goosefoot', 'The Test Kitchen', 'The French Laundry', 'Hof van Cleve', 'A Casa do Porco', 'Hiša Franko', 'Sühring', 'Chi Spacca', 'Alinea', 'Le Bernardin']
  used_index=[]
  index = random.randint(1,35)
  pattern()
  Print('Restaurants'+' '*12+'Price for your items')
  pattern()
  Selected=[]
  for i in range(1,11):
      if i==10:
          print(i,end= ' ')
      else:
          print(i,end='  ')
      while index in used_index:
          index = random.randint(0,34)
      used_index.append(index)
      item = restaurants[index]
      space = (20 - len(item))*' '
      rest_Bill = Bill- (random.randint(1,10)+float(str(random.random())[:4]))
      line = item+ space +'₹'+ str(rest_Bill)
      Print(line)
      Selected.append([i,item,rest_Bill])
  Print()
  pattern()
  Min=Selected[0][2]
  Min_name=Selected[0][1]
  for i in Selected:
      if i[2]<Min:
          Min=i[2]
          Min_name=i[1]
    
  Print('Best Choice - '+Min_name)
  restaurant_chosen = Input('Enter index of restaurant you would like to go for (for chosing '+Min_name+' you can simply press enter) - ')
  if restaurant_chosen =='':
      restaurant_chosen = Min_name
      Bill = Min
  else:
      index = int(restaurant_chosen)
      for i in Selected:
          if i[0]==index:
              restaurant_chosen = i[1]
              Bill = i[2]
  Print('Contacting '+restaurant_chosen)
  for i in range(15):
      time.sleep(.8)
      print('■',end='')
  print()
  Print(restaurant_chosen+' is ready to accept the order  ✓')
  pattern()

  Print()
  Print('Sir / Madam your bill is ready , please pay the amount to take your meal at the soonest')
  print('Ordered fom '+restaurant_chosen)
  print('Name - ',Name)
  print('Contact number - ',number)
  print('Total Amount - ',Bill)
  print('Items Selected -:',)
  for i in range(len(Items_index)):
    index=Items_index[i]
    print(i,Bill_List[i],' X '+Function.item_name(index),Function.item_price(index)*Bill_List[i])
  print('Total - ',int(Bill),'+',gst,'(gst) =',(int(Bill)+gst))
  Bill=Bill+gst
  Bill_1=Bill
  print()
  ch=Input("Do you want to redeem a code (yes/no) - ")
  c=True
  if ch[0] in 'yY' :
    while c:
      a=Input('Please enter a redeem code(Enter your name) - ')
      isreedeemed=False
      if Bill>700:
        if a == 'Pulkit':
          Bill-=500
          Print('Code redeemed Successfully')
          c=False
        else:
          print('''Try Name Pulkit''')
      else:
        print('Sorry your Code could not be redeemed since your bill is less than ₹700 (',Bill,')')
        c=False
  print()
  print('Name - ',Name)
  print('Contact number - ',number)
  print('Total Amount - ',Bill)
  print('Items Selected -:',)
  for i in range(len(Items_index)):
    index=Items_index[i]
    print(i,Bill_List[i],' X '+Function.item_name(index),Function.item_price(index)*Bill_List[i])
  print('Total - ',int(Bill)+500,'- 500 =',(int(Bill)))
  Bill=Bill+gst
  Bill_1=Bill

  now = datetime.now()
  details= str(now)[:11] + ' around ' + str(now)[11:17] 
  
  today = now.day
  time = now.strftime("%H:%M")
  date = today + 5
  ispaid=None
  if len(str(number))==10:
    print('How would you like to pay-:')
    print('1)Cash on Delivery')
    print('2)From our bank service(Suggested)')
    ch_pay=Input('Enter your choice-')
    if ch_pay=='1':
        Modeofpayment='COD'
        print("You will recieve your order within 45 minutes")
        print('Congratulations you also win a ₹1000 voucher(Note-Valid till',date,'date, ie 5 days from now)')
    elif ch_pay=='2':
        Modeofpayment='COD'
        print('This function is still under Developement')
        print("You will recieve your order within 45 minutes")
        print('Congratulations you also win a ₹1000 voucher(Note-Valid till',date,'date, ie 5 days from now)')
  Print('Searching for your delivery Partner')
  import time
  rec = randompicker()
  for i in range(15):
      time.sleep(.8)
      print('■',end='')
  print()
  Print('Your delivery partner is is dispatched  ✓')
  print('ID -',rec[0])
  print('NAME -',rec[1])
  print('GENDER -',rec[2])
  print('DOB -',rec[3])
  print('ADDRESS -',rec[4])
  print('EDUCATION -',rec[5])
  print('SALARY -',rec[6])
  print('STARS -',rec[7])
  print('WORK EXPIRIENCE -',rec[8])
  print('NOOTN -',rec[9])
  print('NOC -',rec[10])
  print('Tip -',rec[11])

  if True: 
     ch=Input('Would you like to download order reciept ? (y/n) -')
     if ch[0] in 'yY':
         reciept = open(Desktop+'/reciept.txt','w')
         reciept.write('---------------GooseFoot------------\nOrdered on '+details+'\n')
         reciept.write('Name - '+Name+'\n')
         reciept.write('Ordered fom '+restaurant_chosen+'\n') 
         reciept.write('Contact number - '+str(number)+'\n')
         reciept.write('Total - ' + str(int(Bill)) + '+' + str(gst) + '(gst) =' + str(Bill) + '\n')
         if ch_pay=='1':
             ispaid='Paid on delicery'
             reciept.write('Mode of payment - Cash on Delicey')
         elif ch_pay=='2':
             if ispaid==True:
                 ispaid='Paid online'
                 reciept.write('Mode of payment - Bank\nStatus of Payment - Paid')
         else:
             ispaid='Paid on Delivery not online'
             reciept.write('Mode of payment - Bank\nStatus of Payment - not Paid')
         reciept.close()
         os.system('start '+Desktop+'/reciept.txt')
     dateoftoday = str(now)[:11]
     return dateoftoday,Items_index,Bill,ispaid,Modeofpayment
  else:
    print('Invalid number')
#Pulkit
