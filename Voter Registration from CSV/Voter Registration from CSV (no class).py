import csv

idList = []
ageList = []
regList = []
votedList = []

print("idList = ", idList)
print("ageList = ", ageList)
print("RegList = ", regList)
print("votedList = ", votedList)

with open(r"C:\Users\knott\OneDrive\Documents\GitHub\Python-Programs\Voter Registration from CSV\example.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        idList.append(row[0])
        ageList.append(int(row[1]))
        regList.append(row[2])
        votedList.append(row[3])

# Printing a list
print("ID =", idList, "\n")
print("age =", ageList, "\n")
print("Reg =", regList, "\n")
print("Voted =", votedList, "\n")

# Printing the size of each list
print("ID = ", len(idList))
print("age = ", len(ageList))
print("Reg = ", len(regList))
print("Voted = ", len(votedList))

items = len(idList)

for i in range(0,items):
    print(idList[i], ", ", ageList[i], ", ", regList[i], ", ", votedList[i])