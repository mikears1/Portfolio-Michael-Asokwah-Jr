# File: L8q1.py
# Author: Michael Asokwah 
# Date: 11/8/2022
# Section: 506 
# E-mail: masokwah@tamu.edu  
# Description: 
# This program simulates an employee database, with the user able to
# add, look up, edit, or delete employees form the database. 




class employee():
    def __init__(self, name, id, jobtitle, department):
        self.name = name
        self.id = id
        self.jobtitle = jobtitle
        self.department = department

    def get_name(self):
        return(self.name)
    
    def get_id(self):
        return(self.id)
    
    def get_jobtitle(self):
        return(self.jobtitle)
    
    def get_department(self):
        return(self.department)
    
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def set_jobtitle(self, jobtitle):
        self.__jobtitle = jobtitle


case = 0
dic_emp = {}

while (case != 5):
    print('*******************Main Menu*****************')
    print('1. Add Employee')
    print('2. Look up Employee')
    print('3. Edit Employee')
    print('4. Delete Employee')
    print('5. Quit')
    print('**********************************************\n')
    case = int(input('Please input choice '))
    if case == 1:
        el= employee(None,None,None,None)
        el.name = input('Enter Name: ')
        el.id = input('Enter id: ')
        el.jobtitle = input('Enter Job Title: ')
        el.department = input('Enter Department: ')
        dic_emp[el.get_name()] = el
        dic_emp[el.get_id()] = el
        dic_emp[el.get_jobtitle()] = el
        dic_emp[el.get_department()] = el
        print('Added!')

    if case == 2:
        id = input('Enter id: ')
        if id in dic_emp:
            el = dic_emp[id]
            print('Employee name:', el.get_name())
            print('Employee Job Title:', el.get_jobtitle())
            print('Employee department:', el.get_department())
        else:
            print('Not found')

    if case == 3: 
        id = input('Enter id: ')
        if id in dic_emp:
            el = dic_emp[id]
            el.name = input('Enter Name: ')
            el.jobtitle = input('Enter Job Title: ')
            el.department = input('Enter Department: ')
            dic_emp[el.get_name()] = el
            dic_emp[el.get_id()] = el
            dic_emp[el.get_jobtitle()] = el
            dic_emp[el.get_department()] = el
            print('Information updated')

    if case == 4:
        id = input('Enter id: ')
        if id in dic_emp:
            del dic_emp[id]

        else:
            print('Not found')

    if case == 5:
        print('Thank you for using the application!')
        break 

    
     
     
