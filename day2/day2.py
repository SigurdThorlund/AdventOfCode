
with open('day2/data/input.py', 'r') as f:
    inp = f.read()

score_matrix = [[3, 6, 0],[0, 3, 6],[6, 0, 3]]
choice_matrix = [['C', 'A', 'B'], 
                 ['A', 'B', 'C'], 
                 ['B', 'C', 'A']]

def calculate_score(a, b):
    # Choosing score
    score_1 = 1 if b == 'A' else 2 if b == 'B' else 3
    
    # Winning score
    idx = 0 if a == 'A' else 1 if a == 'B' else 2 # Opponents choice
    jdx = 0 if b == 'A' else 1 if b == 'B' else 2 # Your choice

    return score_1 + score_matrix[idx][jdx]

def make_choice(a, res):
    idx = 0 if a == 'A' else 1 if a == 'B' else 2 # Opponents choice
    jdx = 0 if res == 'X' else 1 if res == 'Y' else 2 # Your choice

    return choice_matrix[idx][jdx]

runs = inp.split("\n")

total_score = 0

for run in runs:
    choices = run.split(" ")

    score = calculate_score(choices[0], make_choice(choices[0], choices[1]))
    total_score += score
 
print(total_score)