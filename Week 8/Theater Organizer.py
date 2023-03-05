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
        while True:
            row_var=input("\nEnter seat row (ex. 1-15): ")
            try:
                row_var = int(row_var)
            except ValueError:
                print("Invalid input -- try again")
                continue
            break
        seat.append(row_var)
        row = int(seat[0])-1

        while True:            
            col_var=input("Enter seat column (ex. A-Z or 1-4): ")
            try:
                col_var=int(col_var)
            except ValueError:
                col_var=str(col_var)
            break
            
        seat.append(col_var)

        if isinstance(seat[1], str) == True: 
            seat[1].upper
            col = ord(seat[1])-65
        else:
            col = int(seat[1])+25

        if 0<=row<15 and 0<=col<30:
            return (row, col)
        else:
            print("Invalid seat -- try again\n")
            continue

def purchase_tickets():
    total_price = 0
    requested_seats = []
    number_of_tickets = int(input("\nHow many tickets would you like to purchase? "))
    for i in range(number_of_tickets):
        requested_seats.append((get_seat()))
        
        total_price += ticket_prices(requested_seats[i][0])
    
    print(f"\nThe total price for the {number_of_tickets} tickets requested is ${total_price}!")
    while True:
        option_response = input(f"Are you sure you want to purchase these tickets for ${total_price}? Y/N: ").upper()
        
        if isinstance(option_response, str) and option_response == "Y":
            for i in range(number_of_tickets):
                assign_seat(*requested_seats[i])
            print(f"\nCongrats! You purchased {number_of_tickets} tickets!\n")
            break

        elif isinstance(option_response, str) and option_response == "N":
            while True:
                different_tickets=input("Would you like to purchase different tickets? Y/N: ").upper()
                if isinstance(different_tickets, str) and different_tickets == "Y":
                    purchase_tickets()
                    break
                elif isinstance(different_tickets, str) and different_tickets == "N":
                    break
                else:
                    print("Invalid input -- try again")
            break

        else:
            print("Invalid input -- try again")
                    
def ticket_prices(requested_seats):
    ticket_price = 0
    if 0<=requested_seats<5:
        ticket_price+=200
    elif 5<=requested_seats<10:
        ticket_price+=175
    elif 10<=requested_seats<15: 
        ticket_price+=150

    return ticket_price

def theater_details():
    tickets_sold = len(assigned_seats)
    tickets_available = 450 - len(assigned_seats)
    print(f"\n{tickets_sold} tickets have been sold so far... there are {tickets_available} tickets left available\n")

    while True:
        open_seats_in_row = input("Would you like to check a row for available seating? Y/N: ").upper()
        if isinstance(open_seats_in_row, str) and open_seats_in_row == "Y":
            lookup_row = input("What row would you like to check for available seating (ex. 1-15): ")
            try:
                lookup_row = int(lookup_row)-1
            except ValueError:
                print("Invalid input -- try again")
                continue
            if 0<=lookup_row<15:
                seats_available = 0
                for i in seats[lookup_row]:
                    if i == "#":
                        seats_available += 1
                print(f"There are {seats_available} seats available in row {lookup_row}.") 
                break
        if isinstance(open_seats_in_row, str) and open_seats_in_row == "N":
            break    

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
    
seats = []

for i in range(15):
    seats.append(['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#',])

assigned_seats = []

display_seats()
while len(assigned_seats) < 450:
    theater_details()
    purchase_tickets()
    display_seats()
    if assign_another():
        continue
    else:
        break