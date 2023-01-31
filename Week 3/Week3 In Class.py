import csv

fName=[]
lName=[]
state=[]
email=[]
dept =[]
title=[]

rCount=0

with open("") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        fName.append(row[0])
        lName.append(row[1])
        state.append(row[2])
        email.append(row[3])
        dept.append (row[4])
        title.append(row[5])
        rCount+=1

print(f"Number of records processed: {rCount}\n")

size = len(fName)
for i in range(0,size):
    print('{:<15}{:<15}'.format(lName[i], fName[i]),'\n')

stateCount=0
st=input("Enter a state:")
for i in range(0,size):
    if (st == state[i]):
        stateCount+=1
print(f"The number of employees in {st} is: {stateCount}")
