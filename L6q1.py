# File: L6q1.py 
# Author: Michael Asokwah
# Date: 10/20/2022 
# Section: 506 
# E-mail: masokwah@tamu.edu 
# Description: 
# This program simulates a grocery store, with the user able to add fruits and
# their prices, edit or delete those fruits, or search the story for added fruits. 




print('*******************Main Menu*****************')
print('1. Add fruits')
print('2. Edit fruit')
print('3. Delete fruit')
print('4. Search fruits')
print('5. Quit')
print('************************************************\n')

fruitall = {}
def addfruit():
    f1,f2 = input('Enter fruit followed by prices: ').split(', ')
    list1 = list(f2.split(' '))
    fruitname1 = f1
    k = len(list1)
    for i in range(0,k):
        list1[i] = float(list1[i])
        
    fruitall[fruitname1] = list1
    print('Current stock:',fruitall)

def editfruit():
    fn = input(str('Enter the fruit name: '))
    if fn in fruitall:
        f1 = input('Enter the fruit prices: ')
        list1 = f1.split()
        k = len(list1)
        for i in range(0,k):
            list1[i] = float(list1[i])

        fruitall[fn] = list1
        print('Current stock:',fruitall)
        

def deletefruit():
    e = str(input('If you want to remove all items enter all otherwise enter the fruit name. '))
    
          
    if e == 'all':
        fruitall.clear()
        print(fruitall)
    elif e in fruitall:
        fruitall.pop(e)
        print('Current stock:',fruitall)

def searchfruit():
    fs = input(str('Enter the fruit name: '))
    if fs in fruitall:
        prices = str(fruitall[fs])[1:]
        print(fs,'have',len(fruitall[fs]),'different prices of:',prices)
        print('Current stock:',fruitall)

a = 0
while a==0:
    
    n = int(input('Choose from menu: '))

    if n == 1:
        addfruit()

    if n == 2:
       editfruit()

    if n == 3:
       deletefruit()

    if n == 4:
        searchfruit()

    if n == 5:
        print('Current stock:',fruitall)
        a = a+1
    
    

        
