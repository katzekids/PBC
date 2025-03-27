# ===================================================
# The function

# current_sales: a list of the current sales of the seats
#                this function does not modify current_sales!
# c_id: an integer of the id of the customer
# s_start: an integer of the starting station
# s_end: an integer of the ending station
def try_to_sell(current_sales, c_id, s_start, s_end):
    # Initialize the return value: success and assigned_seat
    success = False
    assigned_seat = 0  # Set assigned_seat to 0 as default

    # assign a seat to the customer
    for i in range(seat_cnt):
        no_seat = False
        for j in range(s_start, s_end):
            if current_sales[i][j-1] != 0:
                no_seat = True
        if not no_seat:
            success = True
            assigned_seat = i + 1
            break
    
    # DO NOT modify the values in current_sales
    # return the result
    return success, assigned_seat
# ===================================================
def if_change_seat(current_sales, s_start, s_end):
    change_success = False
    for i in range(s_start-1, s_end-1):
        for j in range(seat_cnt):
            no_change_seat = False
            for k in range(i, s_end - 1):
                if current_sales[j][k] != 0:
                    no_change_seat = True
            if not no_change_seat:
                change_seat_at = i
                change_seat_to = j
                break
        if not no_change_seat:
            break
    if no_change_seat:
        return 0, 0, 0, 0
    for i in range(seat_cnt):
        no_previous_seat = False
        for j in range(s_start-1, change_seat_at):
            if current_sales[i][j] != 0:
                no_previous_seat = True
        if not no_previous_seat:
            previoust_seat = i
            change_success = True
            break
    if no_previous_seat:
        return 0, 0, 0, 0
    return change_success, previoust_seat, change_seat_to, change_seat_at

# ===================================================
# The input module

# Read the first line of input
first_line = input().split(',')
seat_cnt = int(first_line[0])  # Number of seats
segment_cnt = int(first_line[1])  # Number of segments
passenger_cnt = int(first_line[2])  # Number of passengers

# Initialize a list to store passenger requests
# This will be a two-dimensional list
# passengers[i] is the information of the (i + 1)th passenger's
passengers = []

# Read each passenger's request

# Split the input line into s_start, s_end
passenger_data_start = input().split(',')
passenger_data_end = input().split(',')
for i in range(passenger_cnt):
    s_start = int(passenger_data_start[i])  # Starting station
    s_end = int(passenger_data_end[i])    # Ending station
    passengers.append([s_start, s_end])
# ===================================================
# ===================================================
# The computation module

# Initialize the seat allocation map
# current_sales[i][j] represents whether seat i+1 is occupied at segment j+1
# 0 means the seat is available, non-zero means the seat is occupied by a passenger ID
current_sales = []
for _ in range(seat_cnt):
    one_seat = [0] * segment_cnt
    current_sales.append(one_seat)
# note: we may also create current_sales in the following way:
# current_sales = [[0 for _ in range(segment_cnt)] for _ in range(seat_cnt)]

# Process each passenger's request
for i in range(passenger_cnt):
    s_start, s_end = passengers[i]
    # Try to assign a seat to the passenger
    success, assigned_seat = try_to_sell(current_sales, i + 1, s_start, s_end)
    if success:
        # Update the seat allocation map
        for station in range(s_start - 1, s_end - 1):
            current_sales[assigned_seat - 1][station] = i + 1  # Assign the passenger ID to the seat
    else:
        change_success, previoust_seat, change_seat_to, change_seat_at = if_change_seat(current_sales, s_start, s_end)
        if change_success:
            for j in range(s_start - 1, change_seat_at):
                current_sales[previoust_seat][j] = i + 1
            for j in range(change_seat_at, s_end - 1):
                current_sales[change_seat_to][j] = i + 1
# ===================================================


# ===================================================
# The output module

# Print the seat allocation map
for seat in current_sales:
    # Iterate through each segment in the seat
    for j in range(len(seat)):
        # Print the segment's status
        print(seat[j], end='')  # Print the number without newline
        # Print a comma if it's not the last segment
        if j < len(seat) - 1 and bool(seat[j]) == bool(seat[j+1]):
            print(',', end='')
        elif j < len(seat) - 1:
            print(";", end="")
    print()  # Print a newline after each seat
# ===================================================