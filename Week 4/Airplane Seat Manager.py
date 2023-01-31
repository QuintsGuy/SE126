seats = []

for i in range(7):
    seats.append(['A', 'B', 'C', 'D'])

assigned_seats = []

def display_seats():
    for i, row in enumerate(seats):
        print('{:<5}{:<3}{:<3}{:^3}{:<3}{:<3}'.format(i+1, row[0], row[1],"", row[2], row[3]))

def assign_seat(row, col):
    if seats[row][col] == "X":
        print("Seat already occupied.")
        return False
    else:
      seats[row][col] = "X"
      assigned_seats.append((row, col))
      return True

#needs work to return invalid statement when inputing enteries outside range
def get_seat():
    seat = input("\nEnter seat (e.g. 1A): ") 
    row = int(seat[0]) - 1
    col = ord(seat[1]) - 65
    if 0>row>6 or 0>col>3:
        print("Invalid seat -- try again\n")
        return None
    return (row, col)

def assign_another():
  while True:
    check_again=input("\nDo you want to assign anymore seats? Y/N: ").upper()
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

display_seats()
while len(assigned_seats) < 28:
  seat = get_seat()
  if seat == None:
    continue
  else:  
    if assign_seat(*seat):
      display_seats()
      if assign_another():
        continue
      else:
        break