import sys

def part_1_largest_area(points):
    distance_to_pairs = []
    for x, p1 in enumerate(points):
        for y, p2 in enumerate(points):
            if x != y:
                distance_to_pairs.append([distance_between_points(p1, p2), x, y])
    distance_to_pairs = sorted(distance_to_pairs, key=lambda r: r[0], reverse=True)
    furthest_points = distance_to_pairs[0]
    print(furthest_points)
    p1, p2 = points[furthest_points[1]], points[furthest_points[2]]
    print(p1, p2)
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

#94918,50338
#94918,48430
#19286,13672

def part_2_largest_area_in_green_bf(points):
    walls = []
    for i, p1 in enumerate(points):
        p2 = points[(i + 1) % len(points)]
        walls.append([p1, p2])
    largest_area = 0
    largest_area_p1, largest_area_p2 = None, None
    for x, p1 in enumerate(points):
        for y, p2 in enumerate(points):
            if x != y:
                intersects = False
                corner_1 = [p1[0], p2[1]]
                corner_2 = [p2[0], p1[1]]
                box_walls = [
                    [p1, corner_1],
                    [p1, corner_2],
                    [corner_1, p2],
                    [corner_2, p2]
                ]
                for w in walls:
                    for b in box_walls:
                        if intersect(b[0], b[1], w[0], w[1]):
                            intersects = True
                            break
                if intersects:
                    continue
                target_area = area(p1, p2)
                if area(p1, p2) > largest_area:
                    largest_area_p1 = p1
                    largest_area_p2 = p2
                    largest_area = target_area
    print(largest_area_p1, largest_area_p2)
    return largest_area

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def distance_between_points(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def ccw(p1,p2,p3):
    return (p3[1]-p1[1])*(p2[0]-p1[0]) > (p2[1]-p1[1])*(p3[0]-p1[0])

def intersect(p1,p2,p3,p4):
    if p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4:
        return False
    return ccw(p1,p3,p4) != ccw(p2,p3,p4) and ccw(p1,p2,p3) != ccw(p1,p2,p4)

inp = open(sys.argv[1], 'r')
points = []
try:
    for l in inp.readlines():
        p = [int(i) for i in l.split(",")]
        points.append([p[0], p[1]])

    print("Part 1 Answer:", part_1_largest_area(points))
    print("Part 2 Answer:", part_2_largest_area_in_green_bf(points))
finally:
    inp.close()