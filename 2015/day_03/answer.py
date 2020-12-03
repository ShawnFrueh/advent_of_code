import os
from pathlib import Path

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text()


class Tracker(object):
    """ Coordinate class to track Santa """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, c):
        return Tracker(self.x + c.x, self.y + c.y)

    def __sub__(self, c):
        return Tracker(self.x - c.x, self.y - c.y)

    def position(self, as_string=False):
        if as_string:
            return str(self.x) + "_" + str(self.y)
        else:
            return self.x, self.y


# List of directions and their coordinates.
directions = {"^": Tracker(1, 0), "v": Tracker(-1, 0), ">": Tracker(0, 1), "<": Tracker(0, -1)}


# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
How many houses receive at least one present?
"""
visited_houses = {"0_0": 1}
curr_pos = Tracker(0, 0)
for direction in puzzle_data:
    new_dir = directions.get(direction)
    curr_pos += new_dir
    house = curr_pos.position(True)
    if visited_houses.get(house):
        visited_houses[house] += 1
    else:
        visited_houses[house] = 1

print(curr_pos.position())
print(len(visited_houses))
# 2591, 2592

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
Santa and Robo-Santa start at the same location then take turns moving.
(delivering two presents to the same starting house)
How many houses receive at least one present?
"""
visited_houses = {"0_0": 2}
santa_tracker = Tracker(0, 0)
robot_tracker = Tracker(0, 0)

robot = True
for direction in puzzle_data:
    new_dir = directions.get(direction)
    if robot:
        robot_tracker += new_dir
        house = robot_tracker.position(True)
        robot = False
    else:
        santa_tracker += new_dir
        house = santa_tracker.position(True)
        robot = True
    if visited_houses.get(house):
        visited_houses[house] += 1
    else:
        visited_houses[house] = 1

print(santa_tracker.position())
print(robot_tracker.position())
print(len(visited_houses))
