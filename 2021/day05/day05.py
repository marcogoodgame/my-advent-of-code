
import os
import re


# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 5

# open using a "with" statement instead of open and close (saves lines)
with open("input.txt", "r") as f:
    vents = f.read().splitlines()

# function to print partially a matrix
# given the list of lists, the number of rows
# and columns to be printed
# (useful to check if the code is working properly)
def partial_matrix_print(array: list, rows: int, columns: int):
    row_printed = ""
    for r in range(0, rows):
        row_printed += "["
        for c in range(0, columns):
            row_printed += str(array[r][c])
            row_printed += ","
        row_printed += "]"
        print(row_printed)
        row_printed = ""

# each row from the input
# is formatted as: x1,y1 -> x2,y2
# re.split is a way to split strings
# with more than one delimit.
x1 = []
y1 = []
x2 = []
y2 = []

for r in vents:
    split_vents = re.split(',| -> ',r)
    x1.append(int(split_vents[0]))
    y1.append(int(split_vents[1]))
    x2.append(int(split_vents[2]))
    y2.append(int(split_vents[3]))

# the number of rows and columns
# is assigned as a constant
COLS = 1000
ROWS = 1000

# the matrix is created
#
# it is _fundamental_ to convert
# the list to a list
# using `table.append(row)` would have NOT
# created a copy to a different array
# but just a reference to it
# 
# i.e. a change to a single row would have
# been applied to all rows (being the same list)
#
# alternatively `table.append(row[:])`
# could also have been used
row = [0] * COLS
table = []
for i in range (0, ROWS):
    table.append(list(row))

for input_row in range(0, len(x1)):
    # in this 
    
    current_x1 = x1[input_row]
    current_x2 = x2[input_row]
    current_y1 = y1[input_row]
    current_y2 = y2[input_row]
    
    min_x = min(current_x1, current_x2)
    max_x = max(current_x1, current_x2)

    min_y = min(current_y1, current_y2)
    max_y = max(current_y1, current_y2)

    # x1 = x2
    # vertical line
    # x = x1 = x2
    # y = changes, in range(y1, y2)

    if current_x1 == current_x2:
        for cicle_row in range(min_y,max_y+1):
            table[cicle_row][current_x1] += 1
    elif current_y1 == current_y2:
        for cicle_col in range(min_x,max_x+1):
            table[current_y1][cicle_col] += 1

# counting overlapping lines
overlaps = 0
for row_counter in range(0, ROWS):
    for col_counter in range(0, COLS):
        if table[row_counter][col_counter] >= 2:
            overlaps += 1

# the overlaps are printed
print(overlaps)

####################################

# PART 2 OF DAY 5

row = [0] * COLS
table = []
for i in range (0, ROWS):
    table.append(list(row))

for input_row in range(0, len(x1)):
    current_x1 = x1[input_row]
    current_x2 = x2[input_row]
    current_y1 = y1[input_row]
    current_y2 = y2[input_row]
    
    min_x = min(current_x1, current_x2)
    max_x = max(current_x1, current_x2)

    min_y = min(current_y1, current_y2)
    max_y = max(current_y1, current_y2)

    # I need to the corrisponding coordinate
    # for the max ys and xs
    # (note: the point with max x
    # migh not be the point with max y,
    # same with min x / y...)
    if min_y == current_y1:
        co_min_y = current_x1
    elif min_y == current_y2:
        co_min_y = current_x2
    
    if max_y == current_y1:
        co_max_y = current_x1
    elif max_y == current_y2:
        co_max_y = current_x2

    if current_x1 == current_x2:
        for cicle_row in range(min_y,max_y+1):
            table[cicle_row][current_x1] += 1
    elif current_y1 == current_y2:
        for cicle_col in range(min_x,max_x+1):
            table[current_y1][cicle_col] += 1
    else:
        # the slope of the diagonal line
        # must be = to either 1 or -1
        # slope = change in y / change in x
        slope = (current_y2 - current_y1) / (current_x2 - current_x1)
        if slope == 1 or slope == -1:
            for cicle_diag in range(min_y, max_y+1):
                # DOES NOT WORK YET...
                if co_max_y >= co_min_y:
                    for cicle_obliq in range(min_y, max_y+1):
                        table[cicle_obliq][cicle_obliq] += 1
                else:
                    for cicle_obliq in range(min_y, max_y+1):
                        table[cicle_obliq][cicle_obliq] += 1
                        True 

# counting overlapping lines
overlaps = 0

for row_counter in range(0, ROWS):
    for col_counter in range(0, COLS):
        if table[row_counter][col_counter] >= 2:
            overlaps += 1

# the overlaps are printed
print(overlaps)