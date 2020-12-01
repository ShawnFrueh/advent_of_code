import os
import math
import itertools

# Get the puzzle input data
puzzle_input = os.path.join(os.path.dirname(__file__), "input.txt")
# Sum of the two entries
sum_target = 2020

# Get puzzle data from file
with open(puzzle_input, "r") as puzzle:
    # Convert each line into an integer
    puzzle_data = [int(i.strip()) for i in puzzle.readlines()]


def get_sum_target(data_list, target_sum, inputs):
    """Use a list of integers and attempt to find a combination of inputs that add up to a value.

    Notes:
        https://docs.python.org/3/library/itertools.html#itertools.combinations

    Args:
        data_list (list[int]): List of integers to use for combinations.
        target_sum (int): The target value that the combination should add up to.
        inputs (int): The number if inputs from the list to use in the combinations.

    Returns:
        combination (tuple[int]): Tuple of inputs that add up to the target sum.
    """
    for combination in itertools.combinations(data_list, inputs):
        if sum(combination) == target_sum:
            return combination


# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
Find the two entries that sum to 2020.
what do you get if you multiply them together?
"""
input_count = 2
combo = get_sum_target(puzzle_data, sum_target, input_count)
print("Part 1:")
print("Inputs:", combo)
print("Output:", math.prod(combo))

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
what is the product of the three entries that sum to 2020?
"""
input_count = 3
combo = get_sum_target(puzzle_data, sum_target, input_count)
print("\nPart 2:")
print("Inputs:", combo)
print("Output:", math.prod(combo))
