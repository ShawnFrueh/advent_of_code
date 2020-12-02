import os
from collections import namedtuple

# Get the puzzle input data
puzzle_input = os.path.join(os.path.dirname(__file__), "input.txt")

# Get puzzle data from file
with open(puzzle_input, "r") as puzzle:
    # Convert each line into an integer
    puzzle_data = [[j.strip() for j in i.strip().split(":")] for i in puzzle.readlines()]

# Create storage for password data
PassInfo = namedtuple("PassInfo", "min max character password")


def parse_rules(p_data):
    """Parses the incoming password rules and password into a namedtuple.

    Args:
        p_data (list): Rules and Password list.

    Returns:
        (PassInfo): Formatted namedtuple (min, max, character, password)
    """
    p_info, p_word = p_data
    p_range, p_char = p_info.split(" ")
    p_min, p_max = [int(p) for p in p_range.split("-")]
    return PassInfo(min=p_min, max=p_max, character=p_char, password=p_word)

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
1-3: lowest and highest number of times a given letter must appear for the password to be valid.
How many passwords are valid according to their policies?
"""
valid_passes = []
for pass_data in puzzle_data:
    # Parse the password data.
    pass_info = parse_rules(pass_data)
    # Get the number of times a character appears in the password.
    char_count = pass_info.password.count(pass_info.character)
    # Check if the number of characters are within the min/max threshold.
    if pass_info.min <= char_count <= pass_info.max:
        valid_passes.append(pass_info.password)

print("Valid Passwords:", len(valid_passes))
# (569)

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
1-3: positions in the password, where 1 means the first character, 2 means the second character. Only one must match.
How many passwords are valid according to the new interpretation of the policies?
"""
valid_passes = []
for pass_data in puzzle_data:
    # Parse the password data.
    pass_info = parse_rules(pass_data)
    # Get the number of times a character appears in the password.
    char_count = pass_info.password.count(pass_info.character)

    # Get the character as the min position.
    p_min = pass_info.password[pass_info.min - 1]
    # Get the character as the max position.
    p_max = pass_info.password[pass_info.max - 1]

    # Check if min position is character and not the pax position.
    if p_min == pass_info.character and p_max != pass_info.character:
        valid_passes.append(pass_info.password)
    # Check if max position is character and not the min position.
    elif p_min != pass_info.character and p_max == pass_info.character:
        valid_passes.append(pass_info.password)

print("Valid Passwords:", len(valid_passes))
# (346)
