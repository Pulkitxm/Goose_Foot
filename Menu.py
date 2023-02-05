#Pulkit
import random,time,Function
from Function import pattern
def Menu(ch):
  if ch.upper() == 'SNACKS' or ch == '1':
    pattern()
    print('Sancks')
    pattern()
    for i in range(1,11):
        line = str(i)+')'+Function.item_name(i)+'(₹'+str(Function.item_price(i))+')'
        print(line)
    pattern()
  if ch.upper() == 'A LA CARTE' or ch == '2':
    pattern()
    print('a La Carte')
    pattern()
    for i in range(11,21):
        line = str(i)+')'+Function.item_name(i)+'(₹'+str(Function.item_price(i))+')'
        print(line)
    pattern()
  if ch.upper() == 'SWEET'or ch == '3':
    pattern()
    print('Sweet')
    pattern()
    for i in range(21,31):
        line = str(i)+')'+Function.item_name(i)+'(₹'+str(Function.item_price(i))+')'
        print(line)
    pattern()
  if ch.upper() == 'COMBOS'or ch == '4':
    pattern()
    print('Combos')
    pattern()
    for i in range(31,39):
        line = str(i)+')'+Function.item_name(i)+'(₹'+str(Function.item_price(i))+')'
        print(line)
    pattern()
#Pulkit
