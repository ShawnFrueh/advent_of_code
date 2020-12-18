from pathlib import Path
from collections import OrderedDict

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().strip().split("\n")

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
Before you can help with the homework, you need to understand it yourself. 
Evaluate the expression on each line of the homework;
what is the sum of the resulting values?
"""


class NewMath(int):
    """ Class used to alter the way math works.

    Notes:
        In order to change the order of operations we will just change the operators that get
        evaluated and then use this class to evaluate the correct operation.
    """

    def __add__(self, other):
        """ We dont need to alter addition in any way so keep the same.
        """
        return NewMath(int(self) + other)

    def __mul__(self, other):
        """Part two we change the oder of addition and multiplication, so if we are multiplying
        In reality we are just adding.
        """
        return NewMath(int(self) + other)

    def __sub__(self, other):
        """Pat one we replace * with -  since there are no subtractions in the data.
        so if we subtract, lets actually multiply.
        """
        return NewMath(int(self) * other)


def evaluate(formulas):
    value = 0
    for formula in formulas:
        # Replace all integers with custom math class
        for d in range(10):
            formula = formula.replace(f"{d}", f"NewMath({d})")
        # Get rid of multiplication to change the order of operations
        formula = formula.replace("*", "-")
        # Pass in the NewMath as a global value and Evaluate the formula.
        value += eval(formula, {"NewMath": NewMath})
    return value


print(evaluate(puzzle_data))
# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
Now, addition and multiplication have different precedence levels, but they're not the ones 
you're familiar with. Instead, addition is evaluated before multiplication.
What do you get if you add up the results of evaluating the homework problems using these new rules?
"""


def evaluate(formulas):
    value = 0
    for formula in formulas:
        # Replace all integers with custom math class
        for digit in range(10):
            formula = formula.replace(str(digit), f"NewMath({digit})")
        # Get rid of multiplication to change the order of operations
        formula = formula.replace("*", "-")
        # Change addition to multiplication to evaluate first
        formula = formula.replace("+", "*")
        # Pass in the NewMath as a global value and Evaluate the formula.
        value += eval(formula, {"NewMath": NewMath})
    return value


print(evaluate(puzzle_data))
