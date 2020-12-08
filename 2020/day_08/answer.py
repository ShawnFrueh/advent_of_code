from pathlib import Path
from copy import deepcopy

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text().strip().split("\n")

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
Run your copy of the boot code. Immediately before any instruction is executed a second time, 
what value is in the accumulator?
"""
# puzzle_data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3",
#                "acc -99", "acc +1", "jmp -4", "acc +6"]


def boot(instructions):
    accumulator = 0
    cur_inst = 0
    executed = {}
    # Create a loop and break if we reach the end of the instruction set
    # or we visit an instruction more than once.
    while cur_inst < len(instructions) and not executed.get(cur_inst):
        executed[cur_inst] = True
        instruction, value = instructions[cur_inst]
        if instruction == "acc":
            accumulator += int(value)
            cur_inst += 1
        elif instruction == "nop":
            cur_inst += 1
        elif instruction == "jmp":
            cur_inst += int(value)

    last_inst = cur_inst == len(instructions)
    return accumulator, last_inst


boot_data = [ins.split(" ") for ins in puzzle_data]
print(boot(boot_data)[0])
# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:
Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
What is the value of the accumulator after the program terminates?
"""


def brute_boot(instructions):
    # Create swap dictionary.
    op_swap = {"jmp": "nop", "nop": "jmp"}
    # Iterate over each original instruction.
    for _try, instruction in enumerate(instructions):
        # We dont care about accumulation
        if instruction[0] != "acc":
            # Create a bootleg copy of the data.
            bootleg = deepcopy(instructions)
            # Swap out jmp or nop
            bootleg[_try][0] = op_swap.get(instruction[0])
            # Run the bootleg and see if we get to the last instruction.
            accumulator, last_inst = boot(bootleg)
            if last_inst:
                # If we did, report the accumulation value.
                return accumulator
    return None


boot_data = [ins.split(" ") for ins in puzzle_data]
print(brute_boot(boot_data))
