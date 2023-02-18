# Tristan Knott
# Week 6 Lab 5b
#
# Variables Used:
# file                  stores csv file from input into function
# report                stores csv information from file into lists
# size                  stores the length of first name
# perform_action        stores response of whether y/n to perform function
# menu_selection        stores response of what action to perform
# look_up               stores last name of the person you're trying to find
# change_counter        stores number of changes that took place
# select_department     stores the department user wishes to change emails from
# topo_level_domain     stores user input of what TLD to change the emails to
# first_name            stores lists of first names derived from csv_file
# last_name             stores lists of last names derived from csv_file
# phone_number          stores lists of phone numbers derived from csv_file
# email_address         stores lists of emails derived from csv_file
# department            stores lists of departments derived from csv_file
# position              stores lists of positions derived from csv_file
# csv_file              stores inputed csv_file to be used in function
#
# ==========================================================================================

import csv

def get_file(csv_file):
    with open(csv_file) as f:
        personnel=0
        file = csv.reader(f)
        report = list(file)
        for row in report:
            first_name.append(row[0])
            last_name.append(row[1])
            phone_number.append(row[2])
            email_address.append(row[3])
            department.append(row[4])
            position.append(row[5])
            personnel+=1
        
        display_spreadsheet()
        print(f"\nNumber of personnel records processed: {personnel}") 

        perform_an_action()

def display_spreadsheet():
    size = len(first_name)
    print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format('Last', 'First', 'Phone', 'Email', 'Department', 'Position'))
    for i in range(size):
        print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format(last_name[i], first_name[i], phone_number[i], email_address[i], department[i], position[i]))

def perform_an_action():
    perform_action=input("\nWould you like to perform any actions? Y/N: ").upper()
    while perform_action==str(perform_action):
        if perform_action=="Y":
            run_menu()
        elif perform_action=="N":
            print("Goodbye...\n")
            break
        else:
            print("Invalid input -- try again")

def run_menu():
    print("Welcome to the actions menu!\n")
    print("1 -- Personnel Data Finder")
    print("2 -- Validate Record Existence")
    print("3 -- Change Personnel Email")
    while True:
        menu_selection = int(input('\nPlease select which action you would like to perform: '))
        if menu_selection == 1:
            find_person_sequential()
        elif menu_selection == 2:
            find_person_binary()
        elif menu_selection == 3:
            email_change()
        else:
            print('Invalid selection -- Please try again')
            continue

def find_person_binary():
    searchName = input("Enter a person's last name: ").lower()

    min = 0
    max = len(last_name)
    guess = int((min + max)/2)

    while(searchName != last_name[guess].lower() and min <= max):
        if (searchName < last_name[guess].lower()):
            max = guess -1
        else:
            min = guess + 1
        guess = int((min + max)/2)

    if (searchName == last_name[guess].lower()):
        print('Name is found.')
    else:
        print('Name is not found.')

    perform_an_action()

def find_person_sequential():
    look_up = input("Enter a person's last name: ").lower()
    for i in range(0, len(first_name)):
        if look_up == last_name[i].lower():
            print(f"\nFound it! The person you're looking for is:")
            print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format('Last', 'First', 'Phone', 'Email', 'Department', 'Position'))
            print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format(last_name[i], first_name[i], phone_number[i], email_address[i], department[i], position[i]))
    
    perform_an_action()

def email_change():
    change_counter=0
    select_department = input('\nPlease enter the department you would like to alter: ')
    top_level_domain = input('Please enter the top level domain you would like to alter: ')
    for i in range(0, len(first_name)):
        if department[i]==select_department:
            email_address[i] = email_address[i][0:-4] + top_level_domain
            change_counter+=1
    display_spreadsheet()
    print(f"\nThere were {change_counter} emails altered by this action...\n")
    perform_an_action()

first_name = []
last_name = []
phone_number = []
email_address = []
department = []
position = []

csv_file = str(input(r"Please enter a file path: "))
get_file(csv_file)
