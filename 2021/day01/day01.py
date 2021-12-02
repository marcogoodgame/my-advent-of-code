import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 1

# open using a "with" statement instead of open and close (saves lines)
with open("input.txt", "r") as f:
    sonar = f.readlines()

sonar = [int(line) for line in sonar]

num_of_increases = 0
for measurement in range(0, 2000):
    if sonar[measurement] > sonar[measurement-1]:
        num_of_increases += 1

print(num_of_increases)

# PART 2 OF DAY 1
with open("input.txt", "r") as f:
    sonar = f.readlines()

sonar = [int(line) for line in sonar]

num_of_increases = 0

sonar_sums = []

for measurement in range(0, 2000-2):
    sonar_sums.append(sonar[measurement] + sonar[measurement + 1] + sonar[measurement + 2])

num_of_increases = 0
for measurement in range(0, 2000-2):
    if sonar_sums[measurement] > sonar_sums[measurement-1]:
        num_of_increases += 1

print(num_of_increases)