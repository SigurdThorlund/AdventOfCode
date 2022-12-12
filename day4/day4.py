with open('day4/data/input.txt', 'r') as f:
    inp = f.read()

pairs = inp.split("\n")


def fully_contained(s1 : list, s2 : list) -> bool:
    """ Returns true if one set is fully contained in the other """
    s1_start = int(s1[0])
    s1_end = int(s1[1])
    
    s2_start = int(s2[0])
    s2_end = int(s2[1])

    if s1_start >= s2_start and s1_end <= s2_end: return True # S1 contained in s2
    
    if s2_start >= s1_start and s2_end <= s1_end: return True # s2 contained in s1

    return False

def num_overlaps(s1 : list, s2 : list) -> list:
    s1_start = int(s1[0])
    s1_end = int(s1[1])
    
    s2_start = int(s2[0])
    s2_end = int(s2[1])

    # Convert to lists
    s1 = list(range(s1_start, s1_end + 1))
    s2 = list(range(s2_start, s2_end + 1))
    #if len(s1) == 0: s1 = [s1_start]
    #if len(s2) == 0: s2 = [s2_start]

    for s in s1:
        if s in s2:
            return 1

    return 0

fully_contained_pairs = []
overlaps = 0

for pair in pairs:
    # Divide each pair into a stop and a start
    sections = pair.split(",")

    section_1 = sections[0].split("-")
    section_2 = sections[1].split("-")

    # Check if they are fully contained
    if fully_contained(section_1, section_2): 
        fully_contained_pairs.append(pairs)
    
    
    temp = num_overlaps(section_1, section_2)
    overlaps += temp


print('There are {} fully contained pairs out of {}'.format(len(fully_contained_pairs), len(pairs)))
print('There are {} overlapping sections'.format(overlaps))