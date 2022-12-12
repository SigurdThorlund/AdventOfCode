with open('day3/data/input.txt', 'r') as f:
    inp = f.read()


backpacks = inp.split('\n')

priorities = []
### PART 1
for backpack in backpacks:
    n = len(backpack)
    middle = n // 2 # There is always an even length in the backpack

    print(backpack)
    # Split backpacks in the middle
    c1 = backpack[:middle]
    c2 = backpack[middle:]

    # Check if each item in the first compartment is in the second one
    # When found count the priority of that letter
    for c in c1:
        if c in c2: 
            priority = ord(c)
            priority = priority - 96 if priority >= 97 else priority + (26 - 64) 
            priorities.append(priority)
            break

# Sum the priorities
print(sum(priorities))


# ----------- PART 2 ---------------
priorities = []
for i in range(0, len(backpacks), 3):
    b1 = backpacks[i]
    b2 = backpacks[i + 1]
    b3 = backpacks[i + 2]

    # Find one item that is in all three backpacks and return priorirty
    for c in b1:
        if c in b2:
            if c in b3:
                priority = ord(c)
                priority = priority - 96 if priority >= 97 else priority + (26 - 64) 
                priorities.append(priority)
                print('added priority {} for group {}.'.format(priority, i // 3))
                break

print(sum(priorities))