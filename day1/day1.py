with open('day1/data/input.py', 'r') as f:
    inp = f.read()

# Divide input into separate bags for each elf
bags = inp.split("\n\n")

# Calculate the total amount of calories for each elf
total_calories = []
for bag in bags:
    calories = bag.split("\n")
    calories = [int(food) for food in calories]
    total_calories.append(sum(calories))

# Return the max calories carried
print(max(total_calories))

# Figure out the top three elves by sorting
total_calories.sort(reverse=True)

print(sum(total_calories[:3]))