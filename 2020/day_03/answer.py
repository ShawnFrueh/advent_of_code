from pathlib import Path
import math

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().split("\n")
sled_map = [list(p) for p in puzzle_data]


class Move(object):
    """ Vector class to store direction """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Sled(object):
    """ Coordinate class to track sled """
    def __init__(self, x, y, _map):
        self.x = x
        self.y = y
        self.damage = 0
        self.map = _map
        self.repeat = len(self.map[0])
        self.hill = len(self.map)

    def slide(self, direction):
        self.x = (self.x + direction.x) % self.repeat
        self.y += direction.y
        if self.position() == "#":
            # You hit a tree, take damage.
            self.damage += 1

    def position(self):
        try:
            return self.map[self.y][self.x]
        except IndexError:
            # We are at the bottom
            return

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
how many trees would you encounter?
"""
# Initialize the sled.
sled = Sled(0, 0, sled_map)
# Right 3 Down 1.
direction = Move(3, 1)
# Slide down the hill, skipping the first row
for i in range(sled.hill)[1:]:
    # Move the sled.
    sled.slide(direction)
# Report the damage
print(sled.damage)

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
Right 1, down 1.
Right 3, down 1. (Same as above)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

What do you get if you multiply together the number of trees encountered on each of 
the listed slopes?
"""
trees_hit = []
# Setup the multiple sled runs
for direction in [Move(1, 1), Move(3, 1), Move(5, 1), Move(7, 1), Move(1, 2)]:
    # Initialize the sled.
    sled = Sled(0, 0, sled_map)
    # Slide down the hill one row at a time.
    for i in range(sled.hill):
        # Skip any rows that we move over and not to.
        if i % direction.y != 0:
            continue
        # Move the sled.
        sled.slide(direction)
    # Report the damage
    trees_hit.append(sled.damage)

# Trees hit for each run.
print(trees_hit)
# Product of all trees hit.
print(math.prod(trees_hit))
