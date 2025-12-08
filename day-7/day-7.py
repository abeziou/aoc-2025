import sys
from functools import reduce

def part_1_number_of_splits(graph):
    start_line = graph[0]
    graph = graph[1:]
    s_position = start_line.index('S')
    beam_positions_above = set()
    beam_positions_above.add(s_position)
    split_count = 0
    for i, line in enumerate(graph[1:]):
        new_beam_positions = set()
        for beam_position in beam_positions_above:
            if line[beam_position] == '^':
                split_count += 1
                new_beam_positions.add(beam_position - 1)
                new_beam_positions.add(beam_position + 1)
            else:
                new_beam_positions.add(beam_position)
        beam_positions_above = new_beam_positions
    return split_count

def part_2_number_of_timelines(graph):
    start_line = graph[0]
    graph = graph[1:]
    s_position = start_line.index('S')
    graph[0][s_position] = 1
    beam_positions_above = set()
    beam_positions_above.add(s_position)
    i = 1
    while i != len(graph):
        new_beam_positions = set()
        for beam_position in beam_positions_above:
            if graph[i][beam_position] == '^':
                new_beam_positions.add(beam_position - 1)
                new_beam_positions.add(beam_position + 1)
                if graph[i][beam_position - 1] == '.':
                    graph[i][beam_position - 1] = graph[i - 1][beam_position]
                else:
                    graph[i][beam_position - 1] += graph[i - 1][beam_position]

                if graph[i][beam_position + 1] == '.':
                    graph[i][beam_position + 1] = graph[i - 1][beam_position]
                else:
                    graph[i][beam_position + 1] += graph[i - 1][beam_position]
            else:
                new_beam_positions.add(beam_position)
                if graph[i][beam_position] == '.':
                    graph[i][beam_position] = graph[i - 1][beam_position]
                else:
                    graph[i][beam_position] += graph[i - 1][beam_position]
        beam_positions_above = new_beam_positions
        i += 1
    timelines = 0
    for i in graph[-1]:
        if i != '.':
            timelines += i
    return timelines

inp = open(sys.argv[1], 'r')
graph = []
try:
    for l in inp.readlines():
        graph.append(list(l.strip()))

    print("Part 1 Answer:", part_1_number_of_splits(graph))
    print("Part 2 Answer:", part_2_number_of_timelines(graph))
finally:
    inp.close()