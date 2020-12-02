import os

# Get the puzzle input data
puzzle_input = os.path.join(os.path.dirname(__file__), "input.txt")

# Get puzzle data from file
with open(puzzle_input, "r") as puzzle:
    # Get each dimension from the input data.
    puzzle_data = [[int(i) for i in d.strip().split("x")] for d in puzzle.readlines()]


def get_area(l, w, h):
    # Sort list to get shortest side
    min = sorted((l, w, h))
    # Calculation rules per puzzle
    return 2*l*w + 2*w*h + 2*h*l + min[0]*min[1]


def get_ribbon(l, w, h):
    # Sort list to get shortest side
    min = sorted((l, w, h))
    # Add the two shortest sides together
    ribbon_len = min[0] + min[0] + min[1] + min[1]
    # Add the volume of the present
    ribbon_len += l*w*h
    return ribbon_len


# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
2*l*w + 2*w*h + 2*h*l
How many total square feet of wrapping paper should they order?
"""
total_dimensions = 0
for dimension in puzzle_data:
    total_dimensions += get_area(*dimension)

print(total_dimensions)

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
2*l*w + 2*w*h + 2*h*l
How many total feet of ribbon should they order?
"""
total_ribbon = 0
for dimension in puzzle_data:
    total_ribbon += get_ribbon(*dimension)

print(total_ribbon)
