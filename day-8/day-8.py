import sys

def part_1_3_largest_circuit_size(junctions):
    distance_to_pairs = []
    for x, j1 in enumerate(junctions):
        for y, j2 in enumerate(junctions):
            if x != y:
                distance_to_pairs.append([j1.distance_to(j2), x, y])
    distance_to_pairs = sorted(distance_to_pairs, key=lambda r: r[0])
    shortest_pairs = []
    number_of_pairs = 10
    if len(junctions) == 1000:
        number_of_pairs = 1000
    for i in range(1000):
        shortest_pairs.append(distance_to_pairs[i * 2])

    circuits = []
    for p in shortest_pairs:
        existing_p1_circuit, existing_p2_circuit = None, None
        for i, c in enumerate(circuits):
            if p[1] in c:
                existing_p1_circuit = i
            elif p[2] in c:
                existing_p2_circuit = i
        if existing_p1_circuit == None:
            if existing_p2_circuit == None: 
                circuits.append(set([p[1], p[2]]))
            else:
                circuits[existing_p2_circuit].add(p[1])
        else:
            if existing_p2_circuit == None: 
                circuits[existing_p1_circuit].add(p[2])
            else:
                p2_circuit = circuits[existing_p2_circuit]
                circuits[existing_p1_circuit] = circuits[existing_p1_circuit].union(p2_circuit)
                circuits.pop(existing_p2_circuit)
    circuits = sorted(circuits, key=lambda l: len(l), reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

def part_2_last_2_junctions_x_coordinates(junctions):
    distance_to_pairs = []
    for x, j1 in enumerate(junctions):
        for y, j2 in enumerate(junctions):
            if x != y:
                distance_to_pairs.append([j1.distance_to(j2), x, y])
    distance_to_pairs = sorted(distance_to_pairs, key=lambda r: r[0])
    shortest_pairs = []
    for i in range(0, len(distance_to_pairs) // 2):
        shortest_pairs.append(distance_to_pairs[i * 2])

    junctions_connected = set()
    circuits = []
    pair_i = 0
    while len(circuits) != 1 or len(junctions_connected) < len(junctions):
        p = shortest_pairs[pair_i]
        existing_p1_circuit, existing_p2_circuit = None, None
        for i, c in enumerate(circuits):
            if p[1] in c:
                existing_p1_circuit = i
            elif p[2] in c:
                existing_p2_circuit = i
        if existing_p1_circuit == None:
            if existing_p2_circuit == None: 
                circuits.append(set([p[1], p[2]]))
            else:
                circuits[existing_p2_circuit].add(p[1])
        else:
            if existing_p2_circuit == None: 
                circuits[existing_p1_circuit].add(p[2])
            else:
                p2_circuit = circuits[existing_p2_circuit]
                circuits[existing_p1_circuit] = circuits[existing_p1_circuit].union(p2_circuit)
                circuits.pop(existing_p2_circuit)
        pair_i += 1
        junctions_connected.add(p[1])
        junctions_connected.add(p[2])
    last_pair = shortest_pairs[pair_i - 1]
    return junctions[last_pair[1]].x * junctions[last_pair[2]].x


class Junction:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
    
    def distance_to(self, junction):
        return ((self.x - junction.x)**2 + (self.y - junction.y)**2 + (self.z - junction.z)**2)**0.5

inp = open(sys.argv[1], 'r')
junctions = []
try:
    for l in inp.readlines():
        j = [int(i) for i in l.split(",")]
        junctions.append(Junction(j[0], j[1], j[2]))

    print("Part 1 Answer:", part_1_3_largest_circuit_size(junctions))
    print("Part 2 Answer:", part_2_last_2_junctions_x_coordinates(junctions))
finally:
    inp.close()