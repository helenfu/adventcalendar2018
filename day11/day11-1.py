size = 300
cells = [[0 for _ in range(size)] for _ in range(size)]

max_val = 0
max_coords = (0, 0)

def sum(input_x, input_y):
    total = 0
    for y in range(input_y, input_y + 3):
        for x in range(input_x, input_x + 3):
            total += cells[x][y]
    return total

try:
    while True:
        serial_number = int(raw_input())

except EOFError:
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            rack = x + 10
            power_level = rack * y
            power_level += serial_number
            power_level = power_level * rack
            power_level = int(str(power_level)[-3])
            power_level -= 5
            cells[x - 1][y - 1] = power_level

    for y in range(size - 3):
        for x in range(size - 3):
            total = sum(x, y)
            if total > max_val:
                max_val = total
                max_coords = (x + 1, y + 1)

print max_coords
