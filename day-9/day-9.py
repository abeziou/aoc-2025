import sys

def part_1_largest_area(points):
    distance_to_pairs = []
    for x, p1 in enumerate(points):
        for y, p2 in enumerate(points):
            if x != y:
                distance_to_pairs.append([distance_between_points(p1, p2), x, y])
    distance_to_pairs = sorted(distance_to_pairs, key=lambda r: r[0], reverse=True)
    furthest_points = distance_to_pairs[0]
    p1, p2 = points[furthest_points[1]], points[furthest_points[2]]
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

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
                target_area = area(p1, p2)
                if target_area <= largest_area:
                    continue
                bounding_box_contains_points = False
                for i, tp in enumerate(points):
                    in_x_range = False
                    in_y_range = False
                    if p1[0] < p2[0] and tp[0] > p1[0] and tp[0] < p2[0]:
                        in_x_range = True
                    elif p1[0] > p2[0] and tp[0] < p1[0] and tp[0] > p2[0]:
                        in_x_range = True
                    if p1[1] < p2[1] and tp[1] > p1[1] and tp[1] < p2[1]:
                        in_y_range = True
                    elif p1[1] > p2[1] and tp[1] < p1[1] and tp[1] > p2[1]:
                        in_y_range = True
                    if in_x_range and in_y_range:
                        bounding_box_contains_points = True
                        break
                if bounding_box_contains_points:
                    continue
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
                largest_area = target_area
                largest_area_p1 = p1
                largest_area_p2 = p2

    return largest_area

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def distance_between_points(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def intersect(p1,p2,p3,p4):
    if p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4:
        return False
    upper_p, lower_p = None, None
    left_p, right_p = None, None
    if p1[0] - p2[0] == 0: # Straight vertical line
        if p3[0] - p4[0] == 0: # Cannot intersect other vertical lines
            return False
        if p1[1] > p2[1]:
            upper_p, lower_p = p1, p2
        else:
            upper_p, lower_p = p2, p1
        if p3[0] > p4[0]:
            left_p, right_p = p4, p3
        else:
            left_p, right_p = p3, p4
        
    else: # Straight horizontal line
        if p3[1] - p4[1] == 0: # Cannot intersect other horizontal lines
            return False
        if p1[0] > p2[0]:
            left_p, right_p = p2, p1
        else:
            left_p, right_p = p1, p2
        if p3[1] > p4[1]:
            upper_p, lower_p = p3, p4
        else:
            upper_p, lower_p = p4, p3
    return left_p[1] < upper_p[1] and left_p[1] > lower_p[1] and left_p[0] < upper_p[0] and right_p[0] > upper_p[0]


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