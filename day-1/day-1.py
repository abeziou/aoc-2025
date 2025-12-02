import sys

def part_1_password(rotations):
    dial_at_zero_count = 0
    dial = 50
    for r in rotations:
        direction = r[0]
        clicks = r[1]
        if direction == 'L':
            clicks *= -1
        dial = (dial + clicks) % 100
        if dial == 0:
            dial_at_zero_count += 1
    return dial_at_zero_count

def part_2_password(rotations):
    dial_at_zero_count = 0
    dial = 50
    for r in rotations:
        direction = r[0]
        clicks = r[1]
        dial_at_zero_count += clicks // 100
        clicks %= 100
        if direction == 'L':
            if clicks >= dial and dial != 0:
                dial_at_zero_count += 1
            clicks *= -1
        else:
            if clicks + dial >= 100:
                dial_at_zero_count += 1
        dial = (dial + clicks) % 100
    return dial_at_zero_count

inp = open(sys.argv[1], 'r')
rotations = [[l[0], int(l[1:])] for l in inp.readlines()]

print("Part 1 Answer:", part_1_password(rotations))
print("Part 2 Answer:", part_2_password(rotations))