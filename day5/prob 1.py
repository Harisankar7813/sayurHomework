'''Problem #1
Wrote a program for seat reservation in a theatre.
You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
When the user asks for tickets, you need to provide them tickets in the form of seat no.
For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
Print the theatre configuaration at the end of each transactio'''
no_of_columns=5
no_of_rows=3
def seats():
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            for k in range(65+i,65+i+1):
                print(chr(k)+str(j+1),end=" ")
        print("\n")
seats()
def ticket_reserve():
    ticket_reserved=int(input("Enter number of seats to reserve:"))
    reserved_seats=[]
    for i in range(ticket_reserved):
        row = i // no_of_columns
        col = i % no_of_columns
        seat = chr(65 + row) + str(col + 1)
        reserved_seats.append(seat)
        print(f"Reserved Seating Arrangement:{seat}")
    print("\n")
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            for k in range(65+i,65+i+1):
                print("X " if(chr(k)+str(j+1)) in reserved_seats else(chr(k)+str(j+1)) ,end=" ")
        print("\n")
ticket_reserve()
'''
output
A1 A2 A3 A4 A5 

B1 B2 B3 B4 B5

C1 C2 C3 C4 C5

Enter number of seats to reserve:5

Reserved Seating Arrangement:A1
Reserved Seating Arrangement:A2
Reserved Seating Arrangement:A3
Reserved Seating Arrangement:A4
Reserved Seating Arrangement:A5


X  X  X  X  X

B1 B2 B3 B4 B5

C1 C2 C3 C4 C5
'''
