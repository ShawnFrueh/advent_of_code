from pathlib import Path
import itertools

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().strip().split("\n")
puzzle_data = [int(x) for x in puzzle_data]
# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:

"""
data = [35, 20, 15, 25, 47,
        40, 62, 55, 65, 95,
        102, 117, 150, 182, 127,
        219, 299, 277, 309, 576]


#prev_num = 5
prev_num = 25

for i, v in enumerate(puzzle_data):
    if i >= prev_num:
        has_pre = False
        for comb in itertools.combinations(puzzle_data[i-prev_num:i], 2):
            if sum(comb) == v:
                has_pre = True
        if not has_pre:
            print(v, has_pre)
            break

invalid = 41682220
# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:

"""

for i, v in enumerate(puzzle_data):
    for j in range(len(puzzle_data)):
        if invalid == sum(puzzle_data[i:j]):
            sum_list = sorted(puzzle_data[i:j])
            print(sum_list)
            print(sum_list[0] + sum_list[-1])
            break
# 5388976