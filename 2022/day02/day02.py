import os
from enum import Enum # enumerated data type

# change the working directory to the one where the python and the input files are stored
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PART 1 OF DAY 2

class Shape(Enum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3

class Outcome(Enum):
    loss = 0
    draw = 3
    win = 6

def evalute_match(other_shape, self_shape):
    difference_players = self_shape - other_shape
    if difference_players == 0:
        outcome = Outcome["draw"].value
    elif difference_players in (1, -2):
        outcome = Outcome["win"].value
    elif difference_players in (2, -1):
        outcome = Outcome["loss"].value
    else:
        outcome = "Error"
    round_result = self_shape + outcome
    return round_result

with open("input.txt", "r") as f:
    rounds = f.read().splitlines()
f.close()

sum_results = 0
for round in rounds:
    other_player = Shape[round[0]].value
    me = Shape[round[2]].value
    round_result = evalute_match(other_player, me)
    sum_results += round_result 

print(sum_results)

# PART 2 OF DAY 2

class PotentialDifference(Enum):    
    X = [-1, 2]  # loss
    Y = [0] # draw
    Z = [1, -2] # win

sum_results = 0
for round in rounds:
    other_player = Shape[round[0]].value
    potential_difference = PotentialDifference[round[2]].value
    for difference in potential_difference:
        potential_shape = other_player + difference 
        if potential_shape in range(1, 4):
            my_shape = potential_shape
    round_result = evalute_match(other_player, my_shape)
    sum_results += round_result

print(sum_results)