from pathlib import Path

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().split("\n\n")

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
For each group, count the number of questions to which anyone answered "yes". 
What is the sum of those counts?
"""
total_answers = 0
for group in puzzle_data:
    answers = []
    passengers = group.split("\n")
    for passenger in passengers:
        for answer in passenger:
            if answer not in answers:
                answers.append(answer)
    total_answers += len(answers)

print(f"{total_answers} total unanimous answers.")

# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?
"""
total_answers = 0
for group in puzzle_data:
    passengers = [set(p) for p in group.strip().split("\n")]
    total_answers += len(set.intersection(*passengers))

print(f"{total_answers} total unanimous answers.")
