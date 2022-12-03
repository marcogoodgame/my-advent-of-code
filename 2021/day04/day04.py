import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 4

with open("input.txt", "r") as f:
    bingo_input = f.readlines()

drawn_numbers = bingo_input[0].split(',')

bingo_cols = 5
bingo_rows = 5

tables = []

for line in range(0, len(bingo_input)):
    if bingo_input[line] == "\n":
        header = line
        table = []
        for row_counter in range(1, bingo_rows+1):
            row = bingo_input[line+row_counter].split()
            table.append(row)
        tables.append(table)


for number_index in range(0, len(drawn_numbers)):
    for selected_table in tables:
        for row in selected_table:
            if drawn_numbers[number_index] in row:
                for column_internal in row:
                    for number_cycle in range(0, number_index+1):
                        if column_internal != drawn_numbers[number_cycle]:
                            break
                        else:
                            winner_table = selected_table
                            last_number_index = number_index

                        



unmarked_numbers_sum = 0
for row in range(0, len(winner_table)):
    for column in range(0, bingo_cols):
        if winner_table[row][column] not in drawn_numbers[0:last_number_index]:
            unmarked_numbers_sum += int(winner_table[row][column])


result = unmarked_numbers_sum * int(drawn_numbers[last_number_index])

print(result)