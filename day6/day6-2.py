areas = []
max_y = -1
max_x = -1
min_x = -1
min_y = -1
max_distance = 10000

def get_distance(x, y, coord):
    return abs(x - coord[0]) + abs(y - coord[1])

def is_total_distance_less_than(x, y):
    total_distance = 0
    for coord in areas:
        distance = get_distance(x, y, coord)
        total_distance += distance
        # if x == 4 and y == 3:
        #     print distance
        if total_distance >= max_distance:
            return False
    return True

try:
    while True:
        input = raw_input()
        x, y = input.split(", ")
        x = int(x)
        y = int(y)
        if max_x == -1:
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
    area = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if is_total_distance_less_than(x, y):
                area += 1

    print area
