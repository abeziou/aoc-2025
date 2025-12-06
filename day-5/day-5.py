import sys

def part_1_number_of_fresh_ingredients(ranges, ingredients):
    fresh_count = 0
    
    for i in ingredients:
        fresh = False
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                fresh = True
                break
        if fresh:
            fresh_count += 1
    return fresh_count

def part_2_number_of_fresh_ingredients(ranges, ingredients):
    ranges = sorted(ranges, key=lambda r: r[0])
    count = 1
    pointer = ranges[0][0]
    for r in ranges:
        if r[0] > pointer:
            pointer = r[0]
            count += 1
        if r[1] > pointer:
            count += r[1] - pointer
            pointer = r[1]
    return count

inp = open(sys.argv[1], 'r')
ranges = []
ingredients = []
try:
    range_stop = False
    for l in inp.readlines():
        if not range_stop:
            if l == "\n":
                range_stop = True
                continue
            ranges.append([int(i) for i in l.split("-")])
        else:
            ingredients.append(int(l))

    print("Part 1 Answer:", part_1_number_of_fresh_ingredients(ranges, ingredients))
    print("Part 2 Answer:", part_2_number_of_fresh_ingredients(ranges, ingredients))
finally:
    inp.close()