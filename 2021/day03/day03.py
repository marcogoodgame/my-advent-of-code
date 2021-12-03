import os

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 3

with open("input.txt", "r") as f:
    bits_input = f.readlines()


zeroes = 0 
ones = 0

gamma_rate = ""
epsilon_rate = ""

for column in range(0, len(bits_input[0])-1):
    for row in range(0, len(bits_input)):
        if bits_input[row][column] == "0":
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
    zeroes = 0
    ones = 0

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
power_consumption = gamma_rate * epsilon_rate

print(power_consumption)

# PART 2 OF DAY 3

with open("input.txt", "r") as f:
    bits_input = f.readlines()


zeroes = 0 
ones = 0
column = -1

while len(bits_input) > 1:
    
    zeroes = 0 
    ones = 0
    column += 1

    for row in range(0, len(bits_input)):
        if bits_input[row][column] == "0":
            zeroes += 1
        else:
            ones += 1
    
    if zeroes > ones:
        prevalence = 0
    else:
        prevalence = 1

    bits_input = [x for x in bits_input if x[column] == str(prevalence)]

oxygen = int(bits_input[0], 2)

#######

with open("input.txt", "r") as f:
    bits_input = f.readlines()

zeroes = 0 
ones = 0
column = -1

while len(bits_input) > 1:
    
    zeroes = 0 
    ones = 0
    column += 1

    for row in range(0, len(bits_input)):
        if bits_input[row][column] == "0":
            zeroes += 1
        else:
            ones += 1
    
    if zeroes > ones:
        prevalence = 1
    else:
        prevalence = 0

    bits_input = [x for x in bits_input if x[column] == str(prevalence)]

co2 = int(bits_input[0], 2)

life_support_rating = oxygen * co2
print(life_support_rating)
