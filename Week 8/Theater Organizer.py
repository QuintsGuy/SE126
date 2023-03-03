seats = []

for i in range(15):
    seats.append(['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#',])

assigned_seats = []

def display_seats():
    print("{:^5}{:^58}".format("Row", "Seats"))
    print("{:^5}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}".format("","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4"))
    for i, row in enumerate(seats):
        print("{:^5}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}".format(i+1,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29]))

def assign_seat(row, col):
    if seats[row][col] == "*":
        print("Seat already occupied.")
        return False
    else:
        seats[row][col] = '*'
        assigned_seats.append((row, col))
        return True
    
def get_seat():
    seat = []
    while True:
        row_var=int(input("\nEnter seat row (ex. 1-15): "))
        try:
            row_var = int(row_var)
            break
        except ValueError:
            print("Invalid input -- try again")
            continue
    seat.append(row_var)
    row = int(seat[0])-1

    while True:            
        col_var=input("\nEnter seat column (ex. A-Z or 1-4): ")
        if isinstance(col_var, str) == True:
            try:
                col_var=int(col_var)
                break
            except ValueError:
                break
        else:
            print("Invalid input -- try again")
            continue
    
    seat.append(col_var)
    print(seat)

    if isinstance(seat[1], str) == True: 
        seat[1].upper
        col = ord(seat[1])-65
    else:
        col = int(seat[1])+25

    if 0<=row<15 and 0<=col<30:
        return (row, col)
    else:
        print("Invalid seat -- try again\n")
        return None
    
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
while len(assigned_seats) < 450:
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