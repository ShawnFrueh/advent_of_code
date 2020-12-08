from pathlib import Path
import math
# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().splitlines()

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""
#puzzle_data = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
#puzzle_data = ["FBFBBFFRLR"]
rows = []
for ticket in puzzle_data:
    region = ticket[:-3]
    column = ticket[-3:]

    row_min = 0
    row_max = 127
    for r in region:
        if r == "F":
            new_range = list(range(row_min, row_max))
            row_max = new_range[int(len(new_range) * 0.5)]
        elif r == "B":
            new_range = list(range(row_min, row_max))
            row_min = new_range[-int(len(new_range) * 0.5)]
    col_min = 0
    col_max = 7
    for c in column:
        new_range = list(range(col_min, col_max+1))
        half = len(new_range) // 2
        if c == "R":
            new_range = new_range[len(new_range) // 2:]
            col_max = new_range[-1]
            col_min = new_range[0]
        elif c == "L":
            new_range = new_range[:len(new_range) // 2]
            col_max = new_range[-1]
            col_min = new_range[0]
    col = col_min if c == "L" else col_max
    rows.append((row_max, col))

seat_id = 0
all_seats = []
for t in rows:
    id = (t[0]*8+t[1])
    if id > seat_id:
        seat_id = id
    all_seats.append({"Row": t[0], "Col": t[1], "Seat ID": id})

print(f"Max seat id: {seat_id}")
# 870, 879

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
Your seat wasn't at the very front or back, though; 
the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""
sorted_seats = sorted(all_seats, key=lambda k: k['Row'])
seats = {}
for seat in sorted_seats:
    row = seat.get("Row")
    if row in seats:
        seats[row]["count"] += 1
        seats[row]["cols"].append(seat)
    else:
        seats[row] = {}
        seats[row]["count"] = 1
        seats[row]["cols"] = [seat]

unfilled_seats = []
for seat in seats:
    if seats.get(seat).get("count") != 8:
        unfilled_seats.append(sorted(seats[seat]["cols"], key=lambda k: k["Col"]))

# Find the missing seat
available_seats = list(range(8))
for seat in unfilled_seats[1]:
    available_seats.remove(seat.get("Col"))

print(available_seats)
if len(available_seats) == 1:
    seat = unfilled_seats[1][available_seats[0]]
    seat_id = seat.get("Row") * 8 + available_seats[0]
    print(f"My seat id: {seat_id}")
