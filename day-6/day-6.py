import sys
from functools import reduce

def part_1_math_answer(lines):
    sum_of_answers = 0
    operations = lines.pop()
    number_lines = []
    for l in lines:
        number_lines.append([int(i) for i in l])
    for i_o, o in enumerate(operations):
        numbers = []
        for number_line in number_lines:
            numbers.append(number_line[i_o])
        if o == '*':
            sum_of_answers += reduce(lambda ans, n: ans * n, numbers)
        else:
            sum_of_answers += reduce(lambda ans, n: ans + n, numbers)
    return sum_of_answers

def part_2_math_answer(lines):
    sum_of_answers = 0
    operations = lines.pop()
    columns_per_operation = []
    count_of_spaces = 1
    for o in operations[1:]:
        if o == ' ':
            count_of_spaces += 1
        else:
            columns_per_operation.append(count_of_spaces - 1)
            count_of_spaces = 1
    columns_per_operation.append(count_of_spaces)
    operations = ''.join(operations).split()
    indentation = 0
    for i_o, o in enumerate(operations):
        numbers = []
        number_of_columns = columns_per_operation[i_o]
        for c in range(number_of_columns):
            c += indentation
            number = ""
            for number_line in lines:
                if number_line[c] != ' ':
                    number += number_line[c]
            numbers.append(int(number))
        if o == '*':
            sum_of_answers += reduce(lambda ans, n: ans * n, numbers)
        else:
            sum_of_answers += reduce(lambda ans, n: ans + n, numbers)
        indentation += number_of_columns + 1
    return sum_of_answers

inp = open(sys.argv[1], 'r')
lines = []
part_2_lines = []
try:
    for l in inp.readlines():
        part_2_lines.append(list(l))
        lines.append(l.split())

    print("Part 1 Answer:", part_1_math_answer(lines))
    print("Part 2 Answer:", part_2_math_answer(part_2_lines))
finally:
    inp.close()