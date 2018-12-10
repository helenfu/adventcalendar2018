# part 2 was basically included in part 1 for this day

from collections import namedtuple

sky_map = {}
min_x = None
max_x = None
min_y = None
max_y = None
curr_time = 0

bounding_box_time = 0
smallest_bounds = None
out_of_bounds = False
curr_bounds = None

def print_stars():
    min_x, min_y, max_x, max_y = curr_bounds
    for y in range(min_y, max_y + 1):
        ans = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in sky_map:
                ans += '#'
            else:
                ans += '.'
        print ans

def bound_width(bound):
    return bound[2] - bound[0]

def bound_height(bound):
    return bound[3] - bound[1]

def update_map(time_pass=1):
    global sky_map
    global smallest_bounds
    global bounding_box_time
    global curr_bounds
    global curr_time
    new_map = {}
    new_bounds = None
    curr_time += time_pass
    for point in sky_map.keys():
        x, y = point
        velocities = sky_map[(x, y)]
        for velocity in velocities:
            new_point = (x + (velocity[0] * time_pass), y + (velocity[1] * time_pass))
            if new_point in new_map:
                new_map[new_point].append(velocity)
            else:
                new_map[new_point] = [velocity]
            new_bounds = update_bounds(new_point[0], new_point[1], new_bounds)

    sky_map = new_map
    curr_bounds = new_bounds
    if smallest_bounds is None:
        smallest_bounds = new_bounds
        bounding_box_time = curr_time
    elif bound_width(new_bounds) <= bound_width(smallest_bounds) and bound_height(new_bounds) <= bound_height(smallest_bounds):
        smallest_bounds = new_bounds
        bounding_box_time = curr_time

def update_bounds(x, y, bounds):
    if bounds is None:
        return (x, y, x, y)

    min_x, min_y, max_x, max_y = bounds
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
    return (min_x, min_y, max_x, max_y)

for input in open('input.txt'):
    open_bracket = input.index('<') + 1
    close_bracket = input.index('>')
    x, y = input[open_bracket:close_bracket].strip().split(', ')
    x = int(x)
    y = int(y)
    point = (x, y)
    # velocity
    open_bracket = input.index('<', open_bracket) + 1
    close_bracket = input.index('>', close_bracket + 1)
    vel_x, vel_y = input[open_bracket:close_bracket].strip().split(', ')
    velocity = (int(vel_x), int(vel_y))

    if point in sky_map:
        sky_map[point].append(velocity)
    else:
        sky_map[point] = [velocity]

    if max_x == None:
        min_x = x
        max_x = x
        min_y = y
        max_y = y
    else:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    curr_bounds = (min_x, min_y, max_x, max_y)
    smallest_bounds = (min_x, min_y, max_x, max_y)

# too lazy to clean up code, but this was the min second
update_map(10418)

# while curr_time >= 10350 and curr_time < 10500:
#     update_map()

# print smallest_bounds
# print bounding_box_time
print_ans()
