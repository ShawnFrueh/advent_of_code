from pathlib import Path
from functools import lru_cache

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = [int(d) for d in input_file.read_text().strip().split("\n")]

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
"""

jolt_1 = 0
jolt_3 = 0
data = sorted(puzzle_data)
# Add your own devices jolt rating (Highest + 3)
data.append(data[-1]+3)
# Add your seats jolt rating as the first element.
data.insert(0, 0)
# Using zip will par up the values so we offset them by removing the
# first digit from the second input. This will also remove the last
# dangling digit since it is no pair-able.
for a, b in zip(data, data[1:]):
    # Check if jolt difference is 1
    if b - a == 1:
        jolt_1 += 1
    # Check if jolt difference is 3
    elif b - a == 3:
        jolt_3 += 1

print(jolt_1 * jolt_3)

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
What is the total number of distinct ways you can arrange the adapters to connect
the charging outlet to your device?
"""

# Create a cache to hold all the calculations so we arent re-iterating over them every time.
arrangements = {data.pop(0): 1}
jolts = (1, 2, 3)
for adapter in data:
    # Get the arrangements of the previously cached values
    curr_arrange = [arrangements[adapter-jolt] for jolt in jolts
                    if adapter-jolt in arrangements]
    # Add up those arrangements and add them to the data.
    arrangements[adapter] = sum(curr_arrange)


print(arrangements.popitem()[1])
# 31581162962944
