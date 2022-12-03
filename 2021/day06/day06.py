import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 6

with open("input.txt", "r") as f:
    lanternfish_input = f.readlines()

lanternfish_data = lanternfish_input[0].split(',')

# lanternfish_data from strings to integers
for x in range(0, len(lanternfish_data)):
    if x == len(lanternfish_data):
        lanternfish_data[x] = int(lanternfish_data[x][0:1],1)
    else:
        lanternfish_data[x] = int(lanternfish_data[x])


lanternfish_data_current = lanternfish_data
lanternfish_data_next = []
lanternfish_births_day = 0

DAYS = 80

for x in range(DAYS):

    for lanternfish in lanternfish_data_current:
        if lanternfish == 0:
            lanternfish_data_next.append(6)
            lanternfish_births_day += 1
        else:
            lanternfish_data_next.append(lanternfish - 1)
    
    lanternfish_data_next.extend([8] * lanternfish_births_day)

    lanternfish_data_current = lanternfish_data_next
    lanternfish_data_next = []
    lanternfish_births_day = 0

print(len(lanternfish_data_current))


# PART 2 OF DAY 6

with open("input.txt", "r") as f:
    lanternfish_input = f.readlines()

lanternfish_data = lanternfish_input[0].split(',')

# lanternfish_data from strings to integers
for x in range(0, len(lanternfish_data)):
    if x == len(lanternfish_data):
        lanternfish_data[x] = int(lanternfish_data[x][0:1],1)
    else:
        lanternfish_data[x] = int(lanternfish_data[x])

lanternfish_initial_state = []
lanternfish_initial_state.extend([0] * 9)
for i in range(9):
    for k in lanternfish_data:
        if i == k:
            lanternfish_initial_state[i] += 1


lanternfish_current_status = lanternfish_initial_state
lanternfish_next_status = []
lanternfish_next_status.extend([0] * 9)


DAYS = 256

for day in range(DAYS):
    for i in range(len(lanternfish_current_status)):
        if i == 0:
            True
            lanternfish_next_status[6] += lanternfish_current_status[i]
            lanternfish_next_status[8] += lanternfish_current_status[i]
        else:
            lanternfish_next_status[i-1] += lanternfish_current_status[i]
    
    lanternfish_current_status = lanternfish_next_status
    lanternfish_next_status = []
    lanternfish_next_status.extend([0] * 9)


print(sum(lanternfish_current_status))