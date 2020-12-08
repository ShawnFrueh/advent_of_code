from pathlib import Path

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().strip().split("\n")

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
How many bag colors can eventually contain at least one shiny gold bag?
"""
# Parse data and generate the rules
my_bag = "shiny gold"
bag_rules = {}
for new_rule in puzzle_data:
    # Split the data into bag and its sub bags.
    cur_bag, bag_contents = new_rule.split(" bags contain ")
    # Split sub bags into individual bags.
    bag_contents = bag_contents.split(", ")
    sub_bags = {}
    for sub_bag in bag_contents:
        # Extract the count type and color. Any extra from the split goes to _
        count, bag_type, bag_color, *_ = sub_bag.split(" ")
        if count == "no":
            continue
        bag = " ".join((bag_type, bag_color))
        sub_bags[bag] = int(count)
    bag_rules[cur_bag] = sub_bags


def get_contents(check_bag):
    """Finds all bags that contain given bag.

    Args:
        check_bag (string): Name of the bag to find.

    Returns:
        bag_list (set): The entire contents of a bag.
    """
    bag_list = set()
    for bag, sub_bags in bag_rules.items():
        if check_bag in sub_bags:
            bag_list.add(bag)
            # Now check inside this bag
            bag_list.update(get_contents(bag))
    return bag_list


print("{} bags can contain my bag.".format(len(get_contents(my_bag))))
# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
How many individual bags are required inside your single shiny gold bag?
"""


def get_bag_count(check_bag):
    """Gets the number of bags within the given bag.

    Args:
        check_bag (str): Name of the bag to check.

    Returns:
        bab_count (int): The number of bags within the checked bag.
    """
    bag_count = 0
    for bag in bag_rules[check_bag]:
        # Get the number of times this bag type is in the checked bag.
        dup_bag = bag_rules[check_bag][bag]
        # Add the Bag count, plus itself and multiply it by the dupe count.
        bag_count += (1 + get_bag_count(bag)) * dup_bag
    return bag_count


print("My bag contains {} other bags.".format(get_bag_count(my_bag)))
