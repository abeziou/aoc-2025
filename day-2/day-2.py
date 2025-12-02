import sys
import math

def part_1_invalid_pid_sum(ranges):
    invalid_pid_sum = 0
    for r in ranges:
        first = r[0]
        last = r[1]
        for num in range(first, last + 1):
            number_str = str(num)
            if len(number_str) % 2 == 1:
                continue
            repeats = True
            half_length = len(number_str) // 2
            for i in range(0, half_length):
                if number_str[i] != number_str[i + half_length]:
                    repeats = False
                    break
            if repeats:
                invalid_pid_sum += num
    return invalid_pid_sum

def part_2_invalid_pid_sum_bruteforce(ranges):
    invalid_pid_sum = 0
    for r in ranges:
        first = r[0]
        last = r[1]
        for num in range(first, last + 1):
            number_str = str(num)
            length = 1
            while length < len(number_str):
                if substring_check(number_str, length):
                    invalid_pid_sum += num
                    break
                length += 1
    return invalid_pid_sum

def substring_check(number_str, length):
    substr = number_str[:length]
    if length * 2 > len(number_str):
        return False
    for i in range(math.ceil(len(number_str) / length)):
        if (i+1)*length > len(number_str) or number_str[i*length:(i+1)*length] != substr:
            return False
    return True

inp = open(sys.argv[1], 'r')
ranges = []
try:
    for l in inp.readlines():
        for r in l.split(","):
            rSplit = r.split("-")
            ranges.append([int(rSplit[0]), int(rSplit[1])])

    print("Part 1 Answer:", part_1_invalid_pid_sum(ranges))
    print("Part 2 Answer:", part_2_invalid_pid_sum_bruteforce(ranges))
finally:
    inp.close()