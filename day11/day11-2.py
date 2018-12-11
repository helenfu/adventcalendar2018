size = 300
cells = [[0 for _ in range(size)] for _ in range(size)]
sum_x = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size + 1)]
sum_y = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size + 1)]
sums = [[] for _ in range(size + 1)]

max_val = 0
max_coords = (0, 0, 0)

def sum_border(input_x, input_y, square_size):
    total = 0
    total = sums[square_size - 1][input_x][input_y]
    total += sum_x[square_size][input_x + square_size - 1][input_y]
    total += sum_y[square_size][input_x][input_y + square_size - 1]
    total -= cells[input_x + square_size - 1][input_y + square_size - 1]
    return total

def update_sum_x(input_x, input_y, square_size):
    sum_x[square_size][input_x][input_y] = sum_x[square_size - 1][input_x][input_y] + cells[input_x][input_y + square_size - 1]

def update_sum_y(input_x, input_y, square_size):
    sum_y[square_size][input_x][input_y] = sum_y[square_size - 1][input_x][input_y] + cells[input_x + square_size - 1][input_y]

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

    max_total = 0
    max_coords = (0, 0, 0)
    sums[0] = [[0 for _ in range(size)] for _ in range(size)]
    for square_size in range(1, size + 1):
        # print square_size
        sums_size = size - square_size + 1
        sums[square_size] = [[0 for _ in range(sums_size)] for _ in range(sums_size)]
        for y in range(sums_size):
            for x in range(sums_size):
                update_sum_x(x, y, square_size)
                update_sum_y(x, y, square_size)
        for y in range(sums_size):
            for x in range(sums_size):
                sums[square_size][x][y] = sum_border(x, y, square_size)
                if sums[square_size][x][y] > max_total:
                    max_total = sums[square_size][x][y]
                    max_coords = (x + 1, y + 1, square_size)

print max_coords
