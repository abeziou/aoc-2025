import sys

def part_1_max_rolls(rolls):
    rolls_moved = 0
    for y, roll in enumerate(rolls):
        for x, char in enumerate(roll):
            adjacent_roll_count = 0
            if char == '@':
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if y + dy < 0 or y + dy >= len(rolls):
                            continue
                        if x + dx < 0 or x + dx >= len(roll):
                            continue
                        if rolls[y + dy][x + dx] == '@':
                            adjacent_roll_count += 1
                if adjacent_roll_count < 4:
                    rolls_moved += 1
    return rolls_moved

def part_2_max_rolls(rolls):
    max_rolls_removed = 0
    removal_coordinates = find_roll_removal_coordinates(rolls)
    while len(removal_coordinates) > 0:
        max_rolls_removed += len(removal_coordinates)
        for c in removal_coordinates:
            x, y = c[0], c[1]
            rolls[y][x] = "."
        removal_coordinates = find_roll_removal_coordinates(rolls)
    return max_rolls_removed

def find_roll_removal_coordinates(rolls):
    coordinates = []
    for y, roll in enumerate(rolls):
        for x, char in enumerate(roll):
            adjacent_roll_count = 0
            if char == '@':
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if y + dy < 0 or y + dy >= len(rolls):
                            continue
                        if x + dx < 0 or x + dx >= len(roll):
                            continue
                        if rolls[y + dy][x + dx] == '@':
                            adjacent_roll_count += 1
                if adjacent_roll_count < 4:
                    coordinates.append([x, y])
    return coordinates

inp = open(sys.argv[1], 'r')
rolls = []
try:
    for l in inp.readlines():
        roll = list(l.strip())
        rolls.append(roll)

    print("Part 1 Answer:", part_1_max_rolls(rolls))
    print("Part 2 Answer:", part_2_max_rolls(rolls))
finally:
    inp.close()