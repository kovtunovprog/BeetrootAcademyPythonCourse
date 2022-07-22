# Extend Phonebook application

# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name 
# Search by telephone number 
# Search by city or state 
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
 
# The first argument to the application should be the name of the phonebook. 
# Application should load JSON data, if it is present in the folder with application, 
# else raise an error. After the user exits, all data should be saved to loaded JSON.


import json
from os import path


def save_file(data):
    with open ('./lesson 11/task2/Phonebook.json', 'w') as f:
        json.dump(data, f, indent=2)

def delete(isUpdate):
    phone = input('What number we need to find: ')
    f =  open ('./lesson 11/task2/Phonebook.json', 'r')
    json_list = json.load(f)
    list_without_phone = json_list
    not_found = True
    for x in json_list:
        if x['telephone']==phone:
            not_found = False
            list_without_phone.remove(x)
            if not isUpdate:
                print('phone number disappeared')
    if not_found:
        print('not found')
    save_file(list_without_phone)

def update():
    delete(True)
    add_entry()

def search_by():
    print('What type of field u wanna to check: first_name, last_name, full_name, telephone, city?')
    search_field_type = input('Please enter one field type: ')
    if search_field_type == 'first_name':
        pass
    elif search_field_type == 'last_name':
        pass
    elif search_field_type == 'full_name':
        pass
    elif search_field_type == 'telephone':
        pass
    elif search_field_type == 'city':
        pass
    else:
        print('Please enter correct field type =)')
        search_by()
        return
    search_field = input('Please enter one field: ')
    f =  open ('./lesson 11/task2/Phonebook.json', 'r')
    json_list = json.load(f)
    not_found = True
    for x in json_list:
        if x[search_field_type]==search_field:
            not_found = False
            print(str(x))
    if not_found:
        print('not found')

def add_entry():
    first_name = input('Enter ur firts name: ')
    last_name = input('Enter ur last name: ')
    full_name = input('Enter ur full name: ')
    telephone = input('Enter ur telephone number: ')
    city = input('Enter ur city: ')
    data = {'first_name': first_name, 'last_name': last_name, 'full_name': full_name, 'telephone': telephone, 'city':city}
    with open ('./lesson 11/task2/Phonebook.json', 'r') as f:
        newJ = json.load(f)
        newJ.append(data)
    save_file(newJ)

def app_mainscreen():
    if path.isfile('./lesson 11/task2/Phonebook.json') is False:
        raise Exception("File not found")
    print('What action do u want: add, search, delete, update, close?')
    action = input('Please enter type of action: ')
    if action == 'add':
        add_entry()
    elif action == 'search':
        search_by()
    elif action == 'delete':
        delete(False)
    elif action == 'update':
        update()
    elif action == 'close':
        return
    else:
        print('Please enter correct action type =)')
        app_mainscreen()
        return
     
app_mainscreen()
