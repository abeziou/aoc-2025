import sys

def part_1_joltage(banks):
    max_joltage = 0
    for bank in banks:
        i1, i2, first_battery, second_battery = 0, 1, bank[0], bank[1]
        for i, battery in enumerate(bank):
            if i == 0 or i == 1:
                continue
            if battery > first_battery and i < len(bank) - 1:
                i1, i2 = i, i + 1
            elif battery > second_battery:
                i2 = i
            first_battery, second_battery = bank[i1], bank[i2]
        max_joltage += 10 * first_battery + second_battery
    return max_joltage

def part_2_joltage(banks):
    max_joltage = 0
    for bank in banks:
        max_joltage += find_max_joltage(bank, 12)
    return max_joltage

def find_max_joltage(bank, number_of_digits):
    max_digit = 10
    indices = []
    if len(bank) == 0:
        return 0
    while len(indices) == 0:
        max_digit -= 1
        indices = find_target_indices(bank[:len(bank) - number_of_digits + 1], max_digit)
    if number_of_digits == 1:
        return max_digit
    max_joltage = 10**(number_of_digits-1) * max_digit
    max_result = 0
    for i in indices:
        result = find_max_joltage(bank[i+1:], number_of_digits - 1)
        if result > max_result:
            max_result = result
    return max_joltage + max_result

def find_target_indices(bank, target):
    indices = []
    for i, battery in enumerate(bank):
        if battery == target:
            indices.append(i)
    return indices

inp = open(sys.argv[1], 'r')
banks = []
try:
    for l in inp.readlines():
        bank = [int(i) for i in list(l.strip())]
        banks.append(bank)

    print("Part 1 Answer:", part_1_joltage(banks))
    print("Part 2 Answer:", part_2_joltage(banks))
finally:
    inp.close()