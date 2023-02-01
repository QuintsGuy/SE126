import csv

def find_person(first_name, last_name, phone_number, email_address, department, position):
    look_up = input("Enter a person's last name: ").lower()
    for i in range(0, len(first_name)):
        if look_up == last_name[i].lower():
            print(f"\nFound it! The person you're looking for is:")
            print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format('Last', 'First', 'Phone', 'Email', 'Department', 'Position'))
            print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format(last_name[i], first_name[i], phone_number[i], email_address[i], department[i], position[i]))

def get_file(csv_file):
    with open(csv_file) as f:
        personnel=0
        file = csv.reader(f)
        report = list(file)
        print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format('Last', 'First', 'Phone', 'Email', 'Department', 'Position'))
        for row in report:
            first_name.append(row[0])
            last_name.append(row[1])
            phone_number.append(row[2])
            email_address.append(row[3])
            department.append(row[4])
            position.append(row[5])
            personnel+=1

        size = len(first_name)
        for i in range(size):    
            print('{:<15}{:<15}{:<20}{:<30}{:<20}{:<15}'.format(last_name[i], first_name[i], phone_number[i], email_address[i], department[i], position[i]))

        print(f"\nNumber of personnel records processed: {personnel}")

def find_another():
  while True:
    check_again=input("\nDo you want to lookup anyone else? Y/N: ").upper()
    try:
      check_again=str(check_again)
    except ValueError:
      print("Invalid input -- try again\n")  
    if check_again=="Y":
      return True
    elif check_again=="N":
      print("Goodbye...\n")
      return False
    else:
      print("Invalid input -- try again")

first_name = []
last_name = []
phone_number = []
email_address = []
department = []
position = []

csv_file = str(input(r"Please enter a file path: "))
get_file(csv_file)

while True:
    find_person(first_name, last_name, phone_number, email_address, department, position)
    if find_another() == False:
        break