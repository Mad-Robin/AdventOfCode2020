class Seat:
    def __init__(self, seat):
        row = seat_prep(seat[0:7])
        column = seat_prep(seat[7:10])
        self.row = row
        self.column = column
        self.seat_id = (row * 8) + column


def seat_prep(string):
    binary = string.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    value = int(binary, 2)
    return value


seats = []
with open("Inputs/day5.txt", "r") as file:
    for line in file:
        seats.append(Seat(line.rstrip()))

print(max(seat.seat_id for seat in seats))

seats_min = Seat('FFFFFFFLLL').seat_id
seats_max = Seat('BBBBBBBRRR').seat_id

taken_seats = []
for seat in seats:
    taken_seats.append(seat.seat_id)

possible_seats = []
for i in range(seats_min, seats_max):
    if i not in taken_seats:
        possible_seats.append(i)

for i in range(0, len(possible_seats)):
    try:
        if possible_seats[i-1] - possible_seats[i] in [1,-1]:
            continue
        if possible_seats[i+1] - possible_seats[i] in [1,-1]:
            continue
        else:
            print(possible_seats[i])
    except:
        continue

examples = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

examp = []
for example in examples:
    examp.append(Seat(example))

for obj in examp:
    print(obj.row, obj.column, obj.seat_id)