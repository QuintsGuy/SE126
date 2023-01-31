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
    seats[row][col] = "X"
    assigned_seats.append((row, col))
    return True

def get_seat():
    seat = input("Enter seat (e.g. 1A): ")
    row = int(seat[0]) - 1
    col = ord(seat[1]) - 65
    if row>6 or col>3:
        print("Invalid seat.")
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
      return 1
    elif check_again=="N":
      return False
    else:
      print("Invalid input -- try again")

display_seats()
while len(assigned_seats) < 28:
    seat = get_seat()
    if seat:
        if assign_seat(*seat):
            display_seats()
        returned_option=assign_another()
        if returned_option==1:
            continue
        else:
            print('Goodbye...\n')
            break
    else:
        print("All seats filled.")