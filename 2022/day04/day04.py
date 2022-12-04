import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 4

with open("input.txt", "r") as f:
    elves = f.read().splitlines()
f.close()

# the file is split and converted to make it useable
elves_split = []
for elf in elves:
    elf = elf.replace("-", ";")
    elf = elf.replace(",", ";")
    row_split = elf.split(";")
    row_num = []
    for number in row_split:
        row_num.append(int(number))
    elves_split.append(row_num)

total_included = 0
for row in elves_split:
    first_start = row[0]
    first_end = row[1]
    second_start = row[2]
    second_end = row[3]
    
    included = 0
    if first_start <= second_start and first_end >= second_end:
        included = 1
    if second_start <= first_start and second_end >= first_end:
        included = 1
    total_included += included

print(total_included)

# PART 2 OF DAY 4

total_overlapping = 0
for row in elves_split:
    first_start = row[0]
    first_end = row[1]
    second_start = row[2]
    second_end = row[3]
    overlap = 0
    for num in range(first_start, first_end + 1):
        if num in range(second_start, second_end + 1):
            overlap = 1
    total_overlapping += overlap

print(total_overlapping)
