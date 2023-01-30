import csv

def find_person():
    look_up = input("Enter a person's last name: ")
    for i in range(0, len(age)):
        if look_up == last_name[i]:
            print(f"Found it! The person you're looking for is {first_name[i]} {last_name[i]} {age[i]}")

first_name = []
last_name = []
age = []

with open("") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        first_name.append(row[0])
        last_name.append(row[1])
        age.append(row[2])

flag = -1
i=0

found_person = find_person()

while i<len(last_name) and found_person.lower()!=last_name[i].lower():
    i+=1

if i>=len(last_name):
    print("Record not found...")
else:
    print(f"{first_name} {last_name} {age}")