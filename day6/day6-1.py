from sets import Set

areas = []
max_y = -1
max_x = -1
min_x = -1
min_y = -1
edge = Set()

def get_distance(x, y, coord):
    return abs(x - coord[0]) + abs(y - coord[1])

def get_min_distance_index(x, y):
    min_distance = float("inf")
    min_id = -1
    dupe = False
    for area_id, coord in enumerate(areas):
        distance = get_distance(x, y, coord)
        if distance < min_distance:
            min_distance = distance
            min_id = area_id
            dupe = False
        elif distance == min_distance and min_id != -1:
            dupe = True
    if dupe:
        return -1
    return min_id

def isInf(index):
    return index in edge

try:
    while True:
        input = raw_input()
        x, y = input.split(", ")
        x = int(x)
        y = int(y)
        if min_x == -1:
            min_x = x
            max_x = x
            min_y = y
            max_y = y
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        areas.append((x, y))

except EOFError:
    area_sizes = {}
    area_sizes[-1] = 0
    for i in range(len(areas)):
        area_sizes[i] = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1 ):
            min_distance_index = get_min_distance_index(x, y)
            area_sizes[min_distance_index] += 1
            if y == min_y or y == max_y + 1 or x == min_x or x == max_x + 1:
                edge.add(min_distance_index)

    max_area = 0
    for key, size in area_sizes.iteritems():
        if size > max_area and key != -1 and not isInf(key):
            max_area = size

    print max_area
