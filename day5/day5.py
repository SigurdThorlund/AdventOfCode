import numpy as np

with open("day5/data/input.txt", "r") as f:
    inp = f.read()

split_inp = inp.split("\n\n")

crates = split_inp[0]
moves = split_inp[1].split("\n")

rows = crates.split("\n")
rows = rows[:-1] # Eliminate the last row

new_rows = []

for row in reversed(rows):
    new_r = []
    for i in range(0, len(row), 4):
        # Remove the empty crates
        #c = row[i:i+3]
        #if c == '   ':
        #    continue
        #else:
        new_r.append(row[i:i+3])
    new_rows.append(new_r)

spots = [[] for _ in range(9)]
print(spots)

# Transpose new rows (the hard way)
for i, row in enumerate(new_rows):
    for j in range(len(row)):
        if row[j] != "   ":
            spots[j].append(row[j])

def move_crates(moves, spots):
    for text in moves:
        move = text.split(' ')
        n = int(move[1]) # Number of crates to move
        f = int(move[3]) - 1 # From spot (zero-index)
        t = int(move[5]) - 1 # To spot (zero-index)
        
        cs = [] 
        
        for i in range(n):
            c = spots[f].pop()
            cs.append(c)

        for c in reversed(cs):
            spots[t].append(c)

move_crates(moves, spots)

for i in range(len(spots)):
    print(spots[i][-1]) # print the top create
