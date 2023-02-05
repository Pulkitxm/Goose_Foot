#Pulkit
import time
# Functions related to Menus Prices etc
Items_Name=['Dahi ke sholley','Allo Tikki', 'Bun Tikki', 'Matar Kulcha', 'Papadi Chaat', 'Bhalla Papadi', 'Special Dahi bhalle',
      'Cholley Bhature', 'Pao Bhaji', 'Raj Kachhori','Mix veg', 'Dal Makhani', 'Panner Gravy', 'Rice Plain', 'Tandoori Roti',
      'Butter Roti', 'Allo Parantha', 'Paneer Parantha', 'Butter Naan', 'Garlic Naaan', 'Coke', 'Rasgulla', 'Jalebi',
      'Gajar Halwa', 'Gulab Jamun', 'Lassi', 'Rasmallai', 'Kheer', 'Chocolate Shake', 'Milk Shake',
      'Combo - 1 [ Cholley Bhature + Gajar Halwa + Coke ]',
      'Combo - 2 [ Garlic Naan(2) + Paneer Gravy + Dal Makhani + Gulab Jamun ]',
      'Combo - 3 [ Butter Roti(2) + Mix Veg + Rice Plain + Dal + Kheer ]',
      'Combo - 4 [ Pao Bhaji + Chocolate Shake + Jalebi ]',
      'Combo - 5 [ Allo Parantha + Dal Makhani + Rasmallai ]', 'Combo - 6[ Matar Kulcha + Coke + Rasgulla ]',
      'Combo - 7 [Butter Naan(2) + Rice Plain + Mix Veg + Paneer Gravy + Lassi + Rasgulla + Gulab Jamun ]',
      'Combo - 8 [Tandoori Roti + Dal Makhani + Mix  Veg + milk Shake + Gajar Halwa ]']
Items_Price=[200,88,60,115,120,120,115,150,150,130,260,300,300,105,30,45,90,105,60,85,45,12,50,200,25,50,40,79,
       350,200,700,700,700,700,700,700,700,700]
def item_price(a):
    if a==0:
      return Items_Price[0]
    else:
      return Items_Price[int(a)-1]
    
def item_name(a):
  if a==0:
    return Items_Name[0]
  else:
    return Items_Name[int(a)-1]
    
# Functions to enhance the presentation
from Control import Speed,Speed_pattern,lenofline

def Input(Message,speed=Speed):
    for i in Message:
        if i.isspace() == True:
            print(i,end='')
        else:
            print(i,end='')
            time.sleep(speed) 
    return input()

def Print(a='',End='newline',speed=Speed):
    if a=='':
        print()
    else:
        for i in a:
            if i.isspace()==False:
                print(i,end='')
                time.sleep(speed)
            else:
                print(i,end='')
        print()
    if End != 'newline':
        print()

def pattern(speed=Speed_pattern):
    for i in range(lenofline):
        print('-',end='')
        time.sleep(speed)
    
#Pulkit
