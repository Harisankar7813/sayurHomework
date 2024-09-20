'''Problem #2
Same problem as above. Also calculate tickets price. 
Firsrt 3 rows - Rs100
Rows 4 to 12 - Rs 200
Rows 13 till top - Rs 300.
3 seats close to the wall on both sides costs less than the other seats in the same row.'''
no_of_rows = 15
no_of_columns = 6
first_3_rows = 100
row_4_to_12 = 200
row_13_till_top = 300

def ticket_price():
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            for k in range(65 + i, 65 + i + 1):
                print(chr(k) + str(j + 1), end=" ")
        print("\n")

    ticket_reserved = int(input("Enter number of seats to reserve:"))
    reserved_seats = []

    for i in range(ticket_reserved):
        row = i // no_of_columns
        col = i % no_of_columns
        seat = chr(65 + row) + str(col + 1)
        reserved_seats.append(seat)

    for i in range(no_of_rows):
        for j in range(no_of_columns):
            for k in range(65 + i, 65 + i + 1):
                print("X " if (chr(k) + str(j + 1)) in reserved_seats else (chr(k) + str(j + 1)), end=" ")
        print("\n")

    total_price = 0
    for seat in reserved_seats:
        row = ord(seat[0]) - 65 + 1
        if row <= 3:
            total_price += first_3_rows
        elif 4 <= row <= 12:
            total_price += row_4_to_12
        else:
            total_price += row_13_till_top

    print(f"Total Price for {ticket_reserved} seats: Rs{total_price}")
ticket_price()
'''
output
A1 A2 A3 A4 A5 A6 

B1 B2 B3 B4 B5 B6

C1 C2 C3 C4 C5 C6

D1 D2 D3 D4 D5 D6

E1 E2 E3 E4 E5 E6

F1 F2 F3 F4 F5 F6

G1 G2 G3 G4 G5 G6

H1 H2 H3 H4 H5 H6

I1 I2 I3 I4 I5 I6

J1 J2 J3 J4 J5 J6

K1 K2 K3 K4 K5 K6

L1 L2 L3 L4 L5 L6

M1 M2 M3 M4 M5 M6

N1 N2 N3 N4 N5 N6

O1 O2 O3 O4 O5 O6

Enter number of seats to reserve:13
X  X  X  X  X  X  

X  X  X  X  X  X

X  C2 C3 C4 C5 C6

D1 D2 D3 D4 D5 D6

E1 E2 E3 E4 E5 E6

F1 F2 F3 F4 F5 F6

G1 G2 G3 G4 G5 G6

H1 H2 H3 H4 H5 H6

I1 I2 I3 I4 I5 I6

J1 J2 J3 J4 J5 J6 

K1 K2 K3 K4 K5 K6

L1 L2 L3 L4 L5 L6

M1 M2 M3 M4 M5 M6

N1 N2 N3 N4 N5 N6

O1 O2 O3 O4 O5 O6 

Total Price for 13 seats: Rs1300
'''