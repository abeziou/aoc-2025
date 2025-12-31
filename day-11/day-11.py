import sys
from functools import cache

def part_1_number_of_paths(node_positions, adjacency_lists):
    starting_position = node_positions["you"]

    @cache
    def traverse_path(position):
        adjacent_nodes = adjacency_lists[position]
        if len(adjacent_nodes) == 0:
            return 1
        out_paths = 0
        for a in adjacent_nodes:
            out_paths += traverse_path(a)
        return out_paths

    return traverse_path(starting_position)

def part_2_number_of_paths(node_positions, adjacency_lists):
    svr_position = node_positions["svr"]
    fft_position = node_positions["fft"]
    dac_position = node_positions["dac"]

    @cache
    def traverse_path(position, fft_seen, dac_seen):
        adjacent_nodes = adjacency_lists[position]
        if len(adjacent_nodes) == 0:
            if dac_seen and fft_seen:
                return 1
            return 0
        fft_seen = fft_seen or position == fft_position
        dac_seen = dac_seen or position == dac_position
        out_paths = 0
        for a in adjacent_nodes:
            out_paths += traverse_path(a, fft_seen, dac_seen)
        return out_paths

    return traverse_path(svr_position, False, False)


inp = open(sys.argv[1], 'r')
node_positions = {}
adjacency_lists = []
try:
    lines = inp.readlines()
    for i, l in enumerate(lines):
        node_name = l.split(":")[0]
        node_positions[node_name] = i
    
    for i, l in enumerate(lines):
        line = l.split(":")
        node_name = line[0]
        outputs = line[1].strip().split()
        adjacency_list = []
        for o in outputs:
            if o == "out":
                break
            adjacency_list.append(node_positions[o])
        adjacency_lists.append(adjacency_list)
    
    print("Part 1 Answer:", part_1_number_of_paths(node_positions, adjacency_lists))
    print("Part 2 Answer:", part_2_number_of_paths(node_positions, adjacency_lists))
finally:
    inp.close()