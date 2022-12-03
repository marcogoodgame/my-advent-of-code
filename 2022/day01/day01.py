import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 1

with open("input.txt", "r") as f:
    calories = f.read().splitlines()

partial_sum = 0
elf_calories = []
for item in calories:
    if item != "":
        partial_sum += int(item)
    else:
        elf_calories.append(partial_sum)
        partial_sum = 0

max_calories_elf = max(elf_calories)
print("MAX =", max_calories_elf)

# PART 2 OF DAY 1

elf_calories_ranked = elf_calories
elf_calories_ranked.sort(reverse=True)

SUM_ELVES = 3
sum_top_n = 0
for elf_index in range(0, SUM_ELVES):
    sum_top_n += elf_calories_ranked[elf_index]

print("Top 3 elves account for calories =", sum_top_n)
