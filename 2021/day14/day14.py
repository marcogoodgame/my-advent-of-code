import os
import string

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 14

with open("input.txt", "r") as f:
    polymerization_input = f.readlines()

# the polymer template is simply the first row of the text file
polymer_template = polymerization_input[0]

#
polym_A = []
polym_B = []
polym_C = []

for row in range(2, len(polymerization_input)):
    polym = polymerization_input[row] #just a shorthand to improve readability
    polym_A.append(polym[0:1])
    polym_B.append(polym[1:2])
    polym_C.append(polym[6:7])

polymer_template_list = list(polymer_template)
polymer_template_list.remove("\n")
polym_current = polymer_template_list
polym_next = []

INSERTIONS = 10

for pair_insertion in range(INSERTIONS):
    for letter_index in range(0, len(polym_current)-1):
        for cycle in range(0, len(polym_A)-1):
            if polym_current[letter_index] == polym_A[cycle] and polym_current[letter_index+1] == polym_B[cycle]:
                True
                polym_next.append(polym_current[letter_index])
                polym_next.append(polym_C[cycle])

    polym_next.append(polym_current[-1])

    polym_current = polym_next
    polym_next = []
    print(pair_insertion, len(polym_current))


most_common_times = 0
least_common_times = len(polym_current)

for letter in string.ascii_uppercase:
    if polym_current.count(letter) > most_common_times:
        most_common_times = polym_current.count(letter)
    if polym_current.count(letter) < least_common_times:
        least_common_times = polym_current.count(letter)

result = most_common_times - least_common_times


print(result)
