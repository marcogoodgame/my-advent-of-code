import os
import string

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 3

with open("input.txt", "r") as f:
    rucksacks = f.read().splitlines()
f.close()

# creation of an array where a = 1, b = 2, etc.
items_priorities = {}
count = 1
for letter in string.ascii_lowercase:
    items_priorities[letter] = count
    count += 1

for letter in string.ascii_uppercase:
    items_priorities[letter] = count
    count += 1

# reading line by line and finding the priority of each rucksack
total_priorities = 0
for rucksack in rucksacks:
    items = len(rucksack)
    half_len = int(items/2)
    first_half = rucksack[:half_len]
    second_half = rucksack[half_len:]
    combination = first_half + second_half
    # print(combination == rucksack)
    # the concation of the two partial strings is the same as the original
    item_double = ""
    for letter in first_half:
        if letter in second_half:
            item_double = letter
    current_priority = items_priorities[item_double]
    total_priorities += current_priority

print(total_priorities)

# PART 2 OF DAY 3

# STOP = len(rucksacks) - 2
# for row_index in range(0, STOP):
#     for letter in row_index:
#     print(row_index, row_index+1, row_index+2)

total_badge_priorities = 0
for index in range(0, 100):
    if index <= len(rucksacks)-3:
        first_row = rucksacks[index * 3]
        second_row = rucksacks[index * 3 + 1]
        third_row = rucksacks[index * 3 + 2]
        for letter in items_priorities:
            if letter in first_row and letter in second_row and letter in third_row:
                total_badge_priorities += items_priorities[letter]

print(total_badge_priorities)
