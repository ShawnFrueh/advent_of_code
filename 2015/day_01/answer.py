import os

# Get the puzzle input data
puzzle_input = os.path.join(os.path.dirname(__file__), "input.txt")

# Get puzzle data from file
with open(puzzle_input, "r") as puzzle:
    # Convert each line into an integer
    puzzle_data = puzzle.read()

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
'(' means up and ')' means down
To what floor do the instructions take Santa?
"""
directions = 0
for c in puzzle_data:
    if c == "(":
        directions += 1
    else:
        directions -= 1

print(directions)

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
'(' means up and ')' means down
What is the position of the character that causes Santa to 
first enter the basement?
"""
directions = 0
cnt = 0
for c in puzzle_data:
    cnt += 1
    if c == "(":
        directions += 1
    else:
        directions -= 1
    if directions < 0:
        break

print(directions, cnt)
