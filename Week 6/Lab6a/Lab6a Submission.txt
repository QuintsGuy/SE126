# Tristan Knott
# Week 6 Lab 6a
#
# Variables Used:
# file                  stores csv file from input into function
# report                stores csv information from file into lists
# search_name           stores input of name user wants to search for
# min                   stores minimum value
# max                   stores value of length of list last_name
# guess                 stores the result of min+max/2 cast as an integer
# size                  stores value of length of list first_name
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

def find_person_binary():
    search_name = input("Enter a person's last name: ").lower()
    min = 0
    max = len(last_name)
    guess = int((min + max)/2)

    while(search_name != last_name[guess].lower() and min <= max):
        if (search_name < last_name[guess].lower()):
            max = guess -1
        else:
            min = guess + 1
        guess = int((min + max)/2)

    if (search_name == last_name[guess].lower()):
        print('Name is found.')
    else:
        print('Name is not found.')

    print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format('Last', 'First', 'Phone', 'Email', 'Department', 'Position'))
    print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format(last_name[guess], first_name[guess], phone_number[guess], email_address[guess], department[guess], position[guess]))


def display_spreadsheet():
    size = len(first_name)
    print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format('Last', 'First', 'Phone', 'Email', 'Department', 'Position'))
    for i in range(size):
        print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format(last_name[i], first_name[i], phone_number[i], email_address[i], department[i], position[i]))

first_name = []
last_name = []
phone_number = []
email_address = []
department = []
position = []

csv_file = str(input(r"Please enter a file path: "))
get_file(csv_file)

find_person_binary()
