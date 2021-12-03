import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 2

with open("input", "r") as f:
    commands = f.readlines()

# set variables at 0
depth = 0
hor_pos = 0

# for each loop
for line in commands:
    command = line.split()[0]
    value = int(line.split()[1])

    if command == 'forward':
        hor_pos += value
    elif command == 'down':
        depth += value
    else:
        depth -= value

print(depth * hor_pos)

# PART 2 OF 2

with open("input", "r") as f:
    commands = f.readlines()

aim = 0
hor_pos = 0
depth = 0

for line in commands:
    command = line.split()[0]
    value = int(line.split()[1])

    if command == 'forward':
        hor_pos += value
        depth += aim * value
    elif command == 'down':
        aim += value
    else:
        aim -= value

print(depth * hor_pos)