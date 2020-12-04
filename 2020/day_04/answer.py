from pathlib import Path
from copy import deepcopy

# Get the puzzle input data
input_file = Path(__file__).parent / "input.txt"
puzzle_data = input_file.read_text()

# ------------------------- Part 1/2 -------------------------
""" Puzzle Rules:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
passports = [p.replace("\n", " ") for p in puzzle_data.split("\n\n")]
passport_data = {"byr": None, "iyr": None, "eyr": None, "hgt": None, "hcl": None,
                 "ecl": None, "pid": None}

valid_passports = []
for pass_info in passports:
    passport = deepcopy(passport_data)
    for info in pass_info.split(" "):
        data = info.split(":")
        if data and len(data) == 2:
            passport.update({data[0]: data[1]})
    print(passport)
    if all(passport.values()):
        valid_passports.append(passport)
print(len(valid_passports))
#print({info: value for info.split() in pass_info})
# 108
# ------------------------- Part 2/2 -------------------------
""" Puzzle Rules:

"""
print("EE", "00".isnumeric())
valid_passports = []
for pass_info in passports:
    passport = deepcopy(passport_data)
    for info in pass_info.split(" "):
        data = info.split(":")
        if data and len(data) == 2:
            passport.update({data[0]: data[1]})
    if all(passport.values()):
        # 1920 and at most 2002
        byr = 1920 <= int(passport.get("byr")) <= 2002
        iyr = 2010 <= int(passport.get("iyr")) <= 2020
        eyr = 2020 <= int(passport.get("eyr")) <= 2030
        hgt = passport.get("hgt")
        if hgt.endswith("cm"):
            # 150 and at most 193.
            hgt = 150 <= int(hgt[:-2]) <= 193
        elif hgt.endswith("in"):
            # 59 and at most 76.
            hgt = 59 <= int(hgt[:-2]) <= 76
        else:
            hgt = None
        hcl = passport.get("hcl")
        if hcl.startswith("#"):
            hcl = hcl[1:].isalnum()
        else:
            hcl = None
        ecl = passport.get("ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        pid = passport.get("pid")
        if len(pid) == 9:
            pid = pid.isnumeric()
        else:
            pid = None
        if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
            valid_passports.append(passport)
            print(passport)
print(len(valid_passports))